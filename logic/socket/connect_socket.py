from fastapi import WebSocket
from uuid import uuid4
pot_sockets:dict[str, WebSocket] = {}
client_sockets:dict[str, WebSocket] = {}

def get_uuid():
    return str(uuid4())
    