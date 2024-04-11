# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: User_db.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import base_pb2 as base__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rUser_db.proto\x1a\nbase.proto\"1\n\x04User\x12\x12\n\nuser_email\x18\x01 \x01(\t\x12\x15\n\ruser_password\x18\x02 \x01(\t\"C\n\x08\x45\x64itUser\x12\"\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\x0b\x32\x0c.AccessToken\x12\x13\n\x04user\x18\x02 \x01(\x0b\x32\x05.User\"\x1f\n\x0cRefreshToken\x12\x0f\n\x07refresh\x18\x01 \x01(\t\"y\n\x10ResponseJwtToken\x12\"\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\x0b\x32\x0c.AccessToken\x12$\n\rrefresh_token\x18\x02 \x01(\x0b\x32\r.RefreshToken\x12\x1b\n\x08response\x18\x03 \x01(\x0b\x32\t.Response\"V\n\x13ResponseAccessToken\x12\"\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\x0b\x32\x0c.AccessToken\x12\x1b\n\x08response\x18\x02 \x01(\x0b\x32\t.Response2\xf6\x01\n\x0bUserTraffic\x12\x1f\n\x0buser_create\x12\x05.User\x1a\t.Response\x12#\n\x0buser_delete\x12\t.EditUser\x1a\t.Response\x12&\n\nuser_login\x12\x05.User\x1a\x11.ResponseJwtToken\x12\x34\n\rrefresh_token\x12\r.RefreshToken\x1a\x14.ResponseAccessToken\x12\x1e\n\nemail_find\x12\x05.User\x1a\t.Response\x12#\n\x0fpassword_update\x12\x05.User\x1a\t.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'User_db_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=29
  _globals['_USER']._serialized_end=78
  _globals['_EDITUSER']._serialized_start=80
  _globals['_EDITUSER']._serialized_end=147
  _globals['_REFRESHTOKEN']._serialized_start=149
  _globals['_REFRESHTOKEN']._serialized_end=180
  _globals['_RESPONSEJWTTOKEN']._serialized_start=182
  _globals['_RESPONSEJWTTOKEN']._serialized_end=303
  _globals['_RESPONSEACCESSTOKEN']._serialized_start=305
  _globals['_RESPONSEACCESSTOKEN']._serialized_end=391
  _globals['_USERTRAFFIC']._serialized_start=394
  _globals['_USERTRAFFIC']._serialized_end=640
# @@protoc_insertion_point(module_scope)
