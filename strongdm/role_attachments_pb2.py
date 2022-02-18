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
# source: role_attachments.proto
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
  name='role_attachments.proto',
  package='v1',
  syntax='proto3',
  serialized_options=b'\n\034com.strongdm.api.v1.plumbingB\027RoleAttachmentsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v2/internal/v1;v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16role_attachments.proto\x12\x02v1\x1a\roptions.proto\x1a\nspec.proto\"\x83\x01\n\x1bRoleAttachmentCreateRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.CreateRequestMetadata\x12\x37\n\x0frole_attachment\x18\x02 \x01(\x0b\x32\x12.v1.RoleAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x02\x18\x01\"\xdc\x01\n\x1cRoleAttachmentCreateResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.CreateResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x37\n\x0frole_attachment\x18\x02 \x01(\x0b\x32\x12.v1.RoleAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01:\x0c\x18\x01\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"\\\n\x18RoleAttachmentGetRequest\x12$\n\x04meta\x18\x01 \x01(\x0b\x32\x16.v1.GetRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x02\x18\x01\"\xd6\x01\n\x19RoleAttachmentGetResponse\x12\x31\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.GetResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x37\n\x0frole_attachment\x18\x02 \x01(\x0b\x32\x12.v1.RoleAttachmentB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01:\x0c\x18\x01\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"b\n\x1bRoleAttachmentDeleteRequest\x12\'\n\x04meta\x18\x01 \x01(\x0b\x32\x19.v1.DeleteRequestMetadata\x12\x16\n\x02id\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x02\x18\x01\"\xa3\x01\n\x1cRoleAttachmentDeleteResponse\x12\x34\n\x04meta\x18\x01 \x01(\x0b\x32\x1a.v1.DeleteResponseMetadataB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x02 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01:\x0c\x18\x01\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\"b\n\x19RoleAttachmentListRequest\x12%\n\x04meta\x18\x01 \x01(\x0b\x32\x17.v1.ListRequestMetadata\x12\x1a\n\x06\x66ilter\x18\x02 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:\x02\x18\x01\"\xc3\x01\n\x1aRoleAttachmentListResponse\x12&\n\x04meta\x18\x01 \x01(\x0b\x32\x18.v1.ListResponseMetadata\x12\x38\n\x10role_attachments\x18\x02 \x03(\x0b\x32\x12.v1.RoleAttachmentB\n\xf2\xf8\xb3\x07\x05\xb8\xf3\xb3\x07\x01\x12?\n\nrate_limit\x18\x03 \x01(\x0b\x32\x15.v1.RateLimitMetadataB\x14\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\xf2\xf8\xb3\x07\x05\x90\xf4\xb3\x07\x01:\x02\x18\x01\"\xef\x01\n\x0eRoleAttachment\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12*\n\x11\x63omposite_role_id\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12)\n\x10\x61ttached_role_id\x18\x03 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01:n\x18\x01\xfa\xf8\xb3\x07g\xa8\xf3\xb3\x07\x01\xc2\xf3\xb3\x07]\xa2\xf3\xb3\x07(tf_examples/role_attachment_resource.txt\xaa\xf3\xb3\x07+tf_examples/role_attachment_data_source.txt2\x82\x05\n\x0fRoleAttachments\x12\x90\x01\n\x06\x43reate\x12\x1f.v1.RoleAttachmentCreateRequest\x1a .v1.RoleAttachmentCreateResponse\"C\x88\x02\x01\x82\xf9\xb3\x07\t\xa2\xf3\xb3\x07\x04post\x82\xf9\xb3\x07\x19\xaa\xf3\xb3\x07\x14/v1/role-attachments\x82\xf9\xb3\x07\x0f\xb2\xf3\xb3\x07\n2022-03-31\x12\x8b\x01\n\x03Get\x12\x1c.v1.RoleAttachmentGetRequest\x1a\x1d.v1.RoleAttachmentGetResponse\"G\x88\x02\x01\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x1e\xaa\xf3\xb3\x07\x19/v1/role-attachments/{id}\x82\xf9\xb3\x07\x0f\xb2\xf3\xb3\x07\n2022-03-31\x12\x97\x01\n\x06\x44\x65lete\x12\x1f.v1.RoleAttachmentDeleteRequest\x1a .v1.RoleAttachmentDeleteResponse\"J\x88\x02\x01\x82\xf9\xb3\x07\x0b\xa2\xf3\xb3\x07\x06\x64\x65lete\x82\xf9\xb3\x07\x1e\xaa\xf3\xb3\x07\x19/v1/role-attachments/{id}\x82\xf9\xb3\x07\x0f\xb2\xf3\xb3\x07\n2022-03-31\x12\x89\x01\n\x04List\x12\x1d.v1.RoleAttachmentListRequest\x1a\x1e.v1.RoleAttachmentListResponse\"B\x88\x02\x01\x82\xf9\xb3\x07\x08\xa2\xf3\xb3\x07\x03get\x82\xf9\xb3\x07\x19\xaa\xf3\xb3\x07\x14/v1/role-attachments\x82\xf9\xb3\x07\x0f\xb2\xf3\xb3\x07\n2022-03-31\x1a(\x88\x02\x01\xca\xf9\xb3\x07\x13\xc2\xf9\xb3\x07\x0eRoleAttachment\xca\xf9\xb3\x07\x08\xd2\xf9\xb3\x07\x03ra-Bn\n\x1c\x63om.strongdm.api.v1.plumbingB\x17RoleAttachmentsPlumbingZ5github.com/strongdm/strongdm-sdk-go/v2/internal/v1;v1b\x06proto3'
  ,
  dependencies=[options__pb2.DESCRIPTOR,spec__pb2.DESCRIPTOR,])




