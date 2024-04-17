from logic._grpc.protos import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Pot(_message.Message):
    __slots__ = ("pot_code", "pot_name")
    POT_CODE_FIELD_NUMBER: _ClassVar[int]
    POT_NAME_FIELD_NUMBER: _ClassVar[int]
    pot_code: str
    pot_name: str
    def __init__(self, pot_code: _Optional[str] = ..., pot_name: _Optional[str] = ...) -> None: ...

class ResponsePot(_message.Message):
    __slots__ = ("pot", "response")
    POT_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    pot: Pot
    response: _base_pb2.Response
    def __init__(self, pot: _Optional[_Union[Pot, _Mapping]] = ..., response: _Optional[_Union[_base_pb2.Response, _Mapping]] = ...) -> None: ...

class CertifiedPot(_message.Message):
    __slots__ = ("access_token", "pot")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    POT_FIELD_NUMBER: _ClassVar[int]
    access_token: _base_pb2.AccessToken
    pot: Pot
    def __init__(self, access_token: _Optional[_Union[_base_pb2.AccessToken, _Mapping]] = ..., pot: _Optional[_Union[Pot, _Mapping]] = ...) -> None: ...
