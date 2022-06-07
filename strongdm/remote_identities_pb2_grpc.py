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

from . import remote_identities_pb2 as remote__identities__pb2


class RemoteIdentitiesStub(object):
    """RemoteIdentities assign a resource directly to an account, giving the account the permission to connect to that resource.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Create = channel.unary_unary(
                '/v1.RemoteIdentities/Create',
                request_serializer=remote__identities__pb2.RemoteIdentityCreateRequest.SerializeToString,
                response_deserializer=remote__identities__pb2.RemoteIdentityCreateResponse.FromString,
                )
        self.Get = channel.unary_unary(
                '/v1.RemoteIdentities/Get',
                request_serializer=remote__identities__pb2.RemoteIdentityGetRequest.SerializeToString,
                response_deserializer=remote__identities__pb2.RemoteIdentityGetResponse.FromString,
                )
        self.Update = channel.unary_unary(
                '/v1.RemoteIdentities/Update',
                request_serializer=remote__identities__pb2.RemoteIdentityUpdateRequest.SerializeToString,
                response_deserializer=remote__identities__pb2.RemoteIdentityUpdateResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/v1.RemoteIdentities/Delete',
                request_serializer=remote__identities__pb2.RemoteIdentityDeleteRequest.SerializeToString,
                response_deserializer=remote__identities__pb2.RemoteIdentityDeleteResponse.FromString,
                )
        self.List = channel.unary_unary(
                '/v1.RemoteIdentities/List',
                request_serializer=remote__identities__pb2.RemoteIdentityListRequest.SerializeToString,
                response_deserializer=remote__identities__pb2.RemoteIdentityListResponse.FromString,
                )


class RemoteIdentitiesServicer(object):
    """RemoteIdentities assign a resource directly to an account, giving the account the permission to connect to that resource.
    """

    def Create(self, request, context):
        """Create registers a new RemoteIdentity.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get(self, request, context):
        """Get reads one RemoteIdentity by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update replaces all the fields of a RemoteIdentity by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete removes a RemoteIdentity by ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """List gets a list of RemoteIdentities matching a given set of criteria.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoteIdentitiesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=remote__identities__pb2.RemoteIdentityCreateRequest.FromString,
                    response_serializer=remote__identities__pb2.RemoteIdentityCreateResponse.SerializeToString,
            ),
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=remote__identities__pb2.RemoteIdentityGetRequest.FromString,
                    response_serializer=remote__identities__pb2.RemoteIdentityGetResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=remote__identities__pb2.RemoteIdentityUpdateRequest.FromString,
                    response_serializer=remote__identities__pb2.RemoteIdentityUpdateResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=remote__identities__pb2.RemoteIdentityDeleteRequest.FromString,
                    response_serializer=remote__identities__pb2.RemoteIdentityDeleteResponse.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=remote__identities__pb2.RemoteIdentityListRequest.FromString,
                    response_serializer=remote__identities__pb2.RemoteIdentityListResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.RemoteIdentities', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RemoteIdentities(object):
    """RemoteIdentities assign a resource directly to an account, giving the account the permission to connect to that resource.
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
        return grpc.experimental.unary_unary(request, target, '/v1.RemoteIdentities/Create',
            remote__identities__pb2.RemoteIdentityCreateRequest.SerializeToString,
            remote__identities__pb2.RemoteIdentityCreateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/v1.RemoteIdentities/Get',
            remote__identities__pb2.RemoteIdentityGetRequest.SerializeToString,
            remote__identities__pb2.RemoteIdentityGetResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/v1.RemoteIdentities/Update',
            remote__identities__pb2.RemoteIdentityUpdateRequest.SerializeToString,
            remote__identities__pb2.RemoteIdentityUpdateResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/v1.RemoteIdentities/Delete',
            remote__identities__pb2.RemoteIdentityDeleteRequest.SerializeToString,
            remote__identities__pb2.RemoteIdentityDeleteResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/v1.RemoteIdentities/List',
            remote__identities__pb2.RemoteIdentityListRequest.SerializeToString,
            remote__identities__pb2.RemoteIdentityListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
