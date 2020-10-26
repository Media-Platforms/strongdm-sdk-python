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
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: role_grants.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='role_grants.proto',
  package='v1',
  syntax='proto3',
  serialized_options=b'\n\034com.strongdm.api.v1.plumbingB\022RoleGrantsPlumbingZ2github.com/strongdm/strongdm-sdk-go/internal/v1;v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11role_grants.proto\x12\x02v1\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\roptions.proto\x1a\nspec.proto\"p\n\x16RoleGrantCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12-\n\nrole_grant\x18\x02 \x01(\x0b\x32\r.v1.RoleGrantB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xc1\x01\n\x17RoleGrantCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12-\n\nrole_grant\x18\x02 \x01(\x0b\x32\r.v1.RoleGrantB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"S\n\x13RoleGrantGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xbb\x01\n\x14RoleGrantGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12-\n\nrole_grant\x18\x02 \x01(\x0b\x32\r.v1.RoleGrantB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"Y\n\x16RoleGrantDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x92\x01\n\x17RoleGrantDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"Y\n\x14RoleGrantListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xa6\x01\n\x15RoleGrantListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12.\n\x0brole_grants\x18\x02 \x03(\x0b\x32\r.v1.RoleGrantB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xf5\x02\n\tRoleGrant\x12\x30\n\x02id\x18\x01 \x01(\tB$\xf2\xf8\xb3\x07\x1f\xa2\xf3\xb3\x07\x02ID\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x0eRolePermission\x12\x44\n\x0bresource_id\x18\x02 \x01(\tB/\xf2\xf8\xb3\x07*\xa2\xf3\xb3\x07\x0c\x44\x61tasourceID\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\nDatasource\x12\x34\n\x07role_id\x18\x03 \x01(\tB#\xf2\xf8\xb3\x07\x1e\xa2\xf3\xb3\x07\x06RoleID\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x04Role:\xb9\x01\xfa\xf8\xb3\x07p\xa2\xf3\xb3\x07\x0eRolePermission\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07S\xa2\xf3\xb3\x07#tf_examples/role_grant_resource.txt\xaa\xf3\xb3\x07&tf_examples/role_grant_data_source.txt\x92\x41\x41\x32?\x12={ \"id\": \"rg-244\", \"resource_id\": \"rs-111\", \"role_id\":\"r-444\"}2\xf2\x03\n\nRoleGrants\x12\xbf\x01\n\x06\x43reate\x12\x1a.v1.RoleGrantCreateRequest\x1a\x1b.v1.RoleGrantCreateResponse\"|\x82\xd3\xe4\x93\x02\x14\"\x0f/v1/role_grants:\x01*\x92\x41_\"]\n\x1dLearn how to make a RoleGrant\x12<https://www.strongdm.com/docs/api/services/RoleGrants#Create\x12V\n\x03Get\x12\x17.v1.RoleGrantGetRequest\x1a\x18.v1.RoleGrantGetResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/role_grants/{id}\x12_\n\x06\x44\x65lete\x12\x1a.v1.RoleGrantDeleteRequest\x1a\x1b.v1.RoleGrantDeleteResponse\"\x1c\x82\xd3\xe4\x93\x02\x16*\x14/v1/role_grants/{id}\x12T\n\x04List\x12\x18.v1.RoleGrantListRequest\x1a\x19.v1.RoleGrantListResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/role_grants\x1a\x13\xca\xf9\xb3\x07\x0e\xc2\xf9\xb3\x07\tRoleGrantBf\n\x1c\x63om.strongdm.api.v1.plumbingB\x12RoleGrantsPlumbingZ2github.com/strongdm/strongdm-sdk-go/internal/v1;v1b\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,])




_ROLEGRANTCREATEREQUEST = _descriptor.Descriptor(
  name='RoleGrantCreateRequest',
  full_name='v1.RoleGrantCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGrantCreateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_grant', full_name='v1.RoleGrantCreateRequest.role_grant', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=240,
)


_ROLEGRANTCREATERESPONSE = _descriptor.Descriptor(
  name='RoleGrantCreateResponse',
  full_name='v1.RoleGrantCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGrantCreateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_grant', full_name='v1.RoleGrantCreateResponse.role_grant', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleGrantCreateResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=436,
)


_ROLEGRANTGETREQUEST = _descriptor.Descriptor(
  name='RoleGrantGetRequest',
  full_name='v1.RoleGrantGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGrantGetRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleGrantGetRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=521,
)


_ROLEGRANTGETRESPONSE = _descriptor.Descriptor(
  name='RoleGrantGetResponse',
  full_name='v1.RoleGrantGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGrantGetResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_grant', full_name='v1.RoleGrantGetResponse.role_grant', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleGrantGetResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=524,
  serialized_end=711,
)


_ROLEGRANTDELETEREQUEST = _descriptor.Descriptor(
  name='RoleGrantDeleteRequest',
  full_name='v1.RoleGrantDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGrantDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleGrantDeleteRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=713,
  serialized_end=802,
)


