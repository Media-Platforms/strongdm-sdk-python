# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spec.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import options_pb2 as options__pb2
from protoc_gen_swagger.options import annotations_pb2 as protoc__gen__swagger_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spec.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\034com.strongdm.api.v1.plumbing\222A\215\002\022\260\001\n\034gRPC/JSON Gateway Tech Spike\022;an exploration of how it feels to use the gRPC JSON gateway\"N\n\022gRPC-Gateway spike\022\"https://www.strongdm.com/docs/api/\032\024support@strongdm.com2\0031.0\032\020app.strongdm.comrF\n!Learn more about the strongDM API\022!https://www.strongdm.com/docs/api'),
  serialized_pb=_b('\n\nspec.proto\x12\x02v1\x1a\roptions.proto\x1a,protoc-gen-swagger/options/annotations.proto\"b\n\x12\x41lreadyExistsError\x12)\n\x08\x65ntities\x18\x01 \x03(\tB\x17\xf2\xf8\xb3\x07\x12\xa2\xf3\xb3\x07\x08\x45ntities\xb0\xf3\xb3\x07\x01:!\xfa\xf8\xb3\x07\x1c\xa2\xf3\xb3\x07\x12\x41lreadyExistsError\xb0\xf3\xb3\x07\x01\"X\n\rNotFoundError\x12)\n\x08\x65ntities\x18\x01 \x03(\tB\x17\xf2\xf8\xb3\x07\x12\xa2\xf3\xb3\x07\x08\x45ntities\xb0\xf3\xb3\x07\x01:\x1c\xfa\xf8\xb3\x07\x17\xa2\xf3\xb3\x07\rNotFoundError\xb0\xf3\xb3\x07\x01\"1\n\x0f\x42\x61\x64RequestError:\x1e\xfa\xf8\xb3\x07\x19\xa2\xf3\xb3\x07\x0f\x42\x61\x64RequestError\xb0\xf3\xb3\x07\x01\"9\n\x13\x41uthenticationError:\"\xfa\xf8\xb3\x07\x1d\xa2\xf3\xb3\x07\x13\x41uthenticationError\xb0\xf3\xb3\x07\x01\"1\n\x0fPermissionError:\x1e\xfa\xf8\xb3\x07\x19\xa2\xf3\xb3\x07\x0fPermissionError\xb0\xf3\xb3\x07\x01\"-\n\rInternalError:\x1c\xfa\xf8\xb3\x07\x17\xa2\xf3\xb3\x07\rInternalError\xb0\xf3\xb3\x07\x01\"/\n\x0eRateLimitError:\x1d\xfa\xf8\xb3\x07\x18\xa2\xf3\xb3\x07\x0eRateLimitError\xb0\xf3\xb3\x07\x01\"\x17\n\x15\x43reateRequestMetadata\"$\n\x16\x43reateResponseMetadata:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\x14\n\x12GetRequestMetadata\"!\n\x13GetResponseMetadata:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\x17\n\x15UpdateRequestMetadata\"$\n\x16UpdateResponseMetadata:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\x17\n\x15\x44\x65leteRequestMetadata\"$\n\x16\x44\x65leteResponseMetadata:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"B\n\x13ListRequestMetadata\x12\x0e\n\x06\x63ursor\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\r\n\x05limit\x18\x03 \x01(\x05\":\n\x14ListResponseMetadata\x12\x13\n\x0bnext_cursor\x18\x01 \x01(\t\x12\r\n\x05\x66ound\x18\x02 \x01(\x05\x42\xaf\x02\n\x1c\x63om.strongdm.api.v1.plumbing\x92\x41\x8d\x02\x12\xb0\x01\n\x1cgRPC/JSON Gateway Tech Spike\x12;an exploration of how it feels to use the gRPC JSON gateway\"N\n\x12gRPC-Gateway spike\x12\"https://www.strongdm.com/docs/api/\x1a\x14support@strongdm.com2\x03\x31.0\x1a\x10\x61pp.strongdm.comrF\n!Learn more about the strongDM API\x12!https://www.strongdm.com/docs/apib\x06proto3')
  ,
  dependencies=[options__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,])




_ALREADYEXISTSERROR = _descriptor.Descriptor(
  name='AlreadyExistsError',
  full_name='v1.AlreadyExistsError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='v1.AlreadyExistsError.entities', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\022\242\363\263\007\010Entities\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\034\242\363\263\007\022AlreadyExistsError\260\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=79,
  serialized_end=177,
)


_NOTFOUNDERROR = _descriptor.Descriptor(
  name='NotFoundError',
  full_name='v1.NotFoundError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entities', full_name='v1.NotFoundError.entities', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\022\242\363\263\007\010Entities\260\363\263\007\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\027\242\363\263\007\rNotFoundError\260\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=179,
  serialized_end=267,
)


