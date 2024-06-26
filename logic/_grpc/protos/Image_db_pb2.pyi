from logic._grpc.protos import base_pb2 as _base_pb2
from logic._grpc.protos import Pot_db_pb2 as _Pot_db_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Image(_message.Message):
    __slots__ = ("image_id", "image_file", "image_time")
    IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FILE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TIME_FIELD_NUMBER: _ClassVar[int]
    image_id: str
    image_file: str
    image_time: str
    def __init__(self, image_id: _Optional[str] = ..., image_file: _Optional[str] = ..., image_time: _Optional[str] = ...) -> None: ...

class ResponseImage(_message.Message):
    __slots__ = ("image", "response")
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    image: Image
    response: _base_pb2.Response
    def __init__(self, image: _Optional[_Union[Image, _Mapping]] = ..., response: _Optional[_Union[_base_pb2.Response, _Mapping]] = ...) -> None: ...

class CertifiedImage(_message.Message):
    __slots__ = ("access_token", "pot", "image")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    POT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    access_token: _base_pb2.AccessToken
    pot: _Pot_db_pb2.Pot
    image: Image
    def __init__(self, access_token: _Optional[_Union[_base_pb2.AccessToken, _Mapping]] = ..., pot: _Optional[_Union[_Pot_db_pb2.Pot, _Mapping]] = ..., image: _Optional[_Union[Image, _Mapping]] = ...) -> None: ...
