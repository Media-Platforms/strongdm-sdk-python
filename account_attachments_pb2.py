# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: account_attachments.proto

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
from . import options_pb2 as options__pb2
from . import spec_pb2 as spec__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='account_attachments.proto',
  package='v1',
  syntax='proto3',
  serialized_options=_b('\n\034com.strongdm.api.v1.plumbingB\032AccountAttachmentsPlumbing'),
  serialized_pb=_b('\n\x19\x61\x63\x63ount_attachments.proto\x12\x02v1\x1a\x1cgoogle/api/annotations.proto\x1a,protoc-gen-swagger/options/annotations.proto\x1a\roptions.proto\x1a\nspec.proto\"\xdc\x01\n\x1e\x41\x63\x63ountAttachmentCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12=\n\x12\x61\x63\x63ount_attachment\x18\x02 \x01(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12?\n\x07options\x18\x03 \x01(\x0b\x32\".v1.AccountAttachmentCreateOptionsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x11\xfa\xf8\xb3\x07\x0c\xba\xf3\xb3\x07\x07options\"K\n\x1e\x41\x63\x63ountAttachmentCreateOptions\x12\x1d\n\toverwrite\x18\x01 \x01(\x08\x42\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\xd9\x01\n\x1f\x41\x63\x63ountAttachmentCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12=\n\x12\x61\x63\x63ount_attachment\x18\x02 \x01(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"[\n\x1b\x41\x63\x63ountAttachmentGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd3\x01\n\x1c\x41\x63\x63ountAttachmentGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12=\n\x12\x61\x63\x63ount_attachment\x18\x02 \x01(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"a\n\x1e\x41\x63\x63ountAttachmentDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\x9a\x01\n\x1f\x41\x63\x63ountAttachmentDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"a\n\x1c\x41\x63\x63ountAttachmentListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xbe\x01\n\x1d\x41\x63\x63ountAttachmentListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12>\n\x13\x61\x63\x63ount_attachments\x18\x02 \x03(\x0b\x32\x15.v1.AccountAttachmentB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12\x35\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\"\xd7\x02\n\x11\x41\x63\x63ountAttachment\x12*\n\x02id\x18\x01 \x01(\tB\x1e\xf2\xf8\xb3\x07\x19\xa2\xf3\xb3\x07\x02ID\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x08UserRole\x12\x32\n\naccount_id\x18\x02 \x01(\tB\x1e\xf2\xf8\xb3\x07\x19\xa2\xf3\xb3\x07\x06UserID\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x04User\x12/\n\x07role_id\x18\x03 \x01(\tB\x1e\xf2\xf8\xb3\x07\x19\xa2\xf3\xb3\x07\x06RoleID\xb0\xf3\xb3\x07\x01\xca\xf3\xb3\x07\x04Role:\xb0\x01\xfa\xf8\xb3\x07\x12\xa2\xf3\xb3\x07\x08UserRole\xa8\xf3\xb3\x07\x01\x92\x41\x95\x01*T\n\x14\x41 AccountAttachment.\x12<https://www.strongdm.com/docs/api/entities#AccountAttachment2=\x12;{ \"id\": \"aa-244\", \"role_id\": \"r-111\", \"account_id\":\"a-444\"}2\xef\x04\n\x12\x41\x63\x63ountAttachments\x12\xe7\x01\n\x06\x43reate\x12\".v1.AccountAttachmentCreateRequest\x1a#.v1.AccountAttachmentCreateResponse\"\x93\x01\x82\xd3\xe4\x93\x02\x1b\"\x16/v1/accountAttachments:\x01*\x92\x41o\"m\n%Learn how to make a AccountAttachment\x12\x44https://www.strongdm.com/docs/api/services/AccountAttachments#Create\x12m\n\x03Get\x12\x1f.v1.AccountAttachmentGetRequest\x1a .v1.AccountAttachmentGetResponse\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/v1/accountAttachments/{id}\x12v\n\x06\x44\x65lete\x12\".v1.AccountAttachmentDeleteRequest\x1a#.v1.AccountAttachmentDeleteResponse\"#\x82\xd3\xe4\x93\x02\x1d*\x1b/v1/accountAttachments/{id}\x12k\n\x04List\x12 .v1.AccountAttachmentListRequest\x1a!.v1.AccountAttachmentListResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/accountAttachments\x1a\x1b\xca\xf9\xb3\x07\x16\xc2\xf9\xb3\x07\x11\x41\x63\x63ountAttachmentB:\n\x1c\x63om.strongdm.api.v1.plumbingB\x1a\x41\x63\x63ountAttachmentsPlumbingb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__swagger_dot_options_dot_annotations__pb2.DESCRIPTOR,options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,])




_ACCOUNTATTACHMENTCREATEREQUEST = _descriptor.Descriptor(
  name='AccountAttachmentCreateRequest',
  full_name='v1.AccountAttachmentCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentCreateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_attachment', full_name='v1.AccountAttachmentCreateRequest.account_attachment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='v1.AccountAttachmentCreateRequest.options', index=2,
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
  serialized_options=_b('\372\370\263\007\014\272\363\263\007\007options'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=357,
)


_ACCOUNTATTACHMENTCREATEOPTIONS = _descriptor.Descriptor(
  name='AccountAttachmentCreateOptions',
  full_name='v1.AccountAttachmentCreateOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='overwrite', full_name='v1.AccountAttachmentCreateOptions.overwrite', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=359,
  serialized_end=434,
)


_ACCOUNTATTACHMENTCREATERESPONSE = _descriptor.Descriptor(
  name='AccountAttachmentCreateResponse',
  full_name='v1.AccountAttachmentCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentCreateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_attachment', full_name='v1.AccountAttachmentCreateResponse.account_attachment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountAttachmentCreateResponse.rate_limit', index=2,
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
  serialized_start=437,
  serialized_end=654,
)


_ACCOUNTATTACHMENTGETREQUEST = _descriptor.Descriptor(
  name='AccountAttachmentGetRequest',
  full_name='v1.AccountAttachmentGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentGetRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountAttachmentGetRequest.id', index=1,
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
  serialized_start=656,
  serialized_end=747,
)


_ACCOUNTATTACHMENTGETRESPONSE = _descriptor.Descriptor(
  name='AccountAttachmentGetResponse',
  full_name='v1.AccountAttachmentGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentGetResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_attachment', full_name='v1.AccountAttachmentGetResponse.account_attachment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountAttachmentGetResponse.rate_limit', index=2,
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
  serialized_start=750,
  serialized_end=961,
)


_ACCOUNTATTACHMENTDELETEREQUEST = _descriptor.Descriptor(
  name='AccountAttachmentDeleteRequest',
  full_name='v1.AccountAttachmentDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountAttachmentDeleteRequest.id', index=1,
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
  serialized_start=963,
  serialized_end=1060,
)


_ACCOUNTATTACHMENTDELETERESPONSE = _descriptor.Descriptor(
  name='AccountAttachmentDeleteResponse',
  full_name='v1.AccountAttachmentDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\260\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountAttachmentDeleteResponse.rate_limit', index=1,
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
  serialized_start=1063,
  serialized_end=1217,
)


_ACCOUNTATTACHMENTLISTREQUEST = _descriptor.Descriptor(
  name='AccountAttachmentListRequest',
  full_name='v1.AccountAttachmentListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentListRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='v1.AccountAttachmentListRequest.filter', index=1,
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
  serialized_start=1219,
  serialized_end=1316,
)


_ACCOUNTATTACHMENTLISTRESPONSE = _descriptor.Descriptor(
  name='AccountAttachmentListResponse',
  full_name='v1.AccountAttachmentListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.AccountAttachmentListResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_attachments', full_name='v1.AccountAttachmentListResponse.account_attachments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\005\270\363\263\007\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.AccountAttachmentListResponse.rate_limit', index=2,
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
  serialized_start=1319,
  serialized_end=1509,
)


_ACCOUNTATTACHMENT = _descriptor.Descriptor(
  name='AccountAttachment',
  full_name='v1.AccountAttachment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AccountAttachment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\031\242\363\263\007\002ID\260\363\263\007\001\312\363\263\007\010UserRole'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_id', full_name='v1.AccountAttachment.account_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\031\242\363\263\007\006UserID\260\363\263\007\001\312\363\263\007\004User'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='v1.AccountAttachment.role_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\362\370\263\007\031\242\363\263\007\006RoleID\260\363\263\007\001\312\363\263\007\004Role'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\372\370\263\007\022\242\363\263\007\010UserRole\250\363\263\007\001\222A\225\001*T\n\024A AccountAttachment.\022<https://www.strongdm.com/docs/api/entities#AccountAttachment2=\022;{ \"id\": \"aa-244\", \"role_id\": \"r-111\", \"account_id\":\"a-444\"}'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1512,
  serialized_end=1855,
)

_ACCOUNTATTACHMENTCREATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._CREATEREQUESTMETADATA
_ACCOUNTATTACHMENTCREATEREQUEST.fields_by_name['account_attachment'].message_type = _ACCOUNTATTACHMENT
_ACCOUNTATTACHMENTCREATEREQUEST.fields_by_name['options'].message_type = _ACCOUNTATTACHMENTCREATEOPTIONS
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._CREATERESPONSEMETADATA
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['account_attachment'].message_type = _ACCOUNTATTACHMENT
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTATTACHMENTGETREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['account_attachment'].message_type = _ACCOUNTATTACHMENT
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTATTACHMENTDELETEREQUEST.fields_by_name['meta'].message_type = spec__pb2._DELETEREQUESTMETADATA
_ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['meta'].message_type = spec__pb2._DELETERESPONSEMETADATA
_ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ACCOUNTATTACHMENTLISTREQUEST.fields_by_name['meta'].message_type = spec__pb2._LISTREQUESTMETADATA
_ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['meta'].message_type = spec__pb2._LISTRESPONSEMETADATA
_ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['account_attachments'].message_type = _ACCOUNTATTACHMENT
_ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
DESCRIPTOR.message_types_by_name['AccountAttachmentCreateRequest'] = _ACCOUNTATTACHMENTCREATEREQUEST
DESCRIPTOR.message_types_by_name['AccountAttachmentCreateOptions'] = _ACCOUNTATTACHMENTCREATEOPTIONS
DESCRIPTOR.message_types_by_name['AccountAttachmentCreateResponse'] = _ACCOUNTATTACHMENTCREATERESPONSE
DESCRIPTOR.message_types_by_name['AccountAttachmentGetRequest'] = _ACCOUNTATTACHMENTGETREQUEST
DESCRIPTOR.message_types_by_name['AccountAttachmentGetResponse'] = _ACCOUNTATTACHMENTGETRESPONSE
DESCRIPTOR.message_types_by_name['AccountAttachmentDeleteRequest'] = _ACCOUNTATTACHMENTDELETEREQUEST
DESCRIPTOR.message_types_by_name['AccountAttachmentDeleteResponse'] = _ACCOUNTATTACHMENTDELETERESPONSE
DESCRIPTOR.message_types_by_name['AccountAttachmentListRequest'] = _ACCOUNTATTACHMENTLISTREQUEST
DESCRIPTOR.message_types_by_name['AccountAttachmentListResponse'] = _ACCOUNTATTACHMENTLISTRESPONSE
DESCRIPTOR.message_types_by_name['AccountAttachment'] = _ACCOUNTATTACHMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountAttachmentCreateRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTCREATEREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentCreateRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentCreateRequest)

AccountAttachmentCreateOptions = _reflection.GeneratedProtocolMessageType('AccountAttachmentCreateOptions', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTCREATEOPTIONS,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentCreateOptions)
  })
