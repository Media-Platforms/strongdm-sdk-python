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
# source: resources.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2
from . import drivers_pb2 as drivers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='resources.proto',
  package='v1',
  syntax='proto3',
  serialized_options=b'\n\034com.strongdm.api.v1.plumbingB\021ResourcesPlumbing',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fresources.proto\x12\x02v1\x1a\x1cgoogle/api/annotations.proto\x1a\roptions.proto\x1a\nspec.proto\x1a\rdrivers.proto\"l\n\x15ResourceCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12*\n\x08resource\x18\x02 \x01(\x0b\x32\x0c.v1.ResourceB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xbd\x01\n\x16ResourceCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12*\n\x08resource\x18\x02 \x01(\x0b\x32\x0c.v1.ResourceB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x04 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"R\n\x12ResourceGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xb7\x01\n\x13ResourceGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12*\n\x08resource\x18\x02 \x01(\x0b\x32\x0c.v1.ResourceB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"x\n\x15ResourceUpdateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\x12*\n\x08resource\x18\x03 \x01(\x0b\x32\x0c.v1.ResourceB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xbd\x01\n\x16ResourceUpdateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12*\n\x08resource\x18\x02 \x01(\x0b\x32\x0c.v1.ResourceB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"X\n\x15ResourceDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x91\x01\n\x16ResourceDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"X\n\x13ResourceListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xa2\x01\n\x14ResourceListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12+\n\tresources\x18\x02 \x03(\x0b\x32\x0c.v1.ResourceB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x32\xdd\x03\n\tResources\x12Y\n\x06\x43reate\x12\x19.v1.ResourceCreateRequest\x1a\x1a.v1.ResourceCreateResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/v1/resources:\x01*\x12R\n\x03Get\x12\x16.v1.ResourceGetRequest\x1a\x17.v1.ResourceGetResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/resources/{id}\x12^\n\x06Update\x12\x19.v1.ResourceUpdateRequest\x1a\x1a.v1.ResourceUpdateResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x1a\x12/v1/resources/{id}:\x01*\x12[\n\x06\x44\x65lete\x12\x19.v1.ResourceDeleteRequest\x1a\x1a.v1.ResourceDeleteResponse\"\x1a\x82\xd3\xe4\x93\x02\x14*\x12/v1/resources/{id}\x12P\n\x04List\x12\x17.v1.ResourceListRequest\x1a\x18.v1.ResourceListResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/v1/resources\x1a\x12\xca\xf9\xb3\x07\r\xc2\xf9\xb3\x07\x08ResourceB1\n\x1c\x63om.strongdm.api.v1.plumbingB\x11ResourcesPlumbingb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,drivers__pb2.DESCRIPTOR,])




_RESOURCECREATEREQUEST = _descriptor.Descriptor(
  name='ResourceCreateRequest',
  full_name='v1.ResourceCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ResourceCreateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='v1.ResourceCreateRequest.resource', index=1,
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
  serialized_start=95,
  serialized_end=203,
)


_RESOURCECREATERESPONSE = _descriptor.Descriptor(
  name='ResourceCreateResponse',
  full_name='v1.ResourceCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ResourceCreateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='v1.ResourceCreateResponse.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.ResourceCreateResponse.rate_limit', index=2,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=206,
  serialized_end=395,
)


_RESOURCEGETREQUEST = _descriptor.Descriptor(
  name='ResourceGetRequest',
  full_name='v1.ResourceGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ResourceGetRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.ResourceGetRequest.id', index=1,
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
  serialized_start=397,
  serialized_end=479,
)


_RESOURCEGETRESPONSE = _descriptor.Descriptor(
  name='ResourceGetResponse',
  full_name='v1.ResourceGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ResourceGetResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='v1.ResourceGetResponse.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.ResourceGetResponse.rate_limit', index=2,
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
  serialized_start=482,
  serialized_end=665,
)


_RESOURCEUPDATEREQUEST = _descriptor.Descriptor(
  name='ResourceUpdateRequest',
  full_name='v1.ResourceUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ResourceUpdateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.ResourceUpdateRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='v1.ResourceUpdateRequest.resource', index=2,
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
  serialized_start=667,
  serialized_end=787,
)


_RESOURCEUPDATERESPONSE = _descriptor.Descriptor(
  name='ResourceUpdateResponse',
  full_name='v1.ResourceUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ResourceUpdateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resource', full_name='v1.ResourceUpdateResponse.resource', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.ResourceUpdateResponse.rate_limit', index=2,
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
  serialized_start=790,
  serialized_end=979,
)


_RESOURCEDELETEREQUEST = _descriptor.Descriptor(
  name='ResourceDeleteRequest',
  full_name='v1.ResourceDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ResourceDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.ResourceDeleteRequest.id', index=1,
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
  serialized_start=981,
  serialized_end=1069,
)


_RESOURCEDELETERESPONSE = _descriptor.Descriptor(
  name='ResourceDeleteResponse',
  full_name='v1.ResourceDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ResourceDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.ResourceDeleteResponse.rate_limit', index=1,
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
  serialized_start=1072,
  serialized_end=1217,
)


_RESOURCELISTREQUEST = _descriptor.Descriptor(
  name='ResourceListRequest',
  full_name='v1.ResourceListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ResourceListRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='v1.ResourceListRequest.filter', index=1,
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
  serialized_start=1219,
  serialized_end=1307,
)


_RESOURCELISTRESPONSE = _descriptor.Descriptor(
  name='ResourceListResponse',
  full_name='v1.ResourceListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ResourceListResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resources', full_name='v1.ResourceListResponse.resources', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\270\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.ResourceListResponse.rate_limit', index=2,
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
  serialized_start=1310,
  serialized_end=1472,
)

_RESOURCECREATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._CREATEREQUESTMETADATA
_RESOURCECREATEREQUEST.fields_by_name['resource'].message_type = drivers__pb2._RESOURCE
_RESOURCECREATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._CREATERESPONSEMETADATA
_RESOURCECREATERESPONSE.fields_by_name['resource'].message_type = drivers__pb2._RESOURCE
_RESOURCECREATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_RESOURCEGETREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_RESOURCEGETRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_RESOURCEGETRESPONSE.fields_by_name['resource'].message_type = drivers__pb2._RESOURCE
_RESOURCEGETRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_RESOURCEUPDATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._UPDATEREQUESTMETADATA
_RESOURCEUPDATEREQUEST.fields_by_name['resource'].message_type = drivers__pb2._RESOURCE
_RESOURCEUPDATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._UPDATERESPONSEMETADATA
_RESOURCEUPDATERESPONSE.fields_by_name['resource'].message_type = drivers__pb2._RESOURCE
_RESOURCEUPDATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_RESOURCEDELETEREQUEST.fields_by_name['meta'].message_type = spec__pb2._DELETEREQUESTMETADATA
_RESOURCEDELETERESPONSE.fields_by_name['meta'].message_type = spec__pb2._DELETERESPONSEMETADATA
_RESOURCEDELETERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_RESOURCELISTREQUEST.fields_by_name['meta'].message_type = spec__pb2._LISTREQUESTMETADATA
_RESOURCELISTRESPONSE.fields_by_name['meta'].message_type = spec__pb2._LISTRESPONSEMETADATA
_RESOURCELISTRESPONSE.fields_by_name['resources'].message_type = drivers__pb2._RESOURCE
_RESOURCELISTRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
DESCRIPTOR.message_types_by_name['ResourceCreateRequest'] = _RESOURCECREATEREQUEST
DESCRIPTOR.message_types_by_name['ResourceCreateResponse'] = _RESOURCECREATERESPONSE
DESCRIPTOR.message_types_by_name['ResourceGetRequest'] = _RESOURCEGETREQUEST
DESCRIPTOR.message_types_by_name['ResourceGetResponse'] = _RESOURCEGETRESPONSE
DESCRIPTOR.message_types_by_name['ResourceUpdateRequest'] = _RESOURCEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['ResourceUpdateResponse'] = _RESOURCEUPDATERESPONSE
DESCRIPTOR.message_types_by_name['ResourceDeleteRequest'] = _RESOURCEDELETEREQUEST
DESCRIPTOR.message_types_by_name['ResourceDeleteResponse'] = _RESOURCEDELETERESPONSE
DESCRIPTOR.message_types_by_name['ResourceListRequest'] = _RESOURCELISTREQUEST
DESCRIPTOR.message_types_by_name['ResourceListResponse'] = _RESOURCELISTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResourceCreateRequest = _reflection.GeneratedProtocolMessageType('ResourceCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCECREATEREQUEST,
  '__module__' : 'resources_pb2'
  # @@protoc_insertion_point(class_scope:v1.ResourceCreateRequest)
  })
