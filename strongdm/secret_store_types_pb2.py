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
# source: secret_store_types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import options_pb2 as options__pb2
from . import tags_pb2 as tags__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='secret_store_types.proto',
  package='v1',
  syntax='proto3',
  serialized_options=b'\n\034com.strongdm.api.v1.plumbingB\031SecretStoresTypesPlumbingZ2github.com/strongdm/strongdm-sdk-go/internal/v1;v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18secret_store_types.proto\x12\x02v1\x1a\roptions.proto\x1a\ntags.proto\"\xa3\x02\n\x0bSecretStore\x12*\n\x03\x61ws\x18\x03 \x01(\x0b\x32\x0c.v1.AWSStoreB\r\xf2\xf8\xb3\x07\x08\x8a\xf4\xb3\x07\x03\x61wsH\x00\x12\x30\n\x05\x61zure\x18\x65 \x01(\x0b\x32\x0e.v1.AzureStoreB\x0f\xf2\xf8\xb3\x07\n\x8a\xf4\xb3\x07\x05\x61zureH\x00\x12:\n\tvault_tls\x18\x01 \x01(\x0b\x32\x11.v1.VaultTLSStoreB\x12\xf2\xf8\xb3\x07\r\x8a\xf4\xb3\x07\x08vaultTLSH\x00\x12@\n\x0bvault_token\x18\x02 \x01(\x0b\x32\x13.v1.VaultTokenStoreB\x14\xf2\xf8\xb3\x07\x0f\x8a\xf4\xb3\x07\nvaultTokenH\x00:\n\xfa\xf8\xb3\x07\x05\xa8\xf3\xb3\x07\x01\x42,\n\x0csecret_store\x12\x1c\xaa\xf8\xb3\x07\t\xaa\xf8\xb3\x07\x04tags\xaa\xf8\xb3\x07\t\xaa\xf8\xb3\x07\x04name\"\xbd\x01\n\x08\x41WSStore\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12*\n\x06region\x18\x03 \x01(\tB\x1a\xf2\xf8\xb3\x07\x15\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x8a\xf4\xb3\x07\x06region\x12\"\n\x04tags\x18\x04 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:*\xfa\xf8\xb3\x07%\xa8\xf3\xb3\x07\x01\xda\xf3\xb3\x07\x03\x61ws\xe2\xf3\xb3\x07\x03\x61ws\xea\xf3\xb3\x07\x03\x61ws\xfa\xf3\xb3\x07\x03\x61ws\"\xc4\x01\n\nAzureStore\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12/\n\tvault_uri\x18\x03 \x01(\tB\x1c\xf2\xf8\xb3\x07\x17\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x8a\xf4\xb3\x07\x08vaultUri\x12$\n\x04tags\x18\x83\x80\x02 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:(\xfa\xf8\xb3\x07#\xa8\xf3\xb3\x07\x01\xda\xf3\xb3\x07\x05\x61zure\xe2\xf3\xb3\x07\x05\x61zure\xea\xf3\xb3\x07\x05\x61zure\"\xbe\x03\n\rVaultTLSStore\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12/\n\x0c\x43\x41_cert_path\x18\x04 \x01(\tB\x19\xf2\xf8\xb3\x07\x14\xb0\xf3\xb3\x07\x01\x8a\xf4\xb3\x07\ncaCertPath\x12<\n\x10\x63lient_cert_path\x18\x05 \x01(\tB\"\xf2\xf8\xb3\x07\x1d\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x8a\xf4\xb3\x07\x0e\x63lientCertPath\x12:\n\x0f\x63lient_key_path\x18\x06 \x01(\tB!\xf2\xf8\xb3\x07\x1c\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x8a\xf4\xb3\x07\rclientKeyPath\x12+\n\tnamespace\x18\x08 \x01(\tB\x18\xf2\xf8\xb3\x07\x13\xb0\xf3\xb3\x07\x01\x8a\xf4\xb3\x07\tnamespace\x12\x39\n\x0eserver_address\x18\x03 \x01(\tB!\xf2\xf8\xb3\x07\x1c\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x8a\xf4\xb3\x07\rserverAddress\x12\"\n\x04tags\x18\x07 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:?\xfa\xf8\xb3\x07:\xa8\xf3\xb3\x07\x01\xda\xf3\xb3\x07\x08vaultTLS\xe2\xf3\xb3\x07\x08vaultTLS\xea\xf3\xb3\x07\x08vaultTLS\xfa\xf3\xb3\x07\tvault_tls\"\x9d\x02\n\x0fVaultTokenStore\x12\x16\n\x02id\x18\x01 \x01(\tB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01\x12\x1d\n\x04name\x18\x02 \x01(\tB\x0f\xf2\xf8\xb3\x07\n\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x12+\n\tnamespace\x18\x05 \x01(\tB\x18\xf2\xf8\xb3\x07\x13\xb0\xf3\xb3\x07\x01\x8a\xf4\xb3\x07\tnamespace\x12\x39\n\x0eserver_address\x18\x03 \x01(\tB!\xf2\xf8\xb3\x07\x1c\xb0\xf3\xb3\x07\x01\xc0\xf3\xb3\x07\x01\x8a\xf4\xb3\x07\rserverAddress\x12\"\n\x04tags\x18\x04 \x01(\x0b\x32\x08.v1.TagsB\n\xf2\xf8\xb3\x07\x05\xb0\xf3\xb3\x07\x01:G\xfa\xf8\xb3\x07\x42\xa8\xf3\xb3\x07\x01\xda\xf3\xb3\x07\nvaultToken\xe2\xf3\xb3\x07\nvaultToken\xea\xf3\xb3\x07\nvaultToken\xfa\xf3\xb3\x07\x0bvault_tokenBm\n\x1c\x63om.strongdm.api.v1.plumbingB\x19SecretStoresTypesPlumbingZ2github.com/strongdm/strongdm-sdk-go/internal/v1;v1b\x06proto3'
  ,
  dependencies=[options__pb2.DESCRIPTOR,tags__pb2.DESCRIPTOR,])




