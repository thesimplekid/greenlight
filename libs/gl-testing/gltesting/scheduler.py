from glclient import scheduler_pb2_grpc as schedgrpc
from glclient import scheduler_pb2 as schedpb
from concurrent.futures import ThreadPoolExecutor
import grpc
import logging
import tempfile
from pathlib import Path
from gltesting import certs
from dataclasses import dataclass
from gltesting.identity import Identity
import os
import subprocess
import shutil
from typing import Optional
from gltesting.utils import NodeVersion, SignerVersion, Network
from gltesting.node import NodeProcess
from pyln.testing.utils import BitcoinD
from threading import Condition
from pyln.client import LightningRpc
import time
import socket

@dataclass
class Node:
    node_id: bytes
    signer_version: SignerVersion
    directory: Path
    network: Network
    initmsg: bytes
    identity: Identity
    process: Optional[NodeProcess]
    plugin_grpc_uri: Optional[str]
    # Condition we wait on in GetNodeInfo for signers
    condition: Condition

    def rpc(self) -> LightningRpc:
        return LightningRpc(self.directory / "regtest" / "lightning-rpc")


@dataclass
class Challenge:
    node_id: bytes
    challenge: bytes
    scope: str
    used: bool


def enumerate_cln_versions():
    """Search `$PATH` and `$CLN_PATH` for CLN versions."""
    path = os.environ["PATH"].split(":")
    path += os.environ.get("CLN_PATH", "").split(":")
    path = [p for p in path if p != ""]
    version_paths = [shutil.which("lightningd", path=p) for p in path]
    version_paths = [p for p in version_paths if p is not None]

    versions = {}
    for v in version_paths:
        vs = subprocess.check_output([v, "--version"]).strip().decode("ASCII")
        versions[vs] = NodeVersion(path=Path(v).resolve(), name=vs)

    logging.info(f"Found {len(versions)} versions: {versions}")
    return versions