_ROLEATTACHMENTCREATEREQUEST = _descriptor.Descriptor(
  name='RoleAttachmentCreateRequest',
  full_name='v1.RoleAttachmentCreateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleAttachmentCreateRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_attachment', full_name='v1.RoleAttachmentCreateRequest.role_attachment', index=1,
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
  serialized_options=b'\030\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=189,
)


_ROLEATTACHMENTCREATERESPONSE = _descriptor.Descriptor(
  name='RoleAttachmentCreateResponse',
  full_name='v1.RoleAttachmentCreateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleAttachmentCreateResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_attachment', full_name='v1.RoleAttachmentCreateResponse.role_attachment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleAttachmentCreateResponse.rate_limit', index=2,
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
  serialized_options=b'\030\001\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=412,
)


_ROLEATTACHMENTGETREQUEST = _descriptor.Descriptor(
  name='RoleAttachmentGetRequest',
  full_name='v1.RoleAttachmentGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleAttachmentGetRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleAttachmentGetRequest.id', index=1,
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
  serialized_options=b'\030\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=414,
  serialized_end=506,
)


_ROLEATTACHMENTGETRESPONSE = _descriptor.Descriptor(
  name='RoleAttachmentGetResponse',
  full_name='v1.RoleAttachmentGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleAttachmentGetResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_attachment', full_name='v1.RoleAttachmentGetResponse.role_attachment', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleAttachmentGetResponse.rate_limit', index=2,
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
  serialized_options=b'\030\001\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=509,
  serialized_end=723,
)


_ROLEATTACHMENTDELETEREQUEST = _descriptor.Descriptor(
  name='RoleAttachmentDeleteRequest',
  full_name='v1.RoleAttachmentDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleAttachmentDeleteRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleAttachmentDeleteRequest.id', index=1,
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
  serialized_options=b'\030\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=725,
  serialized_end=823,
)


