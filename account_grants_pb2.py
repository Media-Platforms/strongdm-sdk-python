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
# source: account_grants.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='account_grants.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\034com.strongdm.api.v1.plumbingB\025AccountGrantsPlumbing'),
  serialized_pb=_b('\n\x14\x61\x63\x63ount_grants.proto\x12\x02v1\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\roptions.proto\x1a\nspec.proto\"y\n\x19\x41\x63\x63ountGrantCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12\x33\n\raccount_grant\x18\x02 \x01(\x0b\x32\x10.v1.AccountGrantB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xca\x01\n\x1a\x41\x63\x63ountGrantCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x33\n\raccount_grant\x18\x02 \x01(\x0b\x32\x10.v1.AccountGrantB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"V\n\x16\x41\x63\x63ountGrantGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xc4\x01\n\x17\x41\x63\x63ountGrantGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x33\n\raccount_grant\x18\x02 \x01(\x0b\x32\x10.v1.AccountGrantB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\\\n\x19\x41\x63\x63ountGrantDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x95\x01\n\x1a\x41\x63\x63ountGrantDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\\\n\x17\x41\x63\x63ountGrantListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xaf\x01\n\x18\x41\x63\x63ountGrantListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12\x34\n\x0e\x61\x63\x63ount_grants\x18\x02 \x03(\x0b\x32\x10.v1.AccountGrantB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xdf\x04\n\x0c\x41\x63\x63ountGrant\x12,\n\x02id\x18\x01 \x01(\tB \xf2\xf8\xb3\x07\x1b\xa2\xf3\xb3\x07\x02ID\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\nPermission\x12\x44\n\x0bresource_id\x18\x02 \x01(\tB/\xf2\xf8\xb3\x07*\xa2\xf3\xb3\x07\x0c\x44\x61tasourceID\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\nDatasource\x12\x37\n\naccount_id\x18\x03 \x01(\tB#\xf2\xf8\xb3\x07\x1e\xa2\xf3\xb3\x07\x06UserID\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x04User\x12H\n\nstart_from\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x18\xf2\xf8\xb3\x07\x13\xa2\xf3\xb3\x07\tStartFrom\xb0\xf3\xb3\x07\x01\x12J\n\x0bvalid_until\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x19\xf2\xf8\xb3\x07\x14\xa2\xf3\xb3\x07\nValidUntil\xb0\xf3\xb3\x07\x01:\x8b\x02\xfa\xf8\xb3\x07r\xa2\xf3\xb3\x07\nPermission\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07Y\xa2\xf3\xb3\x07&tf_examples/account_grant_resource.txt\xaa\xf3\xb3\x07)tf_examples/account_grant_data_source.txt\x92\x41\x90\x01*J\n\x0f\x41 AccountGrant.\x12\x37https://www.strongdm.com/docs/api/entities#AccountGrant2B\x12@{ \"id\": \"ug-244\", \"resource_id\": \"rs-111\", \"account_id\":\"a-444\"}2\x9f\x04\n\rAccountGrants\x12\xce\x01\n\x06\x43reate\x12\x1d.v1.AccountGrantCreateRequest\x1a\x1e.v1.AccountGrantCreateResponse\"\x84\x01\x82\xd3\xe4\x93\x02\x16\"\x11/v1/accountGrants:\x01*\x92\x41\x65\"c\n Learn how to make a AccountGrant\x12?https://www.strongdm.com/docs/api/services/AccountGrants#Create\x12^\n\x03Get\x12\x1a.v1.AccountGrantGetRequest\x1a\x1b.v1.AccountGrantGetResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/accountGrants/{id}\x12g\n\x06\x44\x65lete\x12\x1d.v1.AccountGrantDeleteRequest\x1a\x1e.v1.AccountGrantDeleteResponse\"\x1e\x82\xd3\xe4\x93\x02\x18*\x16/v1/accountGrants/{id}\x12\\\n\x04List\x12\x1b.v1.AccountGrantListRequest\x1a\x1c.v1.AccountGrantListResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/accountGrants\x1a\x16\xca\xf9\xb3\x07\x11\xc2\xf9\xb3\x07\x0c\x41\x63\x63ountGrantB5\n\x1c\x63om.strongdm.api.v1.plumbingB\x15\x41\x63\x63ountGrantsPlumbingb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,])




_ACCOUNTGRANTCREATEREQUEST = _descriptor.Descriptor(
  name='AccountGrantCreateRequest',
  full_name='v1.AccountGrantCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountGrantCreateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_grant', full_name='v1.AccountGrantCreateRequest.account_grant', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=164,
  serialized_end=285,
)


_ACCOUNTGRANTCREATERESPONSE = _descriptor.Descriptor(
  name='AccountGrantCreateResponse',
  full_name='v1.AccountGrantCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountGrantCreateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_grant', full_name='v1.AccountGrantCreateResponse.account_grant', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountGrantCreateResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\005\250\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=490,
)


_ACCOUNTGRANTGETREQUEST = _descriptor.Descriptor(
  name='AccountGrantGetRequest',
  full_name='v1.AccountGrantGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountGrantGetRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountGrantGetRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=492,
  serialized_end=578,
)


_ACCOUNTGRANTGETRESPONSE = _descriptor.Descriptor(
  name='AccountGrantGetResponse',
  full_name='v1.AccountGrantGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountGrantGetResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_grant', full_name='v1.AccountGrantGetResponse.account_grant', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountGrantGetResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\005\250\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=581,
  serialized_end=777,
)


_ACCOUNTGRANTDELETEREQUEST = _descriptor.Descriptor(
  name='AccountGrantDeleteRequest',
  full_name='v1.AccountGrantDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountGrantDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountGrantDeleteRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=779,
  serialized_end=871,
)


_ACCOUNTGRANTDELETERESPONSE = _descriptor.Descriptor(
  name='AccountGrantDeleteResponse',
  full_name='v1.AccountGrantDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountGrantDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountGrantDeleteResponse.rate_limit', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\005\250\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=874,
  serialized_end=1023,
)


_ACCOUNTGRANTLISTREQUEST = _descriptor.Descriptor(
  name='AccountGrantListRequest',
  full_name='v1.AccountGrantListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountGrantListRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='v1.AccountGrantListRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=1025,
  serialized_end=1117,
)


_ACCOUNTGRANTLISTRESPONSE = _descriptor.Descriptor(
  name='AccountGrantListResponse',
  full_name='v1.AccountGrantListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountGrantListResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_grants', full_name='v1.AccountGrantListResponse.account_grants', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\270\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountGrantListResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
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
  serialized_start=1120,
  serialized_end=1295,
)


_ACCOUNTGRANT = _descriptor.Descriptor(
  name='AccountGrant',
  full_name='v1.AccountGrant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountGrant.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\033\242\363\263\007\002ID\260\363\263\007\001\312\363\263\007\nPermission'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='v1.AccountGrant.resource_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007*\242\363\263\007\014DatasourceID\260\363\263\007\001\300\363\263\007\001\312\363\263\007\nDatasource'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='v1.AccountGrant.account_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\036\242\363\263\007\006UserID\260\363\263\007\001\300\363\263\007\001\312\363\263\007\004User'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_from', full_name='v1.AccountGrant.start_from', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\023\242\363\263\007\tStartFrom\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid_until', full_name='v1.AccountGrant.valid_until', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\024\242\363\263\007\nValidUntil\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007r\242\363\263\007\nPermission\250\363\263\007\001\302\363\263\007Y\242\363\263\007&tf_examples/account_grant_resource.txt\252\363\263\007)tf_examples/account_grant_data_source.txt\222A\220\001*J\n\017A AccountGrant.\0227https://www.strongdm.com/docs/api/entities#AccountGrant2B\022@{ \"id\": \"ug-244\", \"resource_id\": \"rs-111\", \"account_id\":\"a-444\"}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1298,
  serialized_end=1905,
)

_ACCOUNTGRANTCREATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._CREATEREQUESTMETADATA
_ACCOUNTGRANTCREATEREQUEST.fields_by_name['account_grant'].message_type = _ACCOUNTGRANT
_ACCOUNTGRANTCREATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._CREATERESPONSEMETADATA
_ACCOUNTGRANTCREATERESPONSE.fields_by_name['account_grant'].message_type = _ACCOUNTGRANT
_ACCOUNTGRANTCREATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTGRANTGETREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_ACCOUNTGRANTGETRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_ACCOUNTGRANTGETRESPONSE.fields_by_name['account_grant'].message_type = _ACCOUNTGRANT
_ACCOUNTGRANTGETRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTGRANTDELETEREQUEST.fields_by_name['meta'].message_type = spec__pb2._DELETEREQUESTMETADATA
_ACCOUNTGRANTDELETERESPONSE.fields_by_name['meta'].message_type = spec__pb2._DELETERESPONSEMETADATA
_ACCOUNTGRANTDELETERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTGRANTLISTREQUEST.fields_by_name['meta'].message_type = spec__pb2._LISTREQUESTMETADATA
_ACCOUNTGRANTLISTRESPONSE.fields_by_name['meta'].message_type = spec__pb2._LISTRESPONSEMETADATA
_ACCOUNTGRANTLISTRESPONSE.fields_by_name['account_grants'].message_type = _ACCOUNTGRANT
_ACCOUNTGRANTLISTRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTGRANT.fields_by_name['start_from'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ACCOUNTGRANT.fields_by_name['valid_until'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['AccountGrantCreateRequest'] = _ACCOUNTGRANTCREATEREQUEST
DESCRIPTOR.message_types_by_name['AccountGrantCreateResponse'] = _ACCOUNTGRANTCREATERESPONSE
DESCRIPTOR.message_types_by_name['AccountGrantGetRequest'] = _ACCOUNTGRANTGETREQUEST
DESCRIPTOR.message_types_by_name['AccountGrantGetResponse'] = _ACCOUNTGRANTGETRESPONSE
DESCRIPTOR.message_types_by_name['AccountGrantDeleteRequest'] = _ACCOUNTGRANTDELETEREQUEST
DESCRIPTOR.message_types_by_name['AccountGrantDeleteResponse'] = _ACCOUNTGRANTDELETERESPONSE
DESCRIPTOR.message_types_by_name['AccountGrantListRequest'] = _ACCOUNTGRANTLISTREQUEST
DESCRIPTOR.message_types_by_name['AccountGrantListResponse'] = _ACCOUNTGRANTLISTRESPONSE
DESCRIPTOR.message_types_by_name['AccountGrant'] = _ACCOUNTGRANT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountGrantCreateRequest = _reflection.GeneratedProtocolMessageType('AccountGrantCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTCREATEREQUEST,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantCreateRequest)
  })
_sym_db.RegisterMessage(AccountGrantCreateRequest)

AccountGrantCreateResponse = _reflection.GeneratedProtocolMessageType('AccountGrantCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTCREATERESPONSE,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantCreateResponse)
  })
