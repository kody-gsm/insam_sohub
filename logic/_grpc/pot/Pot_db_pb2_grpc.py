# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from logic.grpc.base import base_pb2 as logic_dot_grpc_dot_base_dot_base__pb2
from logic.grpc.pot import Pot_db_pb2 as logic_dot_grpc_dot_pot_dot_Pot__db__pb2


class PotTrafficStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.pot_create = channel.unary_unary(
                '/PotTraffic/pot_create',
                request_serializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.Pot.SerializeToString,
                response_deserializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
                )
        self.pot_delete = channel.unary_unary(
                '/PotTraffic/pot_delete',
                request_serializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.SerializeToString,
                response_deserializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
                )
        self.pot_update = channel.unary_unary(
                '/PotTraffic/pot_update',
                request_serializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.SerializeToString,
                response_deserializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
                )
        self.pot_read = channel.unary_unary(
                '/PotTraffic/pot_read',
                request_serializer=logic_dot_grpc_dot_base_dot_base__pb2.AccessToken.SerializeToString,
                response_deserializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
                )
        self.pot_read_list = channel.unary_stream(
                '/PotTraffic/pot_read_list',
                request_serializer=logic_dot_grpc_dot_base_dot_base__pb2.AccessToken.SerializeToString,
                response_deserializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.Pot.FromString,
                )


class PotTrafficServicer(object):
    """Missing associated documentation comment in .proto file."""

    def pot_create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pot_delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pot_update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pot_read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pot_read_list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PotTrafficServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'pot_create': grpc.unary_unary_rpc_method_handler(
                    servicer.pot_create,
                    request_deserializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.Pot.FromString,
                    response_serializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.SerializeToString,
            ),
            'pot_delete': grpc.unary_unary_rpc_method_handler(
                    servicer.pot_delete,
                    request_deserializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.FromString,
                    response_serializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.SerializeToString,
            ),
            'pot_update': grpc.unary_unary_rpc_method_handler(
                    servicer.pot_update,
                    request_deserializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.FromString,
                    response_serializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.SerializeToString,
            ),
            'pot_read': grpc.unary_unary_rpc_method_handler(
                    servicer.pot_read,
                    request_deserializer=logic_dot_grpc_dot_base_dot_base__pb2.AccessToken.FromString,
                    response_serializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.SerializeToString,
            ),
            'pot_read_list': grpc.unary_stream_rpc_method_handler(
                    servicer.pot_read_list,
                    request_deserializer=logic_dot_grpc_dot_base_dot_base__pb2.AccessToken.FromString,
                    response_serializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.Pot.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PotTraffic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PotTraffic(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def pot_create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PotTraffic/pot_create',
            logic_dot_grpc_dot_pot_dot_Pot__db__pb2.Pot.SerializeToString,
            logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pot_delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PotTraffic/pot_delete',
            logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.SerializeToString,
            logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pot_update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PotTraffic/pot_update',
            logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.SerializeToString,
            logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pot_read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PotTraffic/pot_read',
            logic_dot_grpc_dot_base_dot_base__pb2.AccessToken.SerializeToString,
            logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pot_read_list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/PotTraffic/pot_read_list',
            logic_dot_grpc_dot_base_dot_base__pb2.AccessToken.SerializeToString,
            logic_dot_grpc_dot_pot_dot_Pot__db__pb2.Pot.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class UserPotTrafficStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.user_add_pot = channel.unary_unary(
                '/UserPotTraffic/user_add_pot',
                request_serializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.SerializeToString,
                response_deserializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
                )
        self.user_remove_pot = channel.unary_unary(
                '/UserPotTraffic/user_remove_pot',
                request_serializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.SerializeToString,
                response_deserializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
                )
        self.user_read_pot_list = channel.unary_stream(
                '/UserPotTraffic/user_read_pot_list',
                request_serializer=logic_dot_grpc_dot_base_dot_base__pb2.AccessToken.SerializeToString,
                response_deserializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.Pot.FromString,
                )


class UserPotTrafficServicer(object):
    """Missing associated documentation comment in .proto file."""

    def user_add_pot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def user_remove_pot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def user_read_pot_list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserPotTrafficServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'user_add_pot': grpc.unary_unary_rpc_method_handler(
                    servicer.user_add_pot,
                    request_deserializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.FromString,
                    response_serializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.SerializeToString,
            ),
            'user_remove_pot': grpc.unary_unary_rpc_method_handler(
                    servicer.user_remove_pot,
                    request_deserializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.FromString,
                    response_serializer=logic_dot_grpc_dot_base_dot_base__pb2.Response.SerializeToString,
            ),
            'user_read_pot_list': grpc.unary_stream_rpc_method_handler(
                    servicer.user_read_pot_list,
                    request_deserializer=logic_dot_grpc_dot_base_dot_base__pb2.AccessToken.FromString,
                    response_serializer=logic_dot_grpc_dot_pot_dot_Pot__db__pb2.Pot.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'UserPotTraffic', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserPotTraffic(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def user_add_pot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserPotTraffic/user_add_pot',
            logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.SerializeToString,
            logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def user_remove_pot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/UserPotTraffic/user_remove_pot',
            logic_dot_grpc_dot_pot_dot_Pot__db__pb2.CertifiedPot.SerializeToString,
            logic_dot_grpc_dot_base_dot_base__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def user_read_pot_list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/UserPotTraffic/user_read_pot_list',
            logic_dot_grpc_dot_base_dot_base__pb2.AccessToken.SerializeToString,
            logic_dot_grpc_dot_pot_dot_Pot__db__pb2.Pot.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
