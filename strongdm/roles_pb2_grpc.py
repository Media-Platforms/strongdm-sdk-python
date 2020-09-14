# Copyright 2020 StrongDM Inc
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# 
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import roles_pb2 as roles__pb2


class RolesStub(object):
    """Roles are tools for controlling user access to resources. Each Role holds a
    list of resources which they grant access to. Composite roles are a special
    type of Role which have no resource associations of their own, but instead
    grant access to the combined resources associated with a set of child roles.
    Each user can be a member of one Role or composite role.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/v1.Roles/Create',
                request_serializer=roles__pb2.RoleCreateRequest.SerializeToString,
                response_deserializer=roles__pb2.RoleCreateResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/v1.Roles/Get',
                request_serializer=roles__pb2.RoleGetRequest.SerializeToString,
                response_deserializer=roles__pb2.RoleGetResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/v1.Roles/Update',
                request_serializer=roles__pb2.RoleUpdateRequest.SerializeToString,
                response_deserializer=roles__pb2.RoleUpdateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/v1.Roles/Delete',
                request_serializer=roles__pb2.RoleDeleteRequest.SerializeToString,
                response_deserializer=roles__pb2.RoleDeleteResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/v1.Roles/List',
                request_serializer=roles__pb2.RoleListRequest.SerializeToString,
                response_deserializer=roles__pb2.RoleListResponse.FromString,
                )


class RolesServicer(object):
    """Roles are tools for controlling user access to resources. Each Role holds a
    list of resources which they grant access to. Composite roles are a special
    type of Role which have no resource associations of their own, but instead
    grant access to the combined resources associated with a set of child roles.
    Each user can be a member of one Role or composite role.
    """

    def Create(self, request, context):
        """Create registers a new Role.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get reads one Role by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update patches a Role by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete removes a Role by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List gets a list of Roles matching a given set of criteria.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RolesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=roles__pb2.RoleCreateRequest.FromString,
                    response_serializer=roles__pb2.RoleCreateResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=roles__pb2.RoleGetRequest.FromString,
                    response_serializer=roles__pb2.RoleGetResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=roles__pb2.RoleUpdateRequest.FromString,
                    response_serializer=roles__pb2.RoleUpdateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=roles__pb2.RoleDeleteRequest.FromString,
                    response_serializer=roles__pb2.RoleDeleteResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=roles__pb2.RoleListRequest.FromString,
                    response_serializer=roles__pb2.RoleListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.Roles', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Roles(object):
    """Roles are tools for controlling user access to resources. Each Role holds a
    list of resources which they grant access to. Composite roles are a special
    type of Role which have no resource associations of their own, but instead
    grant access to the combined resources associated with a set of child roles.
    Each user can be a member of one Role or composite role.
    """

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.Roles/Create',
            roles__pb2.RoleCreateRequest.SerializeToString,
            roles__pb2.RoleCreateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.Roles/Get',
            roles__pb2.RoleGetRequest.SerializeToString,
            roles__pb2.RoleGetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.Roles/Update',
            roles__pb2.RoleUpdateRequest.SerializeToString,
            roles__pb2.RoleUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.Roles/Delete',
            roles__pb2.RoleDeleteRequest.SerializeToString,
            roles__pb2.RoleDeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.Roles/List',
            roles__pb2.RoleListRequest.SerializeToString,
            roles__pb2.RoleListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