_sym_db.RegisterMessage(AccountAttachmentCreateOptions)

AccountAttachmentCreateResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTCREATERESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentCreateResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentCreateResponse)

AccountAttachmentGetRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTGETREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentGetRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentGetRequest)

AccountAttachmentGetResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTGETRESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentGetResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentGetResponse)

AccountAttachmentDeleteRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTDELETEREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentDeleteRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentDeleteRequest)

AccountAttachmentDeleteResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTDELETERESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentDeleteResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentDeleteResponse)

AccountAttachmentListRequest = _reflection.GeneratedProtocolMessageType('AccountAttachmentListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTLISTREQUEST,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentListRequest)
  })
_sym_db.RegisterMessage(AccountAttachmentListRequest)

AccountAttachmentListResponse = _reflection.GeneratedProtocolMessageType('AccountAttachmentListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENTLISTRESPONSE,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachmentListResponse)
  })
_sym_db.RegisterMessage(AccountAttachmentListResponse)

AccountAttachment = _reflection.GeneratedProtocolMessageType('AccountAttachment', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTATTACHMENT,
  '__module__' : 'account_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.AccountAttachment)
  })
_sym_db.RegisterMessage(AccountAttachment)


DESCRIPTOR._options = None
_ACCOUNTATTACHMENTCREATEREQUEST.fields_by_name['account_attachment']._options = None
_ACCOUNTATTACHMENTCREATEREQUEST.fields_by_name['options']._options = None
_ACCOUNTATTACHMENTCREATEREQUEST._options = None
_ACCOUNTATTACHMENTCREATEOPTIONS.fields_by_name['overwrite']._options = None
_ACCOUNTATTACHMENTCREATEOPTIONS._options = None
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['meta']._options = None
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['account_attachment']._options = None
_ACCOUNTATTACHMENTCREATERESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTATTACHMENTCREATERESPONSE._options = None
_ACCOUNTATTACHMENTGETREQUEST.fields_by_name['id']._options = None
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['meta']._options = None
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['account_attachment']._options = None
_ACCOUNTATTACHMENTGETRESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTATTACHMENTGETRESPONSE._options = None
_ACCOUNTATTACHMENTDELETEREQUEST.fields_by_name['id']._options = None
_ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['meta']._options = None
_ACCOUNTATTACHMENTDELETERESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTATTACHMENTDELETERESPONSE._options = None
_ACCOUNTATTACHMENTLISTREQUEST.fields_by_name['filter']._options = None
_ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['account_attachments']._options = None
_ACCOUNTATTACHMENTLISTRESPONSE.fields_by_name['rate_limit']._options = None
_ACCOUNTATTACHMENT.fields_by_name['id']._options = None
_ACCOUNTATTACHMENT.fields_by_name['account_id']._options = None
_ACCOUNTATTACHMENT.fields_by_name['role_id']._options = None
_ACCOUNTATTACHMENT._options = None