_SECRETSTORE = _descriptor.Descriptor(
  name='SecretStore',
  full_name='v1.SecretStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='aws', full_name='v1.SecretStore.aws', index=0,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\010\212\364\263\007\003aws', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='azure', full_name='v1.SecretStore.azure', index=1,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\212\364\263\007\005azure', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vault_tls', full_name='v1.SecretStore.vault_tls', index=2,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\r\212\364\263\007\010vaultTLS', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vault_token', full_name='v1.SecretStore.vault_token', index=3,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\017\212\364\263\007\nvaultToken', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='secret_store', full_name='v1.SecretStore.secret_store',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[], serialized_options=b'\252\370\263\007\t\252\370\263\007\004tags\252\370\263\007\t\252\370\263\007\004name'),
  ],
  serialized_start=60,
  serialized_end=351,
)


_AWSSTORE = _descriptor.Descriptor(
  name='AWSStore',
  full_name='v1.AWSStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AWSStore.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.AWSStore.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='v1.AWSStore.region', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\025\260\363\263\007\001\300\363\263\007\001\212\364\263\007\006region', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.AWSStore.tags', index=3,
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
  serialized_options=b'\372\370\263\007%\250\363\263\007\001\332\363\263\007\003aws\342\363\263\007\003aws\352\363\263\007\003aws\372\363\263\007\003aws',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=543,
)


_AZURESTORE = _descriptor.Descriptor(
  name='AzureStore',
  full_name='v1.AzureStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.AzureStore.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.AzureStore.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vault_uri', full_name='v1.AzureStore.vault_uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\027\260\363\263\007\001\300\363\263\007\001\212\364\263\007\010vaultUri', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.AzureStore.tags', index=3,
      number=32771, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\372\370\263\007#\250\363\263\007\001\332\363\263\007\005azure\342\363\263\007\005azure\352\363\263\007\005azure',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=546,
  serialized_end=742,
)


