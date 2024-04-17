from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Response(_message.Message):
    __slots__ = ("http_code",)
    HTTP_CODE_FIELD_NUMBER: _ClassVar[int]
    http_code: str
    def __init__(self, http_code: _Optional[str] = ...) -> None: ...

class AccessToken(_message.Message):
    __slots__ = ("access",)
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    access: str
    def __init__(self, access: _Optional[str] = ...) -> None: ...
