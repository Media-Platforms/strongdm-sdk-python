# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nodes.proto

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
import options_pb2 as options__pb2
import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nodes.proto',
  package='v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bnodes.proto\x12\x02v1\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\roptions.proto\x1a\nspec.proto\"U\n\x11NodeCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12\x17\n\x05nodes\x18\x02 \x03(\x0b\x32\x08.v1.Node\"\xba\x01\n\x12NodeCreateResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadata\x12\x17\n\x05nodes\x18\x02 \x03(\x0b\x32\x08.v1.Node\x12\x32\n\x06tokens\x18\x03 \x03(\x0b\x32\".v1.NodeCreateResponse.TokensEntry\x1a-\n\x0bTokensEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"B\n\x0eNodeGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\"P\n\x0fNodeGetResponse\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadata\x12\x16\n\x04node\x18\x02 \x01(\x0b\x32\x08.v1.Node\"`\n\x11NodeUpdateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.UpdateRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\x12\x16\n\x04node\x18\x03 \x01(\x0b\x32\x08.v1.Node\"V\n\x12NodeUpdateResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.UpdateResponseMetadata\x12\x16\n\x04node\x18\x02 \x01(\x0b\x32\x08.v1.Node\"H\n\x11NodeDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\n\n\x02id\x18\x02 \x01(\t\">\n\x12NodeDeleteResponse\x12(\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadata\"H\n\x0fNodeListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\"S\n\x10NodeListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12\x17\n\x05nodes\x18\x02 \x03(\x0b\x32\x08.v1.Node\"_\n\x16NodeBatchUpdateRequest\x12,\n\x04meta\x18\x01 \x01(\x0b\x32\x1e.v1.BatchUpdateRequestMetadata\x12\x17\n\x05nodes\x18\x02 \x03(\x0b\x32\x08.v1.Node\"a\n\x17NodeBatchUpdateResponse\x12-\n\x04meta\x18\x01 \x01(\x0b\x32\x1f.v1.BatchUpdateResponseMetadata\x12\x17\n\x05nodes\x18\x02 \x03(\x0b\x32\x08.v1.Node\"S\n\x16NodeBatchDeleteRequest\x12,\n\x04meta\x18\x01 \x01(\x0b\x32\x1e.v1.BatchDeleteRequestMetadata\x12\x0b\n\x03ids\x18\x02 \x03(\t\"H\n\x17NodeBatchDeleteResponse\x12-\n\x04meta\x18\x01 \x01(\x0b\x32\x1f.v1.BatchDeleteResponseMetadata\"\xcb\x01\n\x04Node\x12\x1a\n\x05relay\x18\x01 \x01(\x0b\x32\t.v1.RelayH\x00\x12\x1e\n\x07gateway\x18\x02 \x01(\x0b\x32\x0b.v1.GatewayH\x00:o\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x92\x41\x62*:\n\x07\x41 node.\x12/https://www.strongdm.com/docs/api/entities#Node2$\x12\"{ \"id\": \"7\", \"name\": \"happy-goat\"}B\x16\n\x04node\x12\x0e\xaa\xf8\xb3\x07\t\xa2\xf8\xb3\x07\x04Node\"Y\n\x05Relay\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xf2\xf8\xb3\x07\x07\xa2\xf3\xb3\x07\x02ID\x12\x1c\n\x04name\x18\x02 \x01(\tB\x0e\xf2\xf8\xb3\x07\t\xa2\xf3\xb3\x07\x04Name:\x18\xfa\xf8\xb3\x07\t\xa2\xf3\xb3\x07\x04Node\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xc7\x01\n\x07Gateway\x12\x18\n\x02id\x18\x01 \x01(\tB\x0c\xf2\xf8\xb3\x07\x07\xa2\xf3\xb3\x07\x02ID\x12\x1c\n\x04name\x18\x02 \x01(\tB\x0e\xf2\xf8\xb3\x07\t\xa2\xf3\xb3\x07\x04Name\x12\x36\n\x0elisten_address\x18\x03 \x01(\tB\x1e\xf2\xf8\xb3\x07\x0f\xa2\xf3\xb3\x07\nListenAddr\xf2\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x12\x32\n\x0c\x62ind_address\x18\x04 \x01(\tB\x1c\xf2\xf8\xb3\x07\r\xa2\xf3\xb3\x07\x08\x42indAddr\xf2\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01:\x18\xfa\xf8\xb3\x07\t\xa2\xf3\xb3\x07\x04Node\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x32\x9b\x05\n\x05Nodes\x12\xa5\x01\n\x06\x43reate\x12\x15.v1.NodeCreateRequest\x1a\x16.v1.NodeCreateResponse\"l\x82\xd3\xe4\x93\x02\x0e\"\t/v1/nodes:\x01*\x92\x41U\"S\n\x18Learn how to make a Node\x12\x37https://www.strongdm.com/docs/api/services/Nodes#Create\x12\x46\n\x03Get\x12\x12.v1.NodeGetRequest\x1a\x13.v1.NodeGetResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/nodes/{id}\x12R\n\x06Update\x12\x15.v1.NodeUpdateRequest\x1a\x16.v1.NodeUpdateResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x1a\x0e/v1/nodes/{id}:\x01*\x12O\n\x06\x44\x65lete\x12\x15.v1.NodeDeleteRequest\x1a\x16.v1.NodeDeleteResponse\"\x16\x82\xd3\xe4\x93\x02\x10*\x0e/v1/nodes/{id}\x12\x44\n\x04List\x12\x13.v1.NodeListRequest\x1a\x14.v1.NodeListResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/v1/nodes\x12\\\n\x0b\x42\x61tchUpdate\x12\x1a.v1.NodeBatchUpdateRequest\x1a\x1b.v1.NodeBatchUpdateResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x1a\t/v1/nodes:\x01*\x12Y\n\x0b\x42\x61tchDelete\x12\x1a.v1.NodeBatchDeleteRequest\x1a\x1b.v1.NodeBatchDeleteResponse\"\x11\x82\xd3\xe4\x93\x02\x0b*\t/v1/nodesb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,])