_ROLEATTACHMENTDELETERESPONSE = _descriptor.Descriptor(
  name='RoleAttachmentDeleteResponse',
  full_name='v1.RoleAttachmentDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleAttachmentDeleteResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleAttachmentDeleteResponse.rate_limit', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\030\001\372\370\263\007\005\250\363\263\007\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=826,
  serialized_end=989,
)


_ROLEATTACHMENTLISTREQUEST = _descriptor.Descriptor(
  name='RoleAttachmentListRequest',
  full_name='v1.RoleAttachmentListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleAttachmentListRequest.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter', full_name='v1.RoleAttachmentListRequest.filter', index=1,
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
  serialized_options=b'\030\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=991,
  serialized_end=1089,
)


_ROLEATTACHMENTLISTRESPONSE = _descriptor.Descriptor(
  name='RoleAttachmentListResponse',
  full_name='v1.RoleAttachmentListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta', full_name='v1.RoleAttachmentListResponse.meta', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='role_attachments', full_name='v1.RoleAttachmentListResponse.role_attachments', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\270\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rate_limit', full_name='v1.RoleAttachmentListResponse.rate_limit', index=2,
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
  serialized_options=b'\030\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1092,
  serialized_end=1287,
)


_ROLEATTACHMENT = _descriptor.Descriptor(
  name='RoleAttachment',
  full_name='v1.RoleAttachment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.RoleAttachment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='composite_role_id', full_name='v1.RoleAttachment.composite_role_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attached_role_id', full_name='v1.RoleAttachment.attached_role_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'\030\001\372\370\263\007g\250\363\263\007\001\302\363\263\007]\242\363\263\007(tf_examples/role_attachment_resource.txt\252\363\263\007+tf_examples/role_attachment_data_source.txt',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1290,
  serialized_end=1529,
)

_ROLEATTACHMENTCREATEREQUEST.fields_by_name['meta'].message_type = spec__pb2._CREATEREQUESTMETADATA
_ROLEATTACHMENTCREATEREQUEST.fields_by_name['role_attachment'].message_type = _ROLEATTACHMENT
_ROLEATTACHMENTCREATERESPONSE.fields_by_name['meta'].message_type = spec__pb2._CREATERESPONSEMETADATA
_ROLEATTACHMENTCREATERESPONSE.fields_by_name['role_attachment'].message_type = _ROLEATTACHMENT
_ROLEATTACHMENTCREATERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLEATTACHMENTGETREQUEST.fields_by_name['meta'].message_type = spec__pb2._GETREQUESTMETADATA
_ROLEATTACHMENTGETRESPONSE.fields_by_name['meta'].message_type = spec__pb2._GETRESPONSEMETADATA
_ROLEATTACHMENTGETRESPONSE.fields_by_name['role_attachment'].message_type = _ROLEATTACHMENT
_ROLEATTACHMENTGETRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLEATTACHMENTDELETEREQUEST.fields_by_name['meta'].message_type = spec__pb2._DELETEREQUESTMETADATA
_ROLEATTACHMENTDELETERESPONSE.fields_by_name['meta'].message_type = spec__pb2._DELETERESPONSEMETADATA
_ROLEATTACHMENTDELETERESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
_ROLEATTACHMENTLISTREQUEST.fields_by_name['meta'].message_type = spec__pb2._LISTREQUESTMETADATA
_ROLEATTACHMENTLISTRESPONSE.fields_by_name['meta'].message_type = spec__pb2._LISTRESPONSEMETADATA
_ROLEATTACHMENTLISTRESPONSE.fields_by_name['role_attachments'].message_type = _ROLEATTACHMENT
_ROLEATTACHMENTLISTRESPONSE.fields_by_name['rate_limit'].message_type = spec__pb2._RATELIMITMETADATA
DESCRIPTOR.message_types_by_name['RoleAttachmentCreateRequest'] = _ROLEATTACHMENTCREATEREQUEST
DESCRIPTOR.message_types_by_name['RoleAttachmentCreateResponse'] = _ROLEATTACHMENTCREATERESPONSE
DESCRIPTOR.message_types_by_name['RoleAttachmentGetRequest'] = _ROLEATTACHMENTGETREQUEST
DESCRIPTOR.message_types_by_name['RoleAttachmentGetResponse'] = _ROLEATTACHMENTGETRESPONSE
DESCRIPTOR.message_types_by_name['RoleAttachmentDeleteRequest'] = _ROLEATTACHMENTDELETEREQUEST
DESCRIPTOR.message_types_by_name['RoleAttachmentDeleteResponse'] = _ROLEATTACHMENTDELETERESPONSE
DESCRIPTOR.message_types_by_name['RoleAttachmentListRequest'] = _ROLEATTACHMENTLISTREQUEST
DESCRIPTOR.message_types_by_name['RoleAttachmentListResponse'] = _ROLEATTACHMENTLISTRESPONSE
DESCRIPTOR.message_types_by_name['RoleAttachment'] = _ROLEATTACHMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RoleAttachmentCreateRequest = _reflection.GeneratedProtocolMessageType('RoleAttachmentCreateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTCREATEREQUEST,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentCreateRequest)
  })
