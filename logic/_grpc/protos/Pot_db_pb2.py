# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logic/_grpc/protos/Pot_db.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from logic._grpc.protos import base_pb2 as logic_dot___grpc_dot_protos_dot_base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1flogic/_grpc/protos/Pot_db.proto\x1a\x1dlogic/_grpc/protos/base.proto\")\n\x03Pot\x12\x10\n\x08pot_code\x18\x01 \x01(\t\x12\x10\n\x08pot_name\x18\x02 \x01(\t\"=\n\x0bResponsePot\x12\x11\n\x03pot\x18\x01 \x01(\x0b\x32\x04.Pot\x12\x1b\n\x08response\x18\x02 \x01(\x0b\x32\t.Response\"E\n\x0c\x43\x65rtifiedPot\x12\"\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\x0b\x32\x0c.AccessToken\x12\x11\n\x03pot\x18\x02 \x01(\x0b\x32\x04.Pot2\xd2\x01\n\nPotTraffic\x12\x1d\n\npot_create\x12\x04.Pot\x1a\t.Response\x12&\n\npot_delete\x12\r.CertifiedPot\x1a\t.Response\x12&\n\npot_update\x12\r.CertifiedPot\x1a\t.Response\x12&\n\x08pot_read\x12\x0c.AccessToken\x1a\x0c.ResponsePot\x12-\n\rpot_read_list\x12\x0c.AccessToken\x1a\x0c.ResponsePot0\x01\x32\x9b\x01\n\x0eUserPotTraffic\x12(\n\x0cuser_add_pot\x12\r.CertifiedPot\x1a\t.Response\x12+\n\x0fuser_remove_pot\x12\r.CertifiedPot\x1a\t.Response\x12\x32\n\x12user_read_pot_list\x12\x0c.AccessToken\x1a\x0c.ResponsePot0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'logic._grpc.protos.Pot_db_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_POT']._serialized_start=66
  _globals['_POT']._serialized_end=107
  _globals['_RESPONSEPOT']._serialized_start=109
  _globals['_RESPONSEPOT']._serialized_end=170
  _globals['_CERTIFIEDPOT']._serialized_start=172
  _globals['_CERTIFIEDPOT']._serialized_end=241
  _globals['_POTTRAFFIC']._serialized_start=244
  _globals['_POTTRAFFIC']._serialized_end=454
  _globals['_USERPOTTRAFFIC']._serialized_start=457
  _globals['_USERPOTTRAFFIC']._serialized_end=612
# @@protoc_insertion_point(module_scope)
