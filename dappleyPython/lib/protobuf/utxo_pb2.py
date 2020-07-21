# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: utxo.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='utxo.proto',
  package='utxopb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\nutxo.proto\x12\x06utxopb\"s\n\x04Utxo\x12\x0e\n\x06\x61mount\x18\x01 \x01(\x0c\x12\x17\n\x0fpublic_key_hash\x18\x02 \x01(\x0c\x12\x0c\n\x04txid\x18\x03 \x01(\x0c\x12\x10\n\x08tx_index\x18\x04 \x01(\r\x12\x10\n\x08utxoType\x18\x05 \x01(\r\x12\x10\n\x08\x63ontract\x18\x06 \x01(\t\"\'\n\x08UtxoList\x12\x1b\n\x05utxos\x18\x01 \x03(\x0b\x32\x0c.utxopb.Utxob\x06proto3'
)




_UTXO = _descriptor.Descriptor(
  name='Utxo',
  full_name='utxopb.Utxo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='amount', full_name='utxopb.Utxo.amount', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_key_hash', full_name='utxopb.Utxo.public_key_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='txid', full_name='utxopb.Utxo.txid', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_index', full_name='utxopb.Utxo.tx_index', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='utxoType', full_name='utxopb.Utxo.utxoType', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract', full_name='utxopb.Utxo.contract', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=22,
  serialized_end=137,
)


_UTXOLIST = _descriptor.Descriptor(
  name='UtxoList',
  full_name='utxopb.UtxoList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='utxos', full_name='utxopb.UtxoList.utxos', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=139,
  serialized_end=178,
)

_UTXOLIST.fields_by_name['utxos'].message_type = _UTXO
DESCRIPTOR.message_types_by_name['Utxo'] = _UTXO
DESCRIPTOR.message_types_by_name['UtxoList'] = _UTXOLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Utxo = _reflection.GeneratedProtocolMessageType('Utxo', (_message.Message,), {
  'DESCRIPTOR' : _UTXO,
  '__module__' : 'utxo_pb2'
  # @@protoc_insertion_point(class_scope:utxopb.Utxo)
  })
_sym_db.RegisterMessage(Utxo)

UtxoList = _reflection.GeneratedProtocolMessageType('UtxoList', (_message.Message,), {
  'DESCRIPTOR' : _UTXOLIST,
  '__module__' : 'utxo_pb2'
  # @@protoc_insertion_point(class_scope:utxopb.UtxoList)
  })
_sym_db.RegisterMessage(UtxoList)


# @@protoc_insertion_point(module_scope)