_sym_db.RegisterMessage(RoleAttachmentCreateRequest)

RoleAttachmentCreateResponse = _reflection.GeneratedProtocolMessageType('RoleAttachmentCreateResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTCREATERESPONSE,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentCreateResponse)
  })
_sym_db.RegisterMessage(RoleAttachmentCreateResponse)

RoleAttachmentGetRequest = _reflection.GeneratedProtocolMessageType('RoleAttachmentGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTGETREQUEST,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentGetRequest)
  })
_sym_db.RegisterMessage(RoleAttachmentGetRequest)

RoleAttachmentGetResponse = _reflection.GeneratedProtocolMessageType('RoleAttachmentGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTGETRESPONSE,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentGetResponse)
  })
_sym_db.RegisterMessage(RoleAttachmentGetResponse)

RoleAttachmentDeleteRequest = _reflection.GeneratedProtocolMessageType('RoleAttachmentDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTDELETEREQUEST,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentDeleteRequest)
  })
_sym_db.RegisterMessage(RoleAttachmentDeleteRequest)

RoleAttachmentDeleteResponse = _reflection.GeneratedProtocolMessageType('RoleAttachmentDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTDELETERESPONSE,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentDeleteResponse)
  })
_sym_db.RegisterMessage(RoleAttachmentDeleteResponse)

RoleAttachmentListRequest = _reflection.GeneratedProtocolMessageType('RoleAttachmentListRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTLISTREQUEST,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentListRequest)
  })
_sym_db.RegisterMessage(RoleAttachmentListRequest)

RoleAttachmentListResponse = _reflection.GeneratedProtocolMessageType('RoleAttachmentListResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENTLISTRESPONSE,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachmentListResponse)
  })
_sym_db.RegisterMessage(RoleAttachmentListResponse)

RoleAttachment = _reflection.GeneratedProtocolMessageType('RoleAttachment', (_message.Message,), {
  'DESCRIPTOR' : _ROLEATTACHMENT,
  '__module__' : 'role_attachments_pb2'
  # @@protoc_insertion_point(class_scope:v1.RoleAttachment)
  })
_sym_db.RegisterMessage(RoleAttachment)