_sym_db.RegisterMessage(AccountGrantCreateResponse)

AccountGrantGetRequest = _reflection.GeneratedProtocolMessageType('AccountGrantGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTGETREQUEST,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantGetRequest)
  })
_sym_db.RegisterMessage(AccountGrantGetRequest)

AccountGrantGetResponse = _reflection.GeneratedProtocolMessageType('AccountGrantGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTGETRESPONSE,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantGetResponse)
  })
_sym_db.RegisterMessage(AccountGrantGetResponse)

AccountGrantDeleteRequest = _reflection.GeneratedProtocolMessageType('AccountGrantDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTDELETEREQUEST,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantDeleteRequest)
  })
_sym_db.RegisterMessage(AccountGrantDeleteRequest)

AccountGrantDeleteResponse = _reflection.GeneratedProtocolMessageType('AccountGrantDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTDELETERESPONSE,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantDeleteResponse)
  })
_sym_db.RegisterMessage(AccountGrantDeleteResponse)

AccountGrantListRequest = _reflection.GeneratedProtocolMessageType('AccountGrantListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTLISTREQUEST,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantListRequest)
  })
_sym_db.RegisterMessage(AccountGrantListRequest)

AccountGrantListResponse = _reflection.GeneratedProtocolMessageType('AccountGrantListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANTLISTRESPONSE,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrantListResponse)
  })