_ACCOUNTATTACHMENTS = _descriptor.ServiceDescriptor(
  name='AccountAttachments',
  full_name='v1.AccountAttachments',
  file=DESCRIPTOR,
  index=0,
  serialized_options=_b('\312\371\263\007\026\302\371\263\007\021AccountAttachment'),
  serialized_start=1858,
  serialized_end=2481,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='v1.AccountAttachments.Create',
    index=0,
    containing_service=None,
    input_type=_ACCOUNTATTACHMENTCREATEREQUEST,
    output_type=_ACCOUNTATTACHMENTCREATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\033\"\026/v1/accountAttachments:\001*\222Ao\"m\n%Learn how to make a AccountAttachment\022Dhttps://www.strongdm.com/docs/api/services/AccountAttachments#Create'),
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='v1.AccountAttachments.Get',
    index=1,
    containing_service=None,
    input_type=_ACCOUNTATTACHMENTGETREQUEST,
    output_type=_ACCOUNTATTACHMENTGETRESPONSE,
    serialized_options=_b('\202\323\344\223\002\035\022\033/v1/accountAttachments/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='v1.AccountAttachments.Delete',
    index=2,
    containing_service=None,
    input_type=_ACCOUNTATTACHMENTDELETEREQUEST,
    output_type=_ACCOUNTATTACHMENTDELETERESPONSE,
    serialized_options=_b('\202\323\344\223\002\035*\033/v1/accountAttachments/{id}'),
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='v1.AccountAttachments.List',
    index=3,
    containing_service=None,
    input_type=_ACCOUNTATTACHMENTLISTREQUEST,
    output_type=_ACCOUNTATTACHMENTLISTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\030\022\026/v1/accountAttachments'),
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTATTACHMENTS)

DESCRIPTOR.services_by_name['AccountAttachments'] = _ACCOUNTATTACHMENTS

# @@protoc_insertion_point(module_scope)