_VAULTTLSSTORE = _descriptor.Descriptor(
  name='VaultTLSStore',
  full_name='v1.VaultTLSStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.VaultTLSStore.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.VaultTLSStore.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CA_cert_path', full_name='v1.VaultTLSStore.CA_cert_path', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\024\260\363\263\007\001\212\364\263\007\ncaCertPath', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_cert_path', full_name='v1.VaultTLSStore.client_cert_path', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\035\260\363\263\007\001\300\363\263\007\001\212\364\263\007\016clientCertPath', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client_key_path', full_name='v1.VaultTLSStore.client_key_path', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\034\260\363\263\007\001\300\363\263\007\001\212\364\263\007\rclientKeyPath', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='v1.VaultTLSStore.namespace', index=5,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\023\260\363\263\007\001\212\364\263\007\tnamespace', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server_address', full_name='v1.VaultTLSStore.server_address', index=6,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\034\260\363\263\007\001\300\363\263\007\001\212\364\263\007\rserverAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.VaultTLSStore.tags', index=7,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_options=b'\372\370\263\007:\250\363\263\007\001\332\363\263\007\010vaultTLS\342\363\263\007\010vaultTLS\352\363\263\007\010vaultTLS\372\363\263\007\tvault_tls',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=745,
  serialized_end=1191,
)


_VAULTTOKENSTORE = _descriptor.Descriptor(
  name='VaultTokenStore',
  full_name='v1.VaultTokenStore',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='v1.VaultTokenStore.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\005\260\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='v1.VaultTokenStore.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\n\260\363\263\007\001\300\363\263\007\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='v1.VaultTokenStore.namespace', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\023\260\363\263\007\001\212\364\263\007\tnamespace', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='server_address', full_name='v1.VaultTokenStore.server_address', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\362\370\263\007\034\260\363\263\007\001\300\363\263\007\001\212\364\263\007\rserverAddress', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='v1.VaultTokenStore.tags', index=4,
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
  serialized_options=b'\372\370\263\007B\250\363\263\007\001\332\363\263\007\nvaultToken\342\363\263\007\nvaultToken\352\363\263\007\nvaultToken\372\363\263\007\013vault_token',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1194,
  serialized_end=1479,
)

_SECRETSTORE.fields_by_name['aws'].message_type = _AWSSTORE
_SECRETSTORE.fields_by_name['azure'].message_type = _AZURESTORE
_SECRETSTORE.fields_by_name['vault_tls'].message_type = _VAULTTLSSTORE
_SECRETSTORE.fields_by_name['vault_token'].message_type = _VAULTTOKENSTORE
_SECRETSTORE.oneofs_by_name['secret_store'].fields.append(
  _SECRETSTORE.fields_by_name['aws'])
_SECRETSTORE.fields_by_name['aws'].containing_oneof = _SECRETSTORE.oneofs_by_name['secret_store']
_SECRETSTORE.oneofs_by_name['secret_store'].fields.append(
  _SECRETSTORE.fields_by_name['azure'])
_SECRETSTORE.fields_by_name['azure'].containing_oneof = _SECRETSTORE.oneofs_by_name['secret_store']
_SECRETSTORE.oneofs_by_name['secret_store'].fields.append(
  _SECRETSTORE.fields_by_name['vault_tls'])
_SECRETSTORE.fields_by_name['vault_tls'].containing_oneof = _SECRETSTORE.oneofs_by_name['secret_store']
_SECRETSTORE.oneofs_by_name['secret_store'].fields.append(
  _SECRETSTORE.fields_by_name['vault_token'])
_SECRETSTORE.fields_by_name['vault_token'].containing_oneof = _SECRETSTORE.oneofs_by_name['secret_store']
_AWSSTORE.fields_by_name['tags'].message_type = tags__pb2._TAGS
_AZURESTORE.fields_by_name['tags'].message_type = tags__pb2._TAGS
_VAULTTLSSTORE.fields_by_name['tags'].message_type = tags__pb2._TAGS
_VAULTTOKENSTORE.fields_by_name['tags'].message_type = tags__pb2._TAGS
DESCRIPTOR.message_types_by_name['SecretStore'] = _SECRETSTORE
DESCRIPTOR.message_types_by_name['AWSStore'] = _AWSSTORE
DESCRIPTOR.message_types_by_name['AzureStore'] = _AZURESTORE
DESCRIPTOR.message_types_by_name['VaultTLSStore'] = _VAULTTLSSTORE
DESCRIPTOR.message_types_by_name['VaultTokenStore'] = _VAULTTOKENSTORE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SecretStore = _reflection.GeneratedProtocolMessageType('SecretStore', (_message.Message,), {
  'DESCRIPTOR' : _SECRETSTORE,
  '__module__' : 'secret_store_types_pb2'
  # @@protoc_insertion_point(class_scope:v1.SecretStore)
  })