_BADREQUESTERROR = _descriptor.Descriptor(
  name='BadRequestError',
  full_name='v1.BadRequestError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\031\242\363\263\007\017BadRequestError\260\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=269,
  serialized_end=318,
)


_AUTHENTICATIONERROR = _descriptor.Descriptor(
  name='AuthenticationError',
  full_name='v1.AuthenticationError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\035\242\363\263\007\023AuthenticationError\260\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=377,
)


_PERMISSIONERROR = _descriptor.Descriptor(
  name='PermissionError',
  full_name='v1.PermissionError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\031\242\363\263\007\017PermissionError\260\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=379,
  serialized_end=428,
)


_INTERNALERROR = _descriptor.Descriptor(
  name='InternalError',
  full_name='v1.InternalError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\027\242\363\263\007\rInternalError\260\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=430,
  serialized_end=475,
)


_RATELIMITERROR = _descriptor.Descriptor(
  name='RateLimitError',
  full_name='v1.RateLimitError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\030\242\363\263\007\016RateLimitError\260\363\263\007\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=524,
)


_CREATEREQUESTMETADATA = _descriptor.Descriptor(
  name='CreateRequestMetadata',
  full_name='v1.CreateRequestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=526,
  serialized_end=549,
)


_CREATERESPONSEMETADATA = _descriptor.Descriptor(
  name='CreateResponseMetadata',
  full_name='v1.CreateResponseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=551,
  serialized_end=587,
)


_GETREQUESTMETADATA = _descriptor.Descriptor(
  name='GetRequestMetadata',
  full_name='v1.GetRequestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=589,
  serialized_end=609,
)


_GETRESPONSEMETADATA = _descriptor.Descriptor(
  name='GetResponseMetadata',
  full_name='v1.GetResponseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=611,
  serialized_end=644,
)


_UPDATEREQUESTMETADATA = _descriptor.Descriptor(
  name='UpdateRequestMetadata',
  full_name='v1.UpdateRequestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_end=669,
)


_UPDATERESPONSEMETADATA = _descriptor.Descriptor(
  name='UpdateResponseMetadata',
  full_name='v1.UpdateResponseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=671,
  serialized_end=707,
)


_DELETEREQUESTMETADATA = _descriptor.Descriptor(
  name='DeleteRequestMetadata',
  full_name='v1.DeleteRequestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=709,
  serialized_end=732,
)


_DELETERESPONSEMETADATA = _descriptor.Descriptor(
  name='DeleteResponseMetadata',
  full_name='v1.DeleteResponseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=734,
  serialized_end=770,
)


_LISTREQUESTMETADATA = _descriptor.Descriptor(
  name='ListRequestMetadata',
  full_name='v1.ListRequestMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cursor', full_name='v1.ListRequestMetadata.cursor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='v1.ListRequestMetadata.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='v1.ListRequestMetadata.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=772,
  serialized_end=838,
)


_LISTRESPONSEMETADATA = _descriptor.Descriptor(
  name='ListResponseMetadata',
  full_name='v1.ListResponseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='next_cursor', full_name='v1.ListResponseMetadata.next_cursor', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='found', full_name='v1.ListResponseMetadata.found', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=840,
  serialized_end=898,
)

DESCRIPTOR.message_types_by_name['AlreadyExistsError'] = _ALREADYEXISTSERROR
DESCRIPTOR.message_types_by_name['NotFoundError'] = _NOTFOUNDERROR
DESCRIPTOR.message_types_by_name['BadRequestError'] = _BADREQUESTERROR
DESCRIPTOR.message_types_by_name['AuthenticationError'] = _AUTHENTICATIONERROR
DESCRIPTOR.message_types_by_name['PermissionError'] = _PERMISSIONERROR
DESCRIPTOR.message_types_by_name['InternalError'] = _INTERNALERROR
DESCRIPTOR.message_types_by_name['RateLimitError'] = _RATELIMITERROR
DESCRIPTOR.message_types_by_name['CreateRequestMetadata'] = _CREATEREQUESTMETADATA
DESCRIPTOR.message_types_by_name['CreateResponseMetadata'] = _CREATERESPONSEMETADATA
DESCRIPTOR.message_types_by_name['GetRequestMetadata'] = _GETREQUESTMETADATA
DESCRIPTOR.message_types_by_name['GetResponseMetadata'] = _GETRESPONSEMETADATA
DESCRIPTOR.message_types_by_name['UpdateRequestMetadata'] = _UPDATEREQUESTMETADATA
DESCRIPTOR.message_types_by_name['UpdateResponseMetadata'] = _UPDATERESPONSEMETADATA
DESCRIPTOR.message_types_by_name['DeleteRequestMetadata'] = _DELETEREQUESTMETADATA
DESCRIPTOR.message_types_by_name['DeleteResponseMetadata'] = _DELETERESPONSEMETADATA
DESCRIPTOR.message_types_by_name['ListRequestMetadata'] = _LISTREQUESTMETADATA
DESCRIPTOR.message_types_by_name['ListResponseMetadata'] = _LISTRESPONSEMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlreadyExistsError = _reflection.GeneratedProtocolMessageType('AlreadyExistsError', (_message.Message,), {
  'DESCRIPTOR' : _ALREADYEXISTSERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.AlreadyExistsError)
  })
