# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: block.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import transaction_pb2 as transaction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='block.proto',
  package='blockpb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0b\x62lock.proto\x12\x07\x62lockpb\x1a\x11transaction.proto\"t\n\x05\x42lock\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.blockpb.BlockHeader\x12\x30\n\x0ctransactions\x18\x02 \x03(\x0b\x32\x1a.transactionpb.Transaction\x12\x13\n\x0bparent_hash\x18\x03 \x01(\x0c\"\x89\x01\n\x0b\x42lockHeader\x12\x0c\n\x04hash\x18\x01 \x01(\x0c\x12\x15\n\rprevious_hash\x18\x02 \x01(\x0c\x12\r\n\x05nonce\x18\x03 \x01(\x03\x12\x11\n\ttimestamp\x18\x04 \x01(\x03\x12\x11\n\tsignature\x18\x05 \x01(\x0c\x12\x0e\n\x06height\x18\x06 \x01(\x04\x12\x10\n\x08producer\x18\x07 \x01(\tb\x06proto3'
  ,
  dependencies=[transaction__pb2.DESCRIPTOR,])




_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blockpb.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='blockpb.Block.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transactions', full_name='blockpb.Block.transactions', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent_hash', full_name='blockpb.Block.parent_hash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=43,
  serialized_end=159,
)


_BLOCKHEADER = _descriptor.Descriptor(
  name='BlockHeader',
  full_name='blockpb.BlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='blockpb.BlockHeader.hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='previous_hash', full_name='blockpb.BlockHeader.previous_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='blockpb.BlockHeader.nonce', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='blockpb.BlockHeader.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='blockpb.BlockHeader.signature', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='blockpb.BlockHeader.height', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='producer', full_name='blockpb.BlockHeader.producer', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=162,
  serialized_end=299,
)

_BLOCK.fields_by_name['header'].message_type = _BLOCKHEADER
_BLOCK.fields_by_name['transactions'].message_type = transaction__pb2._TRANSACTION
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['BlockHeader'] = _BLOCKHEADER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), {
  'DESCRIPTOR' : _BLOCK,
  '__module__' : 'block_pb2'
  # @@protoc_insertion_point(class_scope:blockpb.Block)
  })
_sym_db.RegisterMessage(Block)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), {
  'DESCRIPTOR' : _BLOCKHEADER,
  '__module__' : 'block_pb2'
  # @@protoc_insertion_point(class_scope:blockpb.BlockHeader)
  })
_sym_db.RegisterMessage(BlockHeader)


# @@protoc_insertion_point(module_scope)