DESCRIPTOR._options = None
_ROLEATTACHMENTCREATEREQUEST.fields_by_name['role_attachment']._options = None
_ROLEATTACHMENTCREATEREQUEST._options = None
_ROLEATTACHMENTCREATERESPONSE.fields_by_name['meta']._options = None
_ROLEATTACHMENTCREATERESPONSE.fields_by_name['role_attachment']._options = None
_ROLEATTACHMENTCREATERESPONSE.fields_by_name['rate_limit']._options = None
_ROLEATTACHMENTCREATERESPONSE._options = None
_ROLEATTACHMENTGETREQUEST.fields_by_name['id']._options = None
_ROLEATTACHMENTGETREQUEST._options = None
_ROLEATTACHMENTGETRESPONSE.fields_by_name['meta']._options = None
_ROLEATTACHMENTGETRESPONSE.fields_by_name['role_attachment']._options = None
_ROLEATTACHMENTGETRESPONSE.fields_by_name['rate_limit']._options = None
_ROLEATTACHMENTGETRESPONSE._options = None
_ROLEATTACHMENTDELETEREQUEST.fields_by_name['id']._options = None
_ROLEATTACHMENTDELETEREQUEST._options = None
_ROLEATTACHMENTDELETERESPONSE.fields_by_name['meta']._options = None
_ROLEATTACHMENTDELETERESPONSE.fields_by_name['rate_limit']._options = None
_ROLEATTACHMENTDELETERESPONSE._options = None
_ROLEATTACHMENTLISTREQUEST.fields_by_name['filter']._options = None
_ROLEATTACHMENTLISTREQUEST._options = None
_ROLEATTACHMENTLISTRESPONSE.fields_by_name['role_attachments']._options = None
_ROLEATTACHMENTLISTRESPONSE.fields_by_name['rate_limit']._options = None
_ROLEATTACHMENTLISTRESPONSE._options = None
_ROLEATTACHMENT.fields_by_name['id']._options = None
_ROLEATTACHMENT.fields_by_name['composite_role_id']._options = None
_ROLEATTACHMENT.fields_by_name['attached_role_id']._options = None
_ROLEATTACHMENT._options = None

_ROLEATTACHMENTS = _descriptor.ServiceDescriptor(
  name='RoleAttachments',
  full_name='v1.RoleAttachments',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\210\002\001\312\371\263\007\023\302\371\263\007\016RoleAttachment\312\371\263\007\010\322\371\263\007\003ra-',
  create_key=_descriptor._internal_create_key,
  serialized_start=1532,
  serialized_end=2174,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='v1.RoleAttachments.Create',
    index=0,
    containing_service=None,
    input_type=_ROLEATTACHMENTCREATEREQUEST,
    output_type=_ROLEATTACHMENTCREATERESPONSE,
    serialized_options=b'\210\002\001\202\371\263\007\t\242\363\263\007\004post\202\371\263\007\031\252\363\263\007\024/v1/role-attachments\202\371\263\007\017\262\363\263\007\n2022-03-31',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='v1.RoleAttachments.Get',
    index=1,
    containing_service=None,
    input_type=_ROLEATTACHMENTGETREQUEST,
    output_type=_ROLEATTACHMENTGETRESPONSE,
    serialized_options=b'\210\002\001\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\036\252\363\263\007\031/v1/role-attachments/{id}\202\371\263\007\017\262\363\263\007\n2022-03-31',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='v1.RoleAttachments.Delete',
    index=2,
    containing_service=None,
    input_type=_ROLEATTACHMENTDELETEREQUEST,
    output_type=_ROLEATTACHMENTDELETERESPONSE,
    serialized_options=b'\210\002\001\202\371\263\007\013\242\363\263\007\006delete\202\371\263\007\036\252\363\263\007\031/v1/role-attachments/{id}\202\371\263\007\017\262\363\263\007\n2022-03-31',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='List',
    full_name='v1.RoleAttachments.List',
    index=3,
    containing_service=None,
    input_type=_ROLEATTACHMENTLISTREQUEST,
    output_type=_ROLEATTACHMENTLISTRESPONSE,
    serialized_options=b'\210\002\001\202\371\263\007\010\242\363\263\007\003get\202\371\263\007\031\252\363\263\007\024/v1/role-attachments\202\371\263\007\017\262\363\263\007\n2022-03-31',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROLEATTACHMENTS)

DESCRIPTOR.services_by_name['RoleAttachments'] = _ROLEATTACHMENTS

# @@protoc_insertion_point(module_scope)
