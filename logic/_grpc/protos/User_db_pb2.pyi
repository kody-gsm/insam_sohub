from logic._grpc.protos import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("user_email", "user_password")
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user_email: str
    user_password: str
    def __init__(self, user_email: _Optional[str] = ..., user_password: _Optional[str] = ...) -> None: ...

class EditUser(_message.Message):
    __slots__ = ("access_token", "user")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    access_token: _base_pb2.AccessToken
    user: User
    def __init__(self, access_token: _Optional[_Union[_base_pb2.AccessToken, _Mapping]] = ..., user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class RefreshToken(_message.Message):
    __slots__ = ("refresh",)
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    refresh: str
    def __init__(self, refresh: _Optional[str] = ...) -> None: ...

class ResponseJwtToken(_message.Message):
    __slots__ = ("access_token", "refresh_token", "response")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    REFRESH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    access_token: _base_pb2.AccessToken
    refresh_token: RefreshToken
    response: _base_pb2.Response
    def __init__(self, access_token: _Optional[_Union[_base_pb2.AccessToken, _Mapping]] = ..., refresh_token: _Optional[_Union[RefreshToken, _Mapping]] = ..., response: _Optional[_Union[_base_pb2.Response, _Mapping]] = ...) -> None: ...

class ResponseAccessToken(_message.Message):
    __slots__ = ("access_token", "response")
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    access_token: _base_pb2.AccessToken
    response: _base_pb2.Response
    def __init__(self, access_token: _Optional[_Union[_base_pb2.AccessToken, _Mapping]] = ..., response: _Optional[_Union[_base_pb2.Response, _Mapping]] = ...) -> None: ...
