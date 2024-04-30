from fastapi import WebSocket
from uuid import uuid4
sockets:dict[str, WebSocket] = {}

def get_uuid():
    return str(uuid4())
    