class Scheduler(object):
    """A mock Scheduler simulating Greenlight's behavior."""

    def __init__(self, bitcoind: BitcoinD, grpc_port=2601, identity=None, node_directory=None):
        self.grpc_port = grpc_port
        self.server = None
        print("Starting scheduler with caroot", identity.caroot)
        self.identity = identity
        self.challenges: List[Challenge] = []
        self.next_challenge: int = 1
        self.nodes: List[Node] = []
        self.versions = enumerate_cln_versions()
        self.bitcoind = bitcoind

        if node_directory is not None:
            self.node_directory = node_directory
        else:
            self.node_directory = Path(tempfile.mkdtemp())

    @property
    def grpc_addr(self):
        return f"https://localhost:{self.grpc_port}"

    def start(self):
        logging.info(f"Starting scheduler on port {self.grpc_port}")
        if self.server is not None:
            raise ValueError("Server already running")

        cred = self.identity.to_server_credentials()
        self.server = grpc.server(ThreadPoolExecutor(max_workers=10))
        schedgrpc.add_SchedulerServicer_to_server(self, self.server)
        self.server.add_secure_port(f"[::]:{self.grpc_port}", cred)
        self.server.start()
        logging.info(f"Scheduler started on port {self.grpc_port}")

    def stop(self):
        self.server.stop(grace=1)
        self.server = None
        for n in self.nodes:
            if n.process:
                n.process.stop()
                n.process = None

    def get_node(self, node_id):
        for n in self.nodes:
            if n.node_id == node_id:
                return n
        raise ValueError(
            f"No node with node_id={node_id} found in gltesting scheduler, do you need to register it first?"
        )

    def Register(self, req: schedpb.RegistrationRequest, ctx):
        challenge = None
        for c in self.challenges:
            if c.challenge == req.challenge and not c.used:
                challenge = c
                break
        assert challenge is not None
        assert challenge.node_id == req.node_id
        assert challenge.scope == schedpb.ChallengeScope.REGISTER
        # TODO Verify that the response matches the challenge.

        # Check that we don't already have this node registered:
        if len([n for n in self.nodes if n.node_id == req.node_id]) > 0:
            raise ValueError(
                "could not register the node with the DB, does the node already exist?"
            )

        num = len(self.nodes)
        hex_node_id = challenge.node_id.hex()
        certs.genca(f"/users/{hex_node_id}")

        # Check if the request contains a csr and use it to generate the 
        # certificate. Use the old flow if csr is not present.
        if req.csr is not None:
            device_cert = certs.gencert_from_csr(req.csr)
        else:
            device_cert = certs.gencert(f"/users/{hex_node_id}/device")
        node_cert = certs.gencert(f"/users/{hex_node_id}/node")
        
        directory = self.node_directory / f"node-{num}"
        directory.mkdir(parents=True)

        vstr = req.signer_proto if req.signer_proto is not None else "v0.10.1"
        sv = SignerVersion(name=vstr)

        self.nodes.append(
            Node(
                node_id=req.node_id,
                signer_version=sv,
                initmsg=req.init_msg,
                network=req.network,
                directory=directory,
                identity=node_cert,
                process=None,
                plugin_grpc_uri=None,
                condition=Condition(),
            )
        )

        crt = device_cert
        key = None

        # No csr was provided, we need to get the cert and the key from the
        # identity.
        if req.csr is None:
            crt = device_cert.cert_chain
            key = device_cert.private_key

        return schedpb.RegistrationResponse(
            device_cert=crt,
            device_key=key,
        )

    def Recover(self, req, ctx):
        challenge = None
        for c in self.challenges:
            if c.challenge == req.challenge and not c.used:
                challenge = c
                break
        assert challenge is not None
        assert challenge.node_id == req.node_id
        assert challenge.scope == schedpb.ChallengeScope.RECOVER
        # TODO Verify that the response matches the challenge.
        hex_node_id = challenge.node_id.hex()
        
        # Check if the request contains a csr and use it to generate the 
        # certificate. Use the old flow if csr is not present.
        if req.csr is not None:
            device_cert = certs.gencert_from_csr(req.csr, recover=True)
            device_key = None
        else:
            device_id = certs.gencert(f"/users/{hex_node_id}/recover-{len(self.challenges)}")
            device_key = device_id.private_key
            device_cert = device_id.cert_chain

        return schedpb.RecoveryResponse(
            device_cert=device_cert,
            device_key=device_key
        )

    def GetChallenge(self, req, ctx):
        challenge = Challenge(
            node_id=req.node_id,
            scope=req.scope,
            challenge=bytes([self.next_challenge] * 32),
            used=False,
        )
        self.next_challenge = (self.next_challenge + 1) % 256

        self.challenges.append(challenge)

        return schedpb.ChallengeResponse(challenge=challenge.challenge)

    def Schedule(self, req, ctx):
        n = self.get_node(req.node_id)

        # If already running we just return the existing binding
        if n.process:
            return schedpb.NodeInfoResponse(
                node_id=n.node_id,
                grpc_uri=n.process.grpc_uri,
            )

        node_version = n.signer_version.get_node_version()
        node_version = self.versions[node_version]
        # Otherwise we need to start a new process
        n.process = NodeProcess(
            node_id=req.node_id,
            init_msg=n.initmsg,
            directory=n.directory,
            network=n.network,
            identity=n.identity,
            version=node_version,
            bitcoind=self.bitcoind,
        )
        n.process.start()

        with n.condition:
            n.condition.notify_all()

        # Wait for the grpc port to be accessible
        start_time = time.perf_counter()
        timeout = 10
        while True:
            try:
                with socket.create_connection(("localhost", n.process.grpc_port), timeout=0.1):
                    break
            except:
                time.sleep(0.01)
                if time.perf_counter() - start_time >= timeout:
                    raise TimeoutError(f'Waited too for port localhost:{n.process.grpc_port} to become reachable')
        # TODO Actually wait for the port to be accessible
        time.sleep(1)

        return schedpb.NodeInfoResponse(
            node_id=n.node_id,
            grpc_uri=n.process.grpc_uri,
        )

    def GetNodeInfo(self, req, ctx):
        node = self.get_node(req.node_id)

        if req.wait:
            with node.condition:
                while node.process.proc is None:
                    logging.info(f"Signer waiting for node {node.node_id.hex()} to get scheduled")
                    node.condition.wait()

        return schedpb.NodeInfoResponse(
            node_id=req.node_id,
            grpc_uri=node.process.grpc_uri
        )

    def MaybeUpgrade(self, req, ctx):
        # Very roundabout way of extracting the x509 common name from
        # which we can extract the node_id
        # TODO Implement version ordering and upgrade here
        #common_name = ctx.auth_context()['x509_common_name'][0].decode('ASCII')
        #node_id = common_name.split('/')[2]
        #node = self.get_node(unhexlify(node_id))

        return schedpb.UpgradeResponse(
            old_version="v0.11.0.1",
        )