_sym_db.RegisterMessage(AlreadyExistsError)

NotFoundError = _reflection.GeneratedProtocolMessageType('NotFoundError', (_message.Message,), {
  'DESCRIPTOR' : _NOTFOUNDERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.NotFoundError)
  })
_sym_db.RegisterMessage(NotFoundError)

BadRequestError = _reflection.GeneratedProtocolMessageType('BadRequestError', (_message.Message,), {
  'DESCRIPTOR' : _BADREQUESTERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.BadRequestError)
  })
_sym_db.RegisterMessage(BadRequestError)

AuthenticationError = _reflection.GeneratedProtocolMessageType('AuthenticationError', (_message.Message,), {
  'DESCRIPTOR' : _AUTHENTICATIONERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.AuthenticationError)
  })
_sym_db.RegisterMessage(AuthenticationError)

PermissionError = _reflection.GeneratedProtocolMessageType('PermissionError', (_message.Message,), {
  'DESCRIPTOR' : _PERMISSIONERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.PermissionError)
  })
_sym_db.RegisterMessage(PermissionError)

InternalError = _reflection.GeneratedProtocolMessageType('InternalError', (_message.Message,), {
  'DESCRIPTOR' : _INTERNALERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.InternalError)
  })
_sym_db.RegisterMessage(InternalError)

RateLimitError = _reflection.GeneratedProtocolMessageType('RateLimitError', (_message.Message,), {
  'DESCRIPTOR' : _RATELIMITERROR,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.RateLimitError)
  })
_sym_db.RegisterMessage(RateLimitError)

CreateRequestMetadata = _reflection.GeneratedProtocolMessageType('CreateRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATEREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.CreateRequestMetadata)
  })
_sym_db.RegisterMessage(CreateRequestMetadata)

CreateResponseMetadata = _reflection.GeneratedProtocolMessageType('CreateResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _CREATERESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.CreateResponseMetadata)
  })
_sym_db.RegisterMessage(CreateResponseMetadata)

GetRequestMetadata = _reflection.GeneratedProtocolMessageType('GetRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GETREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.GetRequestMetadata)
  })
_sym_db.RegisterMessage(GetRequestMetadata)

GetResponseMetadata = _reflection.GeneratedProtocolMessageType('GetResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _GETRESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.GetResponseMetadata)
  })
_sym_db.RegisterMessage(GetResponseMetadata)

UpdateRequestMetadata = _reflection.GeneratedProtocolMessageType('UpdateRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.UpdateRequestMetadata)
  })
_sym_db.RegisterMessage(UpdateRequestMetadata)

UpdateResponseMetadata = _reflection.GeneratedProtocolMessageType('UpdateResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _UPDATERESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.UpdateResponseMetadata)
  })
_sym_db.RegisterMessage(UpdateResponseMetadata)

DeleteRequestMetadata = _reflection.GeneratedProtocolMessageType('DeleteRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETEREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.DeleteRequestMetadata)
  })
_sym_db.RegisterMessage(DeleteRequestMetadata)

DeleteResponseMetadata = _reflection.GeneratedProtocolMessageType('DeleteResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _DELETERESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.DeleteResponseMetadata)
  })
_sym_db.RegisterMessage(DeleteResponseMetadata)

ListRequestMetadata = _reflection.GeneratedProtocolMessageType('ListRequestMetadata', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUESTMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.ListRequestMetadata)
  })
_sym_db.RegisterMessage(ListRequestMetadata)

ListResponseMetadata = _reflection.GeneratedProtocolMessageType('ListResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONSEMETADATA,
  '__module__' : 'spec_pb2'
  # @@protoc_insertion_point(class_scope:v1.ListResponseMetadata)
  })
_sym_db.RegisterMessage(ListResponseMetadata)


DESCRIPTOR._options = None
_ALREADYEXISTSERROR.fields_by_name['entities']._options = None
_ALREADYEXISTSERROR._options = None
_NOTFOUNDERROR.fields_by_name['entities']._options = None
_NOTFOUNDERROR._options = None
_BADREQUESTERROR._options = None
_AUTHENTICATIONERROR._options = None
_PERMISSIONERROR._options = None
_INTERNALERROR._options = None
_RATELIMITERROR._options = None
_CREATERESPONSEMETADATA._options = None
_GETRESPONSEMETADATA._options = None
_UPDATERESPONSEMETADATA._options = None
_DELETERESPONSEMETADATA._options = None
# @@protoc_insertion_point(module_scope)