_sym_db.RegisterMessage(ResourceCreateRequest)

ResourceCreateResponse = _reflection.GeneratedProtocolMessageType('ResourceCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCECREATERESPONSE,
  '__module__' : 'resources_pb2'
  # @@protoc_insertion_point(class_scope:v1.ResourceCreateResponse)
  })
_sym_db.RegisterMessage(ResourceCreateResponse)

ResourceGetRequest = _reflection.GeneratedProtocolMessageType('ResourceGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEGETREQUEST,
  '__module__' : 'resources_pb2'
  # @@protoc_insertion_point(class_scope:v1.ResourceGetRequest)
  })
_sym_db.RegisterMessage(ResourceGetRequest)

ResourceGetResponse = _reflection.GeneratedProtocolMessageType('ResourceGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEGETRESPONSE,
  '__module__' : 'resources_pb2'
  # @@protoc_insertion_point(class_scope:v1.ResourceGetResponse)
  })
_sym_db.RegisterMessage(ResourceGetResponse)

ResourceUpdateRequest = _reflection.GeneratedProtocolMessageType('ResourceUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEUPDATEREQUEST,
  '__module__' : 'resources_pb2'
  # @@protoc_insertion_point(class_scope:v1.ResourceUpdateRequest)
  })
_sym_db.RegisterMessage(ResourceUpdateRequest)