_ROLEGRANTDELETERESPONSE = _descriptor.Descriptor(
  name='RoleGrantDeleteResponse',
  full_name='v1.RoleGrantDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGrantDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleGrantDeleteResponse.rate_limit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=805,
  serialized_end=951,
)


_ROLEGRANTLISTREQUEST = _descriptor.Descriptor(
  name='RoleGrantListRequest',
  full_name='v1.RoleGrantListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGrantListRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='v1.RoleGrantListRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=953,
  serialized_end=1042,
)


_ROLEGRANTLISTRESPONSE = _descriptor.Descriptor(
  name='RoleGrantListResponse',
  full_name='v1.RoleGrantListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleGrantListResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_grants', full_name='v1.RoleGrantListResponse.role_grants', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\270\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleGrantListResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1045,
  serialized_end=1211,
)


_ROLEGRANT = _descriptor.Descriptor(
  name='RoleGrant',
  full_name='v1.RoleGrant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleGrant.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\037\242\363\263\007\002ID\260\363\263\007\001\312\363\263\007\016RolePermission', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='v1.RoleGrant.resource_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007*\242\363\263\007\014DatasourceID\260\363\263\007\001\300\363\263\007\001\312\363\263\007\nDatasource', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='v1.RoleGrant.role_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\036\242\363\263\007\006RoleID\260\363\263\007\001\300\363\263\007\001\312\363\263\007\004Role', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\372\370\263\007p\242\363\263\007\016RolePermission\250\363\263\007\001\302\363\263\007S\242\363\263\007#tf_examples/role_grant_resource.txt\252\363\263\007&tf_examples/role_grant_data_source.txt\222AA2?\022={ \"id\": \"rg-244\", \"resource_id\": \"rs-111\", \"role_id\":\"r-444\"}',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1214,
  serialized_end=1587,
)

_ROLEGRANTCREATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._CREATEREQUESTMETADATA
_ROLEGRANTCREATEREQUEST.fields_by_name['role_grant'].message_type = _ROLEGRANT
_ROLEGRANTCREATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._CREATERESPONSEMETADATA
_ROLEGRANTCREATERESPONSE.fields_by_name['role_grant'].message_type = _ROLEGRANT
_ROLEGRANTCREATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLEGRANTGETREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_ROLEGRANTGETRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_ROLEGRANTGETRESPONSE.fields_by_name['role_grant'].message_type = _ROLEGRANT
_ROLEGRANTGETRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLEGRANTDELETEREQUEST.fields_by_name['meta'].message_type = spec__pb2._DELETEREQUESTMETADATA
_ROLEGRANTDELETERESPONSE.fields_by_name['meta'].message_type = spec__pb2._DELETERESPONSEMETADATA
_ROLEGRANTDELETERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLEGRANTLISTREQUEST.fields_by_name['meta'].message_type = spec__pb2._LISTREQUESTMETADATA
_ROLEGRANTLISTRESPONSE.fields_by_name['meta'].message_type = spec__pb2._LISTRESPONSEMETADATA
_ROLEGRANTLISTRESPONSE.fields_by_name['role_grants'].message_type = _ROLEGRANT
_ROLEGRANTLISTRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
DESCRIPTOR.message_types_by_name['RoleGrantCreateRequest'] = _ROLEGRANTCREATEREQUEST
DESCRIPTOR.message_types_by_name['RoleGrantCreateResponse'] = _ROLEGRANTCREATERESPONSE
DESCRIPTOR.message_types_by_name['RoleGrantGetRequest'] = _ROLEGRANTGETREQUEST
DESCRIPTOR.message_types_by_name['RoleGrantGetResponse'] = _ROLEGRANTGETRESPONSE
DESCRIPTOR.message_types_by_name['RoleGrantDeleteRequest'] = _ROLEGRANTDELETEREQUEST
DESCRIPTOR.message_types_by_name['RoleGrantDeleteResponse'] = _ROLEGRANTDELETERESPONSE
DESCRIPTOR.message_types_by_name['RoleGrantListRequest'] = _ROLEGRANTLISTREQUEST
DESCRIPTOR.message_types_by_name['RoleGrantListResponse'] = _ROLEGRANTLISTRESPONSE
DESCRIPTOR.message_types_by_name['RoleGrant'] = _ROLEGRANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleGrantCreateRequest = _reflection.GeneratedProtocolMessageType('RoleGrantCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGRANTCREATEREQUEST,
  '__module__' : 'role_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGrantCreateRequest)
  })
_sym_db.RegisterMessage(RoleGrantCreateRequest)

RoleGrantCreateResponse = _reflection.GeneratedProtocolMessageType('RoleGrantCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGRANTCREATERESPONSE,
  '__module__' : 'role_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGrantCreateResponse)
  })
_sym_db.RegisterMessage(RoleGrantCreateResponse)

RoleGrantGetRequest = _reflection.GeneratedProtocolMessageType('RoleGrantGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGRANTGETREQUEST,
  '__module__' : 'role_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGrantGetRequest)
  })
_sym_db.RegisterMessage(RoleGrantGetRequest)

