# This file was generated by `genrpcstubs` from the CLN JSON-Schema.
# Do not edit this file.
from .tls import TlsConfig
from . import glclient as native
import logging
from .node_pb2 import *  # noqa: F401,F403
from . import node_pb2 as clnpb


class Node(object):
    def __init__(
            self,
            node_id: bytes,
            network: str,
            tls: TlsConfig,
            grpc_uri: str
    ):
        self.tls = tls
        self.grpc_uri = grpc_uri
        self.inner = native.Node(
            node_id=node_id,
            network=network,
            tls=tls.inner,
            grpc_uri=grpc_uri
        )
        self.logger = logging.getLogger("glclient.rpc.Node")

    def getinfo(
            self,

    ):
        uri = "/cln.Node/Getinfo"
        req = clnpb.GetinfoRequest(

        ).SerializeToString()
        res = clnpb.GetinfoResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def list_peers(
            self,
            id=None,
            level=None
    ):
        uri = "/cln.Node/ListPeers"
        req = clnpb.ListpeersRequest(
            id=id,
            level=level
        ).SerializeToString()
        res = clnpb.ListpeersResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def list_funds(
            self,
            spent=None
    ):
        uri = "/cln.Node/ListFunds"
        req = clnpb.ListfundsRequest(
            spent=spent
        ).SerializeToString()
        res = clnpb.ListfundsResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def send_pay(
            self,
            route,
            payment_hash,
            label=None,
            amount_msat=None,
            bolt11=None,
            payment_secret=None,
            partid=None,
            localinvreqid=None,
            groupid=None
    ):
        uri = "/cln.Node/SendPay"
        req = clnpb.SendpayRequest(
            route=route,
            payment_hash=payment_hash,
            label=label,
            amount_msat=amount_msat,
            bolt11=bolt11,
            payment_secret=payment_secret,
            partid=partid,
            localinvreqid=localinvreqid,
            groupid=groupid
        ).SerializeToString()
        res = clnpb.SendpayResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def list_channels(
            self,
            short_channel_id=None,
            source=None,
            destination=None
    ):
        uri = "/cln.Node/ListChannels"
        req = clnpb.ListchannelsRequest(
            short_channel_id=short_channel_id,
            source=source,
            destination=destination
        ).SerializeToString()
        res = clnpb.ListchannelsResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def add_gossip(
            self,
            message
    ):
        uri = "/cln.Node/AddGossip"
        req = clnpb.AddgossipRequest(
            message=message
        ).SerializeToString()
        res = clnpb.AddgossipResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def auto_clean_invoice(
            self,
            expired_by=None,
            cycle_seconds=None
    ):
        uri = "/cln.Node/AutoCleanInvoice"
        req = clnpb.AutocleaninvoiceRequest(
            expired_by=expired_by,
            cycle_seconds=cycle_seconds
        ).SerializeToString()
        res = clnpb.AutocleaninvoiceResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def check_message(
            self,
            message,
            zbase,
            pubkey=None
    ):
        uri = "/cln.Node/CheckMessage"
        req = clnpb.CheckmessageRequest(
            message=message,
            zbase=zbase,
            pubkey=pubkey
        ).SerializeToString()
        res = clnpb.CheckmessageResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def close(
            self,
            id,
            unilateraltimeout=None,
            destination=None,
            fee_negotiation_step=None,
            wrong_funding=None,
            force_lease_closed=None,
            feerange=None
    ):
        uri = "/cln.Node/Close"
        req = clnpb.CloseRequest(
            id=id,
            unilateraltimeout=unilateraltimeout,
            destination=destination,
            fee_negotiation_step=fee_negotiation_step,
            wrong_funding=wrong_funding,
            force_lease_closed=force_lease_closed,
            feerange=feerange
        ).SerializeToString()
        res = clnpb.CloseResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def connect_peer(
            self,
            id,
            host=None,
            port=None
    ):
        uri = "/cln.Node/ConnectPeer"
        req = clnpb.ConnectRequest(
            id=id,
            host=host,
            port=port
        ).SerializeToString()
        res = clnpb.ConnectResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def create_invoice(
            self,
            invstring,
            label,
            preimage
    ):
        uri = "/cln.Node/CreateInvoice"
        req = clnpb.CreateinvoiceRequest(
            invstring=invstring,
            label=label,
            preimage=preimage
        ).SerializeToString()
        res = clnpb.CreateinvoiceResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def datastore(
            self,
            key,
            string=None,
            hex=None,
            mode=None,
            generation=None
    ):
        uri = "/cln.Node/Datastore"
        req = clnpb.DatastoreRequest(
            key=key,
            string=string,
            hex=hex,
            mode=mode,
            generation=generation
        ).SerializeToString()
        res = clnpb.DatastoreResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def create_onion(
            self,
            hops,
            assocdata,
            session_key=None,
            onion_size=None
    ):
        uri = "/cln.Node/CreateOnion"
        req = clnpb.CreateonionRequest(
            hops=hops,
            assocdata=assocdata,
            session_key=session_key,
            onion_size=onion_size
        ).SerializeToString()
        res = clnpb.CreateonionResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def del_datastore(
            self,
            key,
            generation=None
    ):
        uri = "/cln.Node/DelDatastore"
        req = clnpb.DeldatastoreRequest(
            key=key,
            generation=generation
        ).SerializeToString()
        res = clnpb.DeldatastoreResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def del_expired_invoice(
            self,
            maxexpirytime=None
    ):
        uri = "/cln.Node/DelExpiredInvoice"
        req = clnpb.DelexpiredinvoiceRequest(
            maxexpirytime=maxexpirytime
        ).SerializeToString()
        res = clnpb.DelexpiredinvoiceResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def del_invoice(
            self,
            label,
            status,
            desconly=None
    ):
        uri = "/cln.Node/DelInvoice"
        req = clnpb.DelinvoiceRequest(
            label=label,
            status=status,
            desconly=desconly
        ).SerializeToString()
        res = clnpb.DelinvoiceResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def invoice(
            self,
            amount_msat,
            description,
            label,
            expiry=None,
            fallbacks=None,
            preimage=None,
            exposeprivatechannels=None,
            cltv=None,
            deschashonly=None
    ):
        uri = "/cln.Node/Invoice"
        req = clnpb.InvoiceRequest(
            amount_msat=amount_msat,
            description=description,
            label=label,
            expiry=expiry,
            fallbacks=fallbacks,
            preimage=preimage,
            exposeprivatechannels=exposeprivatechannels,
            cltv=cltv,
            deschashonly=deschashonly
        ).SerializeToString()
        res = clnpb.InvoiceResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def list_datastore(
            self,
            key=None
    ):
        uri = "/cln.Node/ListDatastore"
        req = clnpb.ListdatastoreRequest(
            key=key
        ).SerializeToString()
        res = clnpb.ListdatastoreResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def list_invoices(
            self,
            label=None,
            invstring=None,
            payment_hash=None,
            offer_id=None
    ):
        uri = "/cln.Node/ListInvoices"
        req = clnpb.ListinvoicesRequest(
            label=label,
            invstring=invstring,
            payment_hash=payment_hash,
            offer_id=offer_id
        ).SerializeToString()
        res = clnpb.ListinvoicesResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def send_onion(
            self,
            onion,
            first_hop,
            payment_hash,
            label=None,
            shared_secrets=None,
            partid=None,
            bolt11=None,
            amount_msat=None,
            destination=None,
            localinvreqid=None,
            groupid=None
    ):
        uri = "/cln.Node/SendOnion"
        req = clnpb.SendonionRequest(
            onion=onion,
            first_hop=first_hop,
            payment_hash=payment_hash,
            label=label,
            shared_secrets=shared_secrets,
            partid=partid,
            bolt11=bolt11,
            amount_msat=amount_msat,
            destination=destination,
            localinvreqid=localinvreqid,
            groupid=groupid
        ).SerializeToString()
        res = clnpb.SendonionResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def list_send_pays(
            self,
            bolt11=None,
            payment_hash=None,
            status=None
    ):
        uri = "/cln.Node/ListSendPays"
        req = clnpb.ListsendpaysRequest(
            bolt11=bolt11,
            payment_hash=payment_hash,
            status=status
        ).SerializeToString()
        res = clnpb.ListsendpaysResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def list_transactions(
            self,

    ):
        uri = "/cln.Node/ListTransactions"
        req = clnpb.ListtransactionsRequest(

        ).SerializeToString()
        res = clnpb.ListtransactionsResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def pay(
            self,
            bolt11,
            amount_msat=None,
            label=None,
            riskfactor=None,
            maxfeepercent=None,
            retry_for=None,
            maxdelay=None,
            exemptfee=None,
            localinvreqid=None,
            exclude=None,
            maxfee=None,
            description=None
    ):
        uri = "/cln.Node/Pay"
        req = clnpb.PayRequest(
            bolt11=bolt11,
            amount_msat=amount_msat,
            label=label,
            riskfactor=riskfactor,
            maxfeepercent=maxfeepercent,
            retry_for=retry_for,
            maxdelay=maxdelay,
            exemptfee=exemptfee,
            localinvreqid=localinvreqid,
            exclude=exclude,
            maxfee=maxfee,
            description=description
        ).SerializeToString()
        res = clnpb.PayResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def list_nodes(
            self,
            id=None
    ):
        uri = "/cln.Node/ListNodes"
        req = clnpb.ListnodesRequest(
            id=id
        ).SerializeToString()
        res = clnpb.ListnodesResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def wait_any_invoice(
            self,
            lastpay_index=None,
            timeout=None
    ):
        uri = "/cln.Node/WaitAnyInvoice"
        req = clnpb.WaitanyinvoiceRequest(
            lastpay_index=lastpay_index,
            timeout=timeout
        ).SerializeToString()
        res = clnpb.WaitanyinvoiceResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def wait_invoice(
            self,
            label
    ):
        uri = "/cln.Node/WaitInvoice"
        req = clnpb.WaitinvoiceRequest(
            label=label
        ).SerializeToString()
        res = clnpb.WaitinvoiceResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def wait_send_pay(
            self,
            payment_hash,
            timeout=None,
            partid=None,
            groupid=None
    ):
        uri = "/cln.Node/WaitSendPay"
        req = clnpb.WaitsendpayRequest(
            payment_hash=payment_hash,
            timeout=timeout,
            partid=partid,
            groupid=groupid
        ).SerializeToString()
        res = clnpb.WaitsendpayResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def new_addr(
            self,
            addresstype=None
    ):
        uri = "/cln.Node/NewAddr"
        req = clnpb.NewaddrRequest(
            addresstype=addresstype
        ).SerializeToString()
        res = clnpb.NewaddrResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def withdraw(
            self,
            destination,
            satoshi=None,
            feerate=None,
            minconf=None,
            utxos=None
    ):
        uri = "/cln.Node/Withdraw"
        req = clnpb.WithdrawRequest(
            destination=destination,
            satoshi=satoshi,
            feerate=feerate,
            minconf=minconf,
            utxos=utxos
        ).SerializeToString()
        res = clnpb.WithdrawResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def key_send(
            self,
            destination,
            amount_msat,
            label=None,
            maxfeepercent=None,
            retry_for=None,
            maxdelay=None,
            exemptfee=None,
            routehints=None,
            extratlvs=None
    ):
        uri = "/cln.Node/KeySend"
        req = clnpb.KeysendRequest(
            destination=destination,
            amount_msat=amount_msat,
            label=label,
            maxfeepercent=maxfeepercent,
            retry_for=retry_for,
            maxdelay=maxdelay,
            exemptfee=exemptfee,
            routehints=routehints,
            extratlvs=extratlvs
        ).SerializeToString()
        res = clnpb.KeysendResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def fund_psbt(
            self,
            satoshi,
            feerate,
            startweight,
            minconf=None,
            reserve=None,
            locktime=None,
            min_witness_weight=None,
            excess_as_change=None
    ):
        uri = "/cln.Node/FundPsbt"
        req = clnpb.FundpsbtRequest(
            satoshi=satoshi,
            feerate=feerate,
            startweight=startweight,
            minconf=minconf,
            reserve=reserve,
            locktime=locktime,
            min_witness_weight=min_witness_weight,
            excess_as_change=excess_as_change
        ).SerializeToString()
        res = clnpb.FundpsbtResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def send_psbt(
            self,
            psbt,
            reserve=None
    ):
        uri = "/cln.Node/SendPsbt"
        req = clnpb.SendpsbtRequest(
            psbt=psbt,
            reserve=reserve
        ).SerializeToString()
        res = clnpb.SendpsbtResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def sign_psbt(
            self,
            psbt,
            signonly=None
    ):
        uri = "/cln.Node/SignPsbt"
        req = clnpb.SignpsbtRequest(
            psbt=psbt,
            signonly=signonly
        ).SerializeToString()
        res = clnpb.SignpsbtResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def utxo_psbt(
            self,
            satoshi,
            feerate,
            startweight,
            utxos,
            reserve=None,
            reservedok=None,
            locktime=None,
            min_witness_weight=None,
            excess_as_change=None
    ):
        uri = "/cln.Node/UtxoPsbt"
        req = clnpb.UtxopsbtRequest(
            satoshi=satoshi,
            feerate=feerate,
            startweight=startweight,
            utxos=utxos,
            reserve=reserve,
            reservedok=reservedok,
            locktime=locktime,
            min_witness_weight=min_witness_weight,
            excess_as_change=excess_as_change
        ).SerializeToString()
        res = clnpb.UtxopsbtResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def tx_discard(
            self,
            txid
    ):
        uri = "/cln.Node/TxDiscard"
        req = clnpb.TxdiscardRequest(
            txid=txid
        ).SerializeToString()
        res = clnpb.TxdiscardResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def tx_prepare(
            self,
            outputs,
            feerate=None,
            minconf=None,
            utxos=None
    ):
        uri = "/cln.Node/TxPrepare"
        req = clnpb.TxprepareRequest(
            outputs=outputs,
            feerate=feerate,
            minconf=minconf,
            utxos=utxos
        ).SerializeToString()
        res = clnpb.TxprepareResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def tx_send(
            self,
            txid
    ):
        uri = "/cln.Node/TxSend"
        req = clnpb.TxsendRequest(
            txid=txid
        ).SerializeToString()
        res = clnpb.TxsendResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def disconnect(
            self,
            id,
            force=None
    ):
        uri = "/cln.Node/Disconnect"
        req = clnpb.DisconnectRequest(
            id=id,
            force=force
        ).SerializeToString()
        res = clnpb.DisconnectResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def feerates(
            self,
            style
    ):
        uri = "/cln.Node/Feerates"
        req = clnpb.FeeratesRequest(
            style=style
        ).SerializeToString()
        res = clnpb.FeeratesResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def fund_channel_cancel(
            self,
            id
    ):
        uri = "/cln.Node/FundChannelCancel"
        req = clnpb.FundchannelcancelRequest(
            id=id
        ).SerializeToString()
        res = clnpb.FundchannelcancelResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def fund_channel_complete(
            self,
            id,
            psbt
    ):
        uri = "/cln.Node/FundChannelComplete"
        req = clnpb.FundchannelcompleteRequest(
            id=id,
            psbt=psbt
        ).SerializeToString()
        res = clnpb.FundchannelcompleteResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def fund_channel(
            self,
            id,
            amount,
            feerate=None,
            announce=None,
            minconf=None,
            push_msat=None,
            close_to=None,
            request_amt=None,
            compact_lease=None,
            utxos=None,
            mindepth=None,
            reserve=None
    ):
        uri = "/cln.Node/FundChannel"
        req = clnpb.FundchannelRequest(
            id=id,
            amount=amount,
            feerate=feerate,
            announce=announce,
            minconf=minconf,
            push_msat=push_msat,
            close_to=close_to,
            request_amt=request_amt,
            compact_lease=compact_lease,
            utxos=utxos,
            mindepth=mindepth,
            reserve=reserve
        ).SerializeToString()
        res = clnpb.FundchannelResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def fund_channel_start(
            self,
            id,
            amount,
            feerate=None,
            announce=None,
            close_to=None,
            push_msat=None
    ):
        uri = "/cln.Node/FundChannelStart"
        req = clnpb.FundchannelstartRequest(
            id=id,
            amount=amount,
            feerate=feerate,
            announce=announce,
            close_to=close_to,
            push_msat=push_msat
        ).SerializeToString()
        res = clnpb.FundchannelstartResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def get_route(
            self,
            id,
            amount_msat,
            riskfactor,
            cltv=None,
            fromid=None,
            fuzzpercent=None,
            exclude=None,
            maxhops=None
    ):
        uri = "/cln.Node/GetRoute"
        req = clnpb.GetrouteRequest(
            id=id,
            amount_msat=amount_msat,
            riskfactor=riskfactor,
            cltv=cltv,
            fromid=fromid,
            fuzzpercent=fuzzpercent,
            exclude=exclude,
            maxhops=maxhops
        ).SerializeToString()
        res = clnpb.GetrouteResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def list_forwards(
            self,
            status=None,
            in_channel=None,
            out_channel=None
    ):
        uri = "/cln.Node/ListForwards"
        req = clnpb.ListforwardsRequest(
            status=status,
            in_channel=in_channel,
            out_channel=out_channel
        ).SerializeToString()
        res = clnpb.ListforwardsResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def list_pays(
            self,
            bolt11=None,
            payment_hash=None,
            status=None
    ):
        uri = "/cln.Node/ListPays"
        req = clnpb.ListpaysRequest(
            bolt11=bolt11,
            payment_hash=payment_hash,
            status=status
        ).SerializeToString()
        res = clnpb.ListpaysResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def ping(
            self,
            id,
            len=None,
            pongbytes=None
    ):
        uri = "/cln.Node/Ping"
        req = clnpb.PingRequest(
            id=id,
            len=len,
            pongbytes=pongbytes
        ).SerializeToString()
        res = clnpb.PingResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def set_channel(
            self,
            id,
            feebase=None,
            feeppm=None,
            htlcmin=None,
            htlcmax=None,
            enforcedelay=None
    ):
        uri = "/cln.Node/SetChannel"
        req = clnpb.SetchannelRequest(
            id=id,
            feebase=feebase,
            feeppm=feeppm,
            htlcmin=htlcmin,
            htlcmax=htlcmax,
            enforcedelay=enforcedelay
        ).SerializeToString()
        res = clnpb.SetchannelResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def sign_message(
            self,
            message
    ):
        uri = "/cln.Node/SignMessage"
        req = clnpb.SignmessageRequest(
            message=message
        ).SerializeToString()
        res = clnpb.SignmessageResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )

    def stop(
            self,

    ):
        uri = "/cln.Node/Stop"
        req = clnpb.StopRequest(

        ).SerializeToString()
        res = clnpb.StopResponse
        return res.FromString(
            bytes(self.inner.call(uri, bytes(req)))
        )