ResourceUpdateResponse = _reflection.GeneratedProtocolMessageType('ResourceUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEUPDATERESPONSE,
  '__module__' : 'resources_pb2'
  # @@protoc_insertion_point(class_scope:v1.ResourceUpdateResponse)
  })
_sym_db.RegisterMessage(ResourceUpdateResponse)

ResourceDeleteRequest = _reflection.GeneratedProtocolMessageType('ResourceDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEDELETEREQUEST,
  '__module__' : 'resources_pb2'
  # @@protoc_insertion_point(class_scope:v1.ResourceDeleteRequest)
  })
_sym_db.RegisterMessage(ResourceDeleteRequest)

ResourceDeleteResponse = _reflection.GeneratedProtocolMessageType('ResourceDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCEDELETERESPONSE,
  '__module__' : 'resources_pb2'
  # @@protoc_insertion_point(class_scope:v1.ResourceDeleteResponse)
  })
_sym_db.RegisterMessage(ResourceDeleteResponse)

ResourceListRequest = _reflection.GeneratedProtocolMessageType('ResourceListRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCELISTREQUEST,
  '__module__' : 'resources_pb2'
  # @@protoc_insertion_point(class_scope:v1.ResourceListRequest)
  })
_sym_db.RegisterMessage(ResourceListRequest)

ResourceListResponse = _reflection.GeneratedProtocolMessageType('ResourceListResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESOURCELISTRESPONSE,
  '__module__' : 'resources_pb2'
  # @@protoc_insertion_point(class_scope:v1.ResourceListResponse)
  })
_sym_db.RegisterMessage(ResourceListResponse)


DESCRIPTOR._options = None
_RESOURCECREATEREQUEST.fields_by_name['resource']._options = None
_RESOURCECREATERESPONSE.fields_by_name['meta']._options = None
_RESOURCECREATERESPONSE.fields_by_name['resource']._options = None
_RESOURCECREATERESPONSE.fields_by_name['rate_limit']._options = None
_RESOURCECREATERESPONSE._options = None
_RESOURCEGETREQUEST.fields_by_name['id']._options = None
_RESOURCEGETRESPONSE.fields_by_name['meta']._options = None
_RESOURCEGETRESPONSE.fields_by_name['resource']._options = None
_RESOURCEGETRESPONSE.fields_by_name['rate_limit']._options = None
_RESOURCEGETRESPONSE._options = None
_RESOURCEUPDATEREQUEST.fields_by_name['resource']._options = None
_RESOURCEUPDATERESPONSE.fields_by_name['meta']._options = None
_RESOURCEUPDATERESPONSE.fields_by_name['resource']._options = None
_RESOURCEUPDATERESPONSE.fields_by_name['rate_limit']._options = None
_RESOURCEUPDATERESPONSE._options = None
_RESOURCEDELETEREQUEST.fields_by_name['id']._options = None
_RESOURCEDELETERESPONSE.fields_by_name['meta']._options = None
_RESOURCEDELETERESPONSE.fields_by_name['rate_limit']._options = None
_RESOURCEDELETERESPONSE._options = None
_RESOURCELISTREQUEST.fields_by_name['filter']._options = None
_RESOURCELISTRESPONSE.fields_by_name['resources']._options = None
_RESOURCELISTRESPONSE.fields_by_name['rate_limit']._options = None

_RESOURCES = _descriptor.ServiceDescriptor(
  name='Resources',
  full_name='v1.Resources',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\312\371\263\007\r\302\371\263\007\010Resource',
  create_key=_descriptor._internal_create_key,
  serialized_start=1475,
  serialized_end=1952,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='v1.Resources.Create',
    index=0,
    containing_service=None,
    input_type=_RESOURCECREATEREQUEST,
    output_type=_RESOURCECREATERESPONSE,
    serialized_options=b'\202\323\344\223\002\022\"\r/v1/resources:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='v1.Resources.Get',
    index=1,
    containing_service=None,
    input_type=_RESOURCEGETREQUEST,
    output_type=_RESOURCEGETRESPONSE,
    serialized_options=b'\202\323\344\223\002\024\022\022/v1/resources/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='v1.Resources.Update',
    index=2,
    containing_service=None,
    input_type=_RESOURCEUPDATEREQUEST,
    output_type=_RESOURCEUPDATERESPONSE,
    serialized_options=b'\202\323\344\223\002\027\032\022/v1/resources/{id}:\001*',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='v1.Resources.Delete',
    index=3,
    containing_service=None,
    input_type=_RESOURCEDELETEREQUEST,
    output_type=_RESOURCEDELETERESPONSE,
    serialized_options=b'\202\323\344\223\002\024*\022/v1/resources/{id}',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='v1.Resources.List',
    index=4,
    containing_service=None,
    input_type=_RESOURCELISTREQUEST,
    output_type=_RESOURCELISTRESPONSE,
    serialized_options=b'\202\323\344\223\002\017\022\r/v1/resources',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESOURCES)

DESCRIPTOR.services_by_name['Resources'] = _RESOURCES

# @@protoc_insertion_point(module_scope)
