from ....logic._grpc.base import base_pb2 as _base_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("user_email", "user_password")
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    USER_PASSWORD_FIELD_NUMBER: _ClassVar[int]
    user_email: str
    user_password: str
    def __init__(self, user_email: _Optional[str] = ..., user_password: _Optional[str] = ...) -> None: ...

class JWTToken(_message.Message):
    __slots__ = ("access", "refresh")
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    access: str
    refresh: str
    def __init__(self, access: _Optional[str] = ..., refresh: _Optional[str] = ...) -> None: ...

class RefreshToken(_message.Message):
    __slots__ = ("refresh",)
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    refresh: str
    def __init__(self, refresh: _Optional[str] = ...) -> None: ...