_NODECREATEREQUEST = _descriptor.Descriptor(
  name='NodeCreateRequest',
  full_name='v1.NodeCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeCreateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='v1.NodeCreateRequest.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=122,
  serialized_end=207,
)


_NODECREATERESPONSE_TOKENSENTRY = _descriptor.Descriptor(
  name='TokensEntry',
  full_name='v1.NodeCreateResponse.TokensEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='v1.NodeCreateResponse.TokensEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='v1.NodeCreateResponse.TokensEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=396,
)

_NODECREATERESPONSE = _descriptor.Descriptor(
  name='NodeCreateResponse',
  full_name='v1.NodeCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeCreateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='v1.NodeCreateResponse.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tokens', full_name='v1.NodeCreateResponse.tokens', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_NODECREATERESPONSE_TOKENSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=210,
  serialized_end=396,
)


_NODEGETREQUEST = _descriptor.Descriptor(
  name='NodeGetRequest',
  full_name='v1.NodeGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeGetRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.NodeGetRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=398,
  serialized_end=464,
)


_NODEGETRESPONSE = _descriptor.Descriptor(
  name='NodeGetResponse',
  full_name='v1.NodeGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeGetResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node', full_name='v1.NodeGetResponse.node', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=466,
  serialized_end=546,
)


_NODEUPDATEREQUEST = _descriptor.Descriptor(
  name='NodeUpdateRequest',
  full_name='v1.NodeUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeUpdateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.NodeUpdateRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node', full_name='v1.NodeUpdateRequest.node', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=548,
  serialized_end=644,
)


_NODEUPDATERESPONSE = _descriptor.Descriptor(
  name='NodeUpdateResponse',
  full_name='v1.NodeUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeUpdateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node', full_name='v1.NodeUpdateResponse.node', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=646,
  serialized_end=732,
)


_NODEDELETEREQUEST = _descriptor.Descriptor(
  name='NodeDeleteRequest',
  full_name='v1.NodeDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.NodeDeleteRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=734,
  serialized_end=806,
)


_NODEDELETERESPONSE = _descriptor.Descriptor(
  name='NodeDeleteResponse',
  full_name='v1.NodeDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=808,
  serialized_end=870,
)


_NODELISTREQUEST = _descriptor.Descriptor(
  name='NodeListRequest',
  full_name='v1.NodeListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeListRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='v1.NodeListRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=872,
  serialized_end=944,
)


_NODELISTRESPONSE = _descriptor.Descriptor(
  name='NodeListResponse',
  full_name='v1.NodeListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeListResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='v1.NodeListResponse.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=946,
  serialized_end=1029,
)


_NODEBATCHUPDATEREQUEST = _descriptor.Descriptor(
  name='NodeBatchUpdateRequest',
  full_name='v1.NodeBatchUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeBatchUpdateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='v1.NodeBatchUpdateRequest.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1031,
  serialized_end=1126,
)


_NODEBATCHUPDATERESPONSE = _descriptor.Descriptor(
  name='NodeBatchUpdateResponse',
  full_name='v1.NodeBatchUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeBatchUpdateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nodes', full_name='v1.NodeBatchUpdateResponse.nodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1128,
  serialized_end=1225,
)


