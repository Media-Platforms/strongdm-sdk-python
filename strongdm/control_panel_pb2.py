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
# source: control_panel.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='control_panel.proto',
  package='v1',
  syntax='proto3',
  serialized_options=b'\n\034com.strongdm.api.v1.plumbingB\024ControlPanelPlumbingZ2github.com/strongdm/strongdm-sdk-go/internal/v1;v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x63ontrol_panel.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"L\n$ControlPanelGetSSHCAPublicKeyRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\"\xc7\x01\n%ControlPanelGetSSHCAPublicKeyResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1e\n\npublic_key\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"_\n\x1c\x43ontrolPanelVerifyJWTRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x19\n\x05token\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xba\x01\n\x1d\x43ontrolPanelVerifyJWTResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x19\n\x05valid\x18\x02 \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x32\xb4\x02\n\x0c\x43ontrolPanel\x12\x99\x01\n\x11GetSSHCAPublicKey\x12(.v1.ControlPanelGetSSHCAPublicKeyRequest\x1a).v1.ControlPanelGetSSHCAPublicKeyResponse\"/\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1d\xaa\xf3\xb3\x07\x18/v1/control-panel/ssh/ca\x12\x87\x01\n\tVerifyJWT\x12 .v1.ControlPanelVerifyJWTRequest\x1a!.v1.ControlPanelVerifyJWTResponse\"5\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\"\xaa\xf3\xb3\x07\x1d/v1/control-panel/http/verifyBh\n\x1c\x63om.strongdm.api.v1.plumbingB\x14\x43ontrolPanelPlumbingZ2github.com/strongdm/strongdm-sdk-go/internal/v1;v1b\x06proto3'
  ,
  dependencies=[options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,])




_CONTROLPANELGETSSHCAPUBLICKEYREQUEST = _descriptor.Descriptor(
  name='ControlPanelGetSSHCAPublicKeyRequest',
  full_name='v1.ControlPanelGetSSHCAPublicKeyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ControlPanelGetSSHCAPublicKeyRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=54,
  serialized_end=130,
)


_CONTROLPANELGETSSHCAPUBLICKEYRESPONSE = _descriptor.Descriptor(
  name='ControlPanelGetSSHCAPublicKeyResponse',
  full_name='v1.ControlPanelGetSSHCAPublicKeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ControlPanelGetSSHCAPublicKeyResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='public_key', full_name='v1.ControlPanelGetSSHCAPublicKeyResponse.public_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.ControlPanelGetSSHCAPublicKeyResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\005\220\364\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=133,
  serialized_end=332,
)


_CONTROLPANELVERIFYJWTREQUEST = _descriptor.Descriptor(
  name='ControlPanelVerifyJWTRequest',
  full_name='v1.ControlPanelVerifyJWTRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ControlPanelVerifyJWTRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='token', full_name='v1.ControlPanelVerifyJWTRequest.token', index=1,
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
  serialized_start=334,
  serialized_end=429,
)


_CONTROLPANELVERIFYJWTRESPONSE = _descriptor.Descriptor(
  name='ControlPanelVerifyJWTResponse',
  full_name='v1.ControlPanelVerifyJWTResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.ControlPanelVerifyJWTResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='valid', full_name='v1.ControlPanelVerifyJWTResponse.valid', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.ControlPanelVerifyJWTResponse.rate_limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001\362\370\263\007\005\220\364\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=432,
  serialized_end=618,
)

_CONTROLPANELGETSSHCAPUBLICKEYREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_CONTROLPANELVERIFYJWTREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
DESCRIPTOR.message_types_by_name['ControlPanelGetSSHCAPublicKeyRequest'] = _CONTROLPANELGETSSHCAPUBLICKEYREQUEST
DESCRIPTOR.message_types_by_name['ControlPanelGetSSHCAPublicKeyResponse'] = _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE
DESCRIPTOR.message_types_by_name['ControlPanelVerifyJWTRequest'] = _CONTROLPANELVERIFYJWTREQUEST
DESCRIPTOR.message_types_by_name['ControlPanelVerifyJWTResponse'] = _CONTROLPANELVERIFYJWTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ControlPanelGetSSHCAPublicKeyRequest = _reflection.GeneratedProtocolMessageType('ControlPanelGetSSHCAPublicKeyRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLPANELGETSSHCAPUBLICKEYREQUEST,
  '__module__' : 'control_panel_pb2'
  # @@protoc_insertion_point(class_scope:v1.ControlPanelGetSSHCAPublicKeyRequest)
  })
_sym_db.RegisterMessage(ControlPanelGetSSHCAPublicKeyRequest)

ControlPanelGetSSHCAPublicKeyResponse = _reflection.GeneratedProtocolMessageType('ControlPanelGetSSHCAPublicKeyResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLPANELGETSSHCAPUBLICKEYRESPONSE,
  '__module__' : 'control_panel_pb2'
  # @@protoc_insertion_point(class_scope:v1.ControlPanelGetSSHCAPublicKeyResponse)
  })
_sym_db.RegisterMessage(ControlPanelGetSSHCAPublicKeyResponse)

ControlPanelVerifyJWTRequest = _reflection.GeneratedProtocolMessageType('ControlPanelVerifyJWTRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLPANELVERIFYJWTREQUEST,
  '__module__' : 'control_panel_pb2'
  # @@protoc_insertion_point(class_scope:v1.ControlPanelVerifyJWTRequest)
  })
_sym_db.RegisterMessage(ControlPanelVerifyJWTRequest)

ControlPanelVerifyJWTResponse = _reflection.GeneratedProtocolMessageType('ControlPanelVerifyJWTResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONTROLPANELVERIFYJWTRESPONSE,
  '__module__' : 'control_panel_pb2'
  # @@protoc_insertion_point(class_scope:v1.ControlPanelVerifyJWTResponse)
  })
_sym_db.RegisterMessage(ControlPanelVerifyJWTResponse)


DESCRIPTOR._options = None
_CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['meta']._options = None
_CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['public_key']._options = None
_CONTROLPANELGETSSHCAPUBLICKEYRESPONSE.fields_by_name['rate_limit']._options = None
_CONTROLPANELGETSSHCAPUBLICKEYRESPONSE._options = None
_CONTROLPANELVERIFYJWTREQUEST.fields_by_name['token']._options = None
_CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['meta']._options = None
_CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['valid']._options = None
_CONTROLPANELVERIFYJWTRESPONSE.fields_by_name['rate_limit']._options = None
_CONTROLPANELVERIFYJWTRESPONSE._options = None

_CONTROLPANEL = _descriptor.ServiceDescriptor(
  name='ControlPanel',
  full_name='v1.ControlPanel',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=621,
  serialized_end=929,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetSSHCAPublicKey',
    full_name='v1.ControlPanel.GetSSHCAPublicKey',
    index=0,
    containing_service=None,
    input_type=_CONTROLPANELGETSSHCAPUBLICKEYREQUEST,
    output_type=_CONTROLPANELGETSSHCAPUBLICKEYRESPONSE,
    serialized_options=b'\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\035\252\363\263\007\030/v1/control-panel/ssh/ca',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='VerifyJWT',
    full_name='v1.ControlPanel.VerifyJWT',
    index=1,
    containing_service=None,
    input_type=_CONTROLPANELVERIFYJWTREQUEST,
    output_type=_CONTROLPANELVERIFYJWTRESPONSE,
    serialized_options=b'\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\"\252\363\263\007\035/v1/control-panel/http/verify',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTROLPANEL)

DESCRIPTOR.services_by_name['ControlPanel'] = _CONTROLPANEL

# @@protoc_insertion_point(module_scope)
