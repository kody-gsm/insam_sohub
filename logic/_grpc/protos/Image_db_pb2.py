# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: logic/_grpc/protos/Image_db.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from logic._grpc.protos import base_pb2 as logic_dot___grpc_dot_protos_dot_base__pb2
from logic._grpc.protos import Pot_db_pb2 as logic_dot___grpc_dot_protos_dot_Pot__db__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!logic/_grpc/protos/Image_db.proto\x1a\x1dlogic/_grpc/protos/base.proto\x1a\x1flogic/_grpc/protos/Pot_db.proto\"A\n\x05Image\x12\x10\n\x08image_id\x18\x01 \x01(\t\x12\x12\n\nimage_file\x18\x02 \x01(\t\x12\x12\n\nimage_time\x18\x03 \x01(\t\"C\n\rResponseImage\x12\x15\n\x05image\x18\x01 \x01(\x0b\x32\x06.Image\x12\x1b\n\x08response\x18\x02 \x01(\x0b\x32\t.Response\"^\n\x0e\x43\x65rtifiedImage\x12\"\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\x0b\x32\x0c.AccessToken\x12\x11\n\x03pot\x18\x02 \x01(\x0b\x32\x04.Pot\x12\x15\n\x05image\x18\x03 \x01(\x0b\x32\x06.Image2\xc9\x01\n\x0cImageTraffic\x12*\n\x0cimage_create\x12\x0f.CertifiedImage\x1a\t.Response\x12*\n\x0cimage_delete\x12\x0f.CertifiedImage\x1a\t.Response\x12-\n\nimage_read\x12\x0f.CertifiedImage\x1a\x0e.ResponseImage\x12\x32\n\x0fimage_read_list\x12\r.CertifiedPot\x1a\x0e.ResponseImage0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'logic._grpc.protos.Image_db_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_IMAGE']._serialized_start=101
  _globals['_IMAGE']._serialized_end=166
  _globals['_RESPONSEIMAGE']._serialized_start=168
  _globals['_RESPONSEIMAGE']._serialized_end=235
  _globals['_CERTIFIEDIMAGE']._serialized_start=237
  _globals['_CERTIFIEDIMAGE']._serialized_end=331
  _globals['_IMAGETRAFFIC']._serialized_start=334
  _globals['_IMAGETRAFFIC']._serialized_end=535
# @@protoc_insertion_point(module_scope)