_sym_db.RegisterMessage(AccountGrantListResponse)

AccountGrant = _reflection.GeneratedProtocolMessageType('AccountGrant', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTGRANT,
  '__module__' : 'account_grants_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountGrant)
  })
_sym_db.RegisterMessage(AccountGrant)


DESCRIPTOR._options = None
_ACCOUNTGRANTCREATEREQUEST.fields_by_name['account_grant']._options = None
_ACCOUNTGRANTCREATERESPONSE.fields_by_name['meta']._options = None
_ACCOUNTGRANTCREATERESPONSE.fields_by_name['account_grant']._options = None
_ACCOUNTGRANTCREATERESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTGRANTCREATERESPONSE._options = None
_ACCOUNTGRANTGETREQUEST.fields_by_name['id']._options = None
_ACCOUNTGRANTGETRESPONSE.fields_by_name['meta']._options = None
_ACCOUNTGRANTGETRESPONSE.fields_by_name['account_grant']._options = None
_ACCOUNTGRANTGETRESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTGRANTGETRESPONSE._options = None
_ACCOUNTGRANTDELETEREQUEST.fields_by_name['id']._options = None
_ACCOUNTGRANTDELETERESPONSE.fields_by_name['meta']._options = None
_ACCOUNTGRANTDELETERESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTGRANTDELETERESPONSE._options = None
_ACCOUNTGRANTLISTREQUEST.fields_by_name['filter']._options = None
_ACCOUNTGRANTLISTRESPONSE.fields_by_name['account_grants']._options = None
_ACCOUNTGRANTLISTRESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTGRANT.fields_by_name['id']._options = None
_ACCOUNTGRANT.fields_by_name['resource_id']._options = None
_ACCOUNTGRANT.fields_by_name['account_id']._options = None
_ACCOUNTGRANT.fields_by_name['start_from']._options = None
_ACCOUNTGRANT.fields_by_name['valid_until']._options = None
_ACCOUNTGRANT._options = None

_ACCOUNTGRANTS = _descriptor.ServiceDescriptor(
  name='AccountGrants',
  full_name='v1.AccountGrants',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312\371\263\007\021\302\371\263\007\014AccountGrant'),
  serialized_start=1908,
  serialized_end=2451,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='v1.AccountGrants.Create',
    index=0,
    containing_service=None,
    input_type=_ACCOUNTGRANTCREATEREQUEST,
    output_type=_ACCOUNTGRANTCREATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\026\"\021/v1/accountGrants:\001*\222Ae\"c\n Learn how to make a AccountGrant\022?https://www.strongdm.com/docs/api/services/AccountGrants#Create'),
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='v1.AccountGrants.Get',
    index=1,
    containing_service=None,
    input_type=_ACCOUNTGRANTGETREQUEST,
    output_type=_ACCOUNTGRANTGETRESPONSE,
    serialized_options=_b('\202\323\344\223\002\030\022\026/v1/accountGrants/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='v1.AccountGrants.Delete',
    index=2,
    containing_service=None,
    input_type=_ACCOUNTGRANTDELETEREQUEST,
    output_type=_ACCOUNTGRANTDELETERESPONSE,
    serialized_options=_b('\202\323\344\223\002\030*\026/v1/accountGrants/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='v1.AccountGrants.List',
    index=3,
    containing_service=None,
    input_type=_ACCOUNTGRANTLISTREQUEST,
    output_type=_ACCOUNTGRANTLISTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\023\022\021/v1/accountGrants'),
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTGRANTS)

DESCRIPTOR.services_by_name['AccountGrants'] = _ACCOUNTGRANTS

# @@protoc_insertion_point(module_scope)