_NODEBATCHDELETEREQUEST = _descriptor.Descriptor(
  name='NodeBatchDeleteRequest',
  full_name='v1.NodeBatchDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeBatchDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ids', full_name='v1.NodeBatchDeleteRequest.ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1227,
  serialized_end=1310,
)


_NODEBATCHDELETERESPONSE = _descriptor.Descriptor(
  name='NodeBatchDeleteResponse',
  full_name='v1.NodeBatchDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.NodeBatchDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=1312,
  serialized_end=1384,
)


_NODE = _descriptor.Descriptor(
  name='Node',
  full_name='v1.Node',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='relay', full_name='v1.Node.relay', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gateway', full_name='v1.Node.gateway', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\005\250\363\263\007\001\222Ab*:\n\007A node.\022/https://www.strongdm.com/docs/api/entities#Node2$\022\"{ \"id\": \"7\", \"name\": \"happy-goat\"}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='node', full_name='v1.Node.node',
      index=0, containing_type=None, fields=[], serialized_options=_b('\252\370\263\007\t\242\370\263\007\004Node')),
  ],
  serialized_start=1387,
  serialized_end=1590,
)


_RELAY = _descriptor.Descriptor(
  name='Relay',
  full_name='v1.Relay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.Relay.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\007\242\363\263\007\002ID'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.Relay.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\t\242\363\263\007\004Name'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\t\242\363\263\007\004Node\372\370\263\007\005\250\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1592,
  serialized_end=1681,
)


_GATEWAY = _descriptor.Descriptor(
  name='Gateway',
  full_name='v1.Gateway',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.Gateway.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\007\242\363\263\007\002ID'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.Gateway.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\t\242\363\263\007\004Name'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='listen_address', full_name='v1.Gateway.listen_address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\017\242\363\263\007\nListenAddr\362\370\263\007\005\250\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bind_address', full_name='v1.Gateway.bind_address', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\r\242\363\263\007\010BindAddr\362\370\263\007\005\250\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\t\242\363\263\007\004Node\372\370\263\007\005\250\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1684,
  serialized_end=1883,
)

_NODECREATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._CREATEREQUESTMETADATA
_NODECREATEREQUEST.fields_by_name['nodes'].message_type = _NODE
_NODECREATERESPONSE_TOKENSENTRY.containing_type = _NODECREATERESPONSE
_NODECREATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._CREATERESPONSEMETADATA
_NODECREATERESPONSE.fields_by_name['nodes'].message_type = _NODE
_NODECREATERESPONSE.fields_by_name['tokens'].message_type = _NODECREATERESPONSE_TOKENSENTRY
_NODEGETREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_NODEGETRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_NODEGETRESPONSE.fields_by_name['node'].message_type = _NODE
_NODEUPDATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._UPDATEREQUESTMETADATA
_NODEUPDATEREQUEST.fields_by_name['node'].message_type = _NODE
_NODEUPDATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._UPDATERESPONSEMETADATA
_NODEUPDATERESPONSE.fields_by_name['node'].message_type = _NODE
_NODEDELETEREQUEST.fields_by_name['meta'].message_type = spec__pb2._DELETEREQUESTMETADATA
_NODEDELETERESPONSE.fields_by_name['meta'].message_type = spec__pb2._DELETERESPONSEMETADATA
_NODELISTREQUEST.fields_by_name['meta'].message_type = spec__pb2._LISTREQUESTMETADATA
_NODELISTRESPONSE.fields_by_name['meta'].message_type = spec__pb2._LISTRESPONSEMETADATA
_NODELISTRESPONSE.fields_by_name['nodes'].message_type = _NODE
_NODEBATCHUPDATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._BATCHUPDATEREQUESTMETADATA
_NODEBATCHUPDATEREQUEST.fields_by_name['nodes'].message_type = _NODE
_NODEBATCHUPDATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._BATCHUPDATERESPONSEMETADATA
_NODEBATCHUPDATERESPONSE.fields_by_name['nodes'].message_type = _NODE
_NODEBATCHDELETEREQUEST.fields_by_name['meta'].message_type = spec__pb2._BATCHDELETEREQUESTMETADATA
_NODEBATCHDELETERESPONSE.fields_by_name['meta'].message_type = spec__pb2._BATCHDELETERESPONSEMETADATA
_NODE.fields_by_name['relay'].message_type = _RELAY
_NODE.fields_by_name['gateway'].message_type = _GATEWAY
_NODE.oneofs_by_name['node'].fields.append(
  _NODE.fields_by_name['relay'])