_sym_db.RegisterMessage(SecretStore)

AWSStore = _reflection.GeneratedProtocolMessageType('AWSStore', (_message.Message,), {
  'DESCRIPTOR' : _AWSSTORE,
  '__module__' : 'secret_store_types_pb2'
  # @@protoc_insertion_point(class_scope:v1.AWSStore)
  })
_sym_db.RegisterMessage(AWSStore)

AzureStore = _reflection.GeneratedProtocolMessageType('AzureStore', (_message.Message,), {
  'DESCRIPTOR' : _AZURESTORE,
  '__module__' : 'secret_store_types_pb2'
  # @@protoc_insertion_point(class_scope:v1.AzureStore)
  })
_sym_db.RegisterMessage(AzureStore)

VaultTLSStore = _reflection.GeneratedProtocolMessageType('VaultTLSStore', (_message.Message,), {
  'DESCRIPTOR' : _VAULTTLSSTORE,
  '__module__' : 'secret_store_types_pb2'
  # @@protoc_insertion_point(class_scope:v1.VaultTLSStore)
  })
_sym_db.RegisterMessage(VaultTLSStore)

VaultTokenStore = _reflection.GeneratedProtocolMessageType('VaultTokenStore', (_message.Message,), {
  'DESCRIPTOR' : _VAULTTOKENSTORE,
  '__module__' : 'secret_store_types_pb2'
  # @@protoc_insertion_point(class_scope:v1.VaultTokenStore)
  })
_sym_db.RegisterMessage(VaultTokenStore)


DESCRIPTOR._options = None
_SECRETSTORE.oneofs_by_name['secret_store']._options = None
_SECRETSTORE.fields_by_name['aws']._options = None
_SECRETSTORE.fields_by_name['azure']._options = None
_SECRETSTORE.fields_by_name['vault_tls']._options = None
_SECRETSTORE.fields_by_name['vault_token']._options = None
_SECRETSTORE._options = None
_AWSSTORE.fields_by_name['id']._options = None
_AWSSTORE.fields_by_name['name']._options = None
_AWSSTORE.fields_by_name['region']._options = None
_AWSSTORE.fields_by_name['tags']._options = None
_AWSSTORE._options = None
_AZURESTORE.fields_by_name['id']._options = None
_AZURESTORE.fields_by_name['name']._options = None
_AZURESTORE.fields_by_name['vault_uri']._options = None
_AZURESTORE.fields_by_name['tags']._options = None
_AZURESTORE._options = None
_VAULTTLSSTORE.fields_by_name['id']._options = None
_VAULTTLSSTORE.fields_by_name['name']._options = None
_VAULTTLSSTORE.fields_by_name['CA_cert_path']._options = None
_VAULTTLSSTORE.fields_by_name['client_cert_path']._options = None
_VAULTTLSSTORE.fields_by_name['client_key_path']._options = None
_VAULTTLSSTORE.fields_by_name['namespace']._options = None
_VAULTTLSSTORE.fields_by_name['server_address']._options = None
_VAULTTLSSTORE.fields_by_name['tags']._options = None
_VAULTTLSSTORE._options = None
_VAULTTOKENSTORE.fields_by_name['id']._options = None
_VAULTTOKENSTORE.fields_by_name['name']._options = None
_VAULTTOKENSTORE.fields_by_name['namespace']._options = None
_VAULTTOKENSTORE.fields_by_name['server_address']._options = None
_VAULTTOKENSTORE.fields_by_name['tags']._options = None
_VAULTTOKENSTORE._options = None
# @@protoc_insertion_point(module_scope)