RoleGrantGetResponse = _reflection.GeneratedProtocolMessageType('RoleGrantGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGRANTGETRESPONSE,
  '__module__' : 'role_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGrantGetResponse)
  })
_sym_db.RegisterMessage(RoleGrantGetResponse)

RoleGrantDeleteRequest = _reflection.GeneratedProtocolMessageType('RoleGrantDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGRANTDELETEREQUEST,
  '__module__' : 'role_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGrantDeleteRequest)
  })
_sym_db.RegisterMessage(RoleGrantDeleteRequest)

RoleGrantDeleteResponse = _reflection.GeneratedProtocolMessageType('RoleGrantDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGRANTDELETERESPONSE,
  '__module__' : 'role_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGrantDeleteResponse)
  })
_sym_db.RegisterMessage(RoleGrantDeleteResponse)

RoleGrantListRequest = _reflection.GeneratedProtocolMessageType('RoleGrantListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGRANTLISTREQUEST,
  '__module__' : 'role_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGrantListRequest)
  })
_sym_db.RegisterMessage(RoleGrantListRequest)

RoleGrantListResponse = _reflection.GeneratedProtocolMessageType('RoleGrantListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGRANTLISTRESPONSE,
  '__module__' : 'role_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGrantListResponse)
  })
_sym_db.RegisterMessage(RoleGrantListResponse)

RoleGrant = _reflection.GeneratedProtocolMessageType('RoleGrant', (_message.Message,), {
  'DESCRIPTOR' : _ROLEGRANT,
  '__module__' : 'role_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleGrant)
  })
_sym_db.RegisterMessage(RoleGrant)


DESCRIPTOR._options = None
_ROLEGRANTCREATEREQUEST.fields_by_name['role_grant']._options = None
_ROLEGRANTCREATERESPONSE.fields_by_name['meta']._options = None
_ROLEGRANTCREATERESPONSE.fields_by_name['role_grant']._options = None
_ROLEGRANTCREATERESPONSE.fields_by_name['rate_limit']._options = None
_ROLEGRANTCREATERESPONSE._options = None
_ROLEGRANTGETREQUEST.fields_by_name['id']._options = None
_ROLEGRANTGETRESPONSE.fields_by_name['meta']._options = None
_ROLEGRANTGETRESPONSE.fields_by_name['role_grant']._options = None
_ROLEGRANTGETRESPONSE.fields_by_name['rate_limit']._options = None
_ROLEGRANTGETRESPONSE._options = None
_ROLEGRANTDELETEREQUEST.fields_by_name['id']._options = None
_ROLEGRANTDELETERESPONSE.fields_by_name['meta']._options = None
_ROLEGRANTDELETERESPONSE.fields_by_name['rate_limit']._options = None
_ROLEGRANTDELETERESPONSE._options = None
_ROLEGRANTLISTREQUEST.fields_by_name['filter']._options = None
_ROLEGRANTLISTRESPONSE.fields_by_name['role_grants']._options = None
_ROLEGRANTLISTRESPONSE.fields_by_name['rate_limit']._options = None
_ROLEGRANT.fields_by_name['id']._options = None
_ROLEGRANT.fields_by_name['resource_id']._options = None
_ROLEGRANT.fields_by_name['role_id']._options = None
_ROLEGRANT._options = None

_ROLEGRANTS = _descriptor.ServiceDescriptor(
  name='RoleGrants',
  full_name='v1.RoleGrants',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312\371\263\007\016\302\371\263\007\tRoleGrant',
  create_key=_descriptor._internal_create_key,
  serialized_start=1590,
  serialized_end=2088,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='v1.RoleGrants.Create',
    index=0,
    containing_service=None,
    input_type=_ROLEGRANTCREATEREQUEST,
    output_type=_ROLEGRANTCREATERESPONSE,
    serialized_options=b'\202\323\344\223\002\024\"\017/v1/role_grants:\001*\222A_\"]\n\035Learn how to make a RoleGrant\022<https://www.strongdm.com/docs/api/services/RoleGrants#Create',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='v1.RoleGrants.Get',
    index=1,
    containing_service=None,
    input_type=_ROLEGRANTGETREQUEST,
    output_type=_ROLEGRANTGETRESPONSE,
    serialized_options=b'\202\323\344\223\002\026\022\024/v1/role_grants/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='v1.RoleGrants.Delete',
    index=2,
    containing_service=None,
    input_type=_ROLEGRANTDELETEREQUEST,
    output_type=_ROLEGRANTDELETERESPONSE,
    serialized_options=b'\202\323\344\223\002\026*\024/v1/role_grants/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='v1.RoleGrants.List',
    index=3,
    containing_service=None,
    input_type=_ROLEGRANTLISTREQUEST,
    output_type=_ROLEGRANTLISTRESPONSE,
    serialized_options=b'\202\323\344\223\002\021\022\017/v1/role_grants',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROLEGRANTS)

DESCRIPTOR.services_by_name['RoleGrants'] = _ROLEGRANTS

# @@protoc_insertion_point(module_scope)