_NODE.fields_by_name['relay'].containing_oneof = _NODE.oneofs_by_name['node']
_NODE.oneofs_by_name['node'].fields.append(
  _NODE.fields_by_name['gateway'])
_NODE.fields_by_name['gateway'].containing_oneof = _NODE.oneofs_by_name['node']
DESCRIPTOR.message_types_by_name['NodeCreateRequest'] = _NODECREATEREQUEST
DESCRIPTOR.message_types_by_name['NodeCreateResponse'] = _NODECREATERESPONSE
DESCRIPTOR.message_types_by_name['NodeGetRequest'] = _NODEGETREQUEST
DESCRIPTOR.message_types_by_name['NodeGetResponse'] = _NODEGETRESPONSE
DESCRIPTOR.message_types_by_name['NodeUpdateRequest'] = _NODEUPDATEREQUEST
DESCRIPTOR.message_types_by_name['NodeUpdateResponse'] = _NODEUPDATERESPONSE
DESCRIPTOR.message_types_by_name['NodeDeleteRequest'] = _NODEDELETEREQUEST
DESCRIPTOR.message_types_by_name['NodeDeleteResponse'] = _NODEDELETERESPONSE
DESCRIPTOR.message_types_by_name['NodeListRequest'] = _NODELISTREQUEST
DESCRIPTOR.message_types_by_name['NodeListResponse'] = _NODELISTRESPONSE
DESCRIPTOR.message_types_by_name['NodeBatchUpdateRequest'] = _NODEBATCHUPDATEREQUEST
DESCRIPTOR.message_types_by_name['NodeBatchUpdateResponse'] = _NODEBATCHUPDATERESPONSE
DESCRIPTOR.message_types_by_name['NodeBatchDeleteRequest'] = _NODEBATCHDELETEREQUEST
DESCRIPTOR.message_types_by_name['NodeBatchDeleteResponse'] = _NODEBATCHDELETERESPONSE
DESCRIPTOR.message_types_by_name['Node'] = _NODE
DESCRIPTOR.message_types_by_name['Relay'] = _RELAY
DESCRIPTOR.message_types_by_name['Gateway'] = _GATEWAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeCreateRequest = _reflection.GeneratedProtocolMessageType('NodeCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODECREATEREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeCreateRequest)
  })
_sym_db.RegisterMessage(NodeCreateRequest)

NodeCreateResponse = _reflection.GeneratedProtocolMessageType('NodeCreateResponse', (_message.Message,), {

  'TokensEntry' : _reflection.GeneratedProtocolMessageType('TokensEntry', (_message.Message,), {
    'DESCRIPTOR' : _NODECREATERESPONSE_TOKENSENTRY,
    '__module__' : 'nodes_pb2'
    # @@protoc_insertion_point(class_scope:v1.NodeCreateResponse.TokensEntry)
    })
  ,
  'DESCRIPTOR' : _NODECREATERESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeCreateResponse)
  })
_sym_db.RegisterMessage(NodeCreateResponse)
_sym_db.RegisterMessage(NodeCreateResponse.TokensEntry)

NodeGetRequest = _reflection.GeneratedProtocolMessageType('NodeGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEGETREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeGetRequest)
  })
_sym_db.RegisterMessage(NodeGetRequest)

NodeGetResponse = _reflection.GeneratedProtocolMessageType('NodeGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODEGETRESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeGetResponse)
  })
_sym_db.RegisterMessage(NodeGetResponse)

NodeUpdateRequest = _reflection.GeneratedProtocolMessageType('NodeUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEUPDATEREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeUpdateRequest)
  })
_sym_db.RegisterMessage(NodeUpdateRequest)

NodeUpdateResponse = _reflection.GeneratedProtocolMessageType('NodeUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODEUPDATERESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeUpdateResponse)
  })
_sym_db.RegisterMessage(NodeUpdateResponse)

NodeDeleteRequest = _reflection.GeneratedProtocolMessageType('NodeDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEDELETEREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeDeleteRequest)
  })
_sym_db.RegisterMessage(NodeDeleteRequest)

NodeDeleteResponse = _reflection.GeneratedProtocolMessageType('NodeDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODEDELETERESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeDeleteResponse)
  })
_sym_db.RegisterMessage(NodeDeleteResponse)

NodeListRequest = _reflection.GeneratedProtocolMessageType('NodeListRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODELISTREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeListRequest)
  })
_sym_db.RegisterMessage(NodeListRequest)

