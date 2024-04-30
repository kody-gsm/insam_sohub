from fastapi import APIRouter, WebSocket
from logic._grpc.grpc_pot import GRPC_Pot
import asyncio
from grpc._channel import _InactiveRpcError
from uuid import uuid4
from logic.socket import connect_socket
from logic._grpc import utils

router = APIRouter(
    prefix=""
)
    
@router.websocket("/connect")
async def connect_pot(websocket:WebSocket):
    await websocket.accept()
    pot_code = websocket.headers["pot_code"]

    try:
        GRPC_Pot().pot_create(pot_code=pot_code)
    except _InactiveRpcError:
        return await websocket.close(reason="gRPC server is cot connect")

    connect_socket.sockets[pot_code] = websocket

    try:
        while True:
            recive_data = await websocket.receive_text()

            if recive_data == "exit":
                return await websocket.close()
            
            id, data = recive_data.split("#")
            
            if not id in connect_socket.sockets:
                return await websocket.close(reason="화분 연결 x")
            
            await connect_socket.sockets[id].send_text(f"{data}")
    finally:
        connect_socket.sockets.pop(pot_code)