NodeListResponse = _reflection.GeneratedProtocolMessageType('NodeListResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODELISTRESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeListResponse)
  })
_sym_db.RegisterMessage(NodeListResponse)

NodeBatchUpdateRequest = _reflection.GeneratedProtocolMessageType('NodeBatchUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEBATCHUPDATEREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeBatchUpdateRequest)
  })
_sym_db.RegisterMessage(NodeBatchUpdateRequest)

NodeBatchUpdateResponse = _reflection.GeneratedProtocolMessageType('NodeBatchUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODEBATCHUPDATERESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeBatchUpdateResponse)
  })
_sym_db.RegisterMessage(NodeBatchUpdateResponse)

NodeBatchDeleteRequest = _reflection.GeneratedProtocolMessageType('NodeBatchDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _NODEBATCHDELETEREQUEST,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeBatchDeleteRequest)
  })
_sym_db.RegisterMessage(NodeBatchDeleteRequest)

NodeBatchDeleteResponse = _reflection.GeneratedProtocolMessageType('NodeBatchDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _NODEBATCHDELETERESPONSE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.NodeBatchDeleteResponse)
  })
_sym_db.RegisterMessage(NodeBatchDeleteResponse)

Node = _reflection.GeneratedProtocolMessageType('Node', (_message.Message,), {
  'DESCRIPTOR' : _NODE,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.Node)
  })
_sym_db.RegisterMessage(Node)

Relay = _reflection.GeneratedProtocolMessageType('Relay', (_message.Message,), {
  'DESCRIPTOR' : _RELAY,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.Relay)
  })
_sym_db.RegisterMessage(Relay)

Gateway = _reflection.GeneratedProtocolMessageType('Gateway', (_message.Message,), {
  'DESCRIPTOR' : _GATEWAY,
  '__module__' : 'nodes_pb2'
  # @@protoc_insertion_point(class_scope:v1.Gateway)
  })
_sym_db.RegisterMessage(Gateway)


_NODECREATERESPONSE_TOKENSENTRY._options = None
_NODE.oneofs_by_name['node']._options = None
_NODE._options = None
_RELAY.fields_by_name['id']._options = None
_RELAY.fields_by_name['name']._options = None
_RELAY._options = None
_GATEWAY.fields_by_name['id']._options = None
_GATEWAY.fields_by_name['name']._options = None
_GATEWAY.fields_by_name['listen_address']._options = None
_GATEWAY.fields_by_name['bind_address']._options = None
_GATEWAY._options = None

_NODES = _descriptor.ServiceDescriptor(
  name='Nodes',
  full_name='v1.Nodes',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1886,
  serialized_end=2553,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='v1.Nodes.Create',
    index=0,
    containing_service=None,
    input_type=_NODECREATEREQUEST,
    output_type=_NODECREATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\"\t/v1/nodes:\001*\222AU\"S\n\030Learn how to make a Node\0227https://www.strongdm.com/docs/api/services/Nodes#Create'),
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='v1.Nodes.Get',
    index=1,
    containing_service=None,
    input_type=_NODEGETREQUEST,
    output_type=_NODEGETRESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\022\016/v1/nodes/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='v1.Nodes.Update',
    index=2,
    containing_service=None,
    input_type=_NODEUPDATEREQUEST,
    output_type=_NODEUPDATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\023\032\016/v1/nodes/{id}:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='v1.Nodes.Delete',
    index=3,
    containing_service=None,
    input_type=_NODEDELETEREQUEST,
    output_type=_NODEDELETERESPONSE,
    serialized_options=_b('\202\323\344\223\002\020*\016/v1/nodes/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='v1.Nodes.List',
    index=4,
    containing_service=None,
    input_type=_NODELISTREQUEST,
    output_type=_NODELISTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\013\022\t/v1/nodes'),
  ),
  _descriptor.MethodDescriptor(
    name='BatchUpdate',
    full_name='v1.Nodes.BatchUpdate',
    index=5,
    containing_service=None,
    input_type=_NODEBATCHUPDATEREQUEST,
    output_type=_NODEBATCHUPDATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\032\t/v1/nodes:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='BatchDelete',
    full_name='v1.Nodes.BatchDelete',
    index=6,
    containing_service=None,
    input_type=_NODEBATCHDELETEREQUEST,
    output_type=_NODEBATCHDELETERESPONSE,
    serialized_options=_b('\202\323\344\223\002\013*\t/v1/nodes'),
  ),
])
_sym_db.RegisterServiceDescriptor(_NODES)

DESCRIPTOR.services_by_name['Nodes'] = _NODES

# @@protoc_insertion_point(module_scope)
