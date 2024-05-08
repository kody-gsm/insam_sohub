from fastapi import APIRouter, WebSocket
from logic._grpc.grpc_pot import GRPC_Pot
from logic._grpc.protos import User_db_pb2
from logic._grpc.grpc_image import GRPC_Image
from logic._grpc.grpc_user import GRPC_User
import os
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

    connect_socket.pot_sockets[pot_code] = websocket

    try:
        while True:
            recive_data = await websocket.receive_text()

            if recive_data == "exit":
                return await websocket.close()
            
            id, data = recive_data.split("#")
            if id == "server":
                code, data = data.split(":", 1)
                if code == "s4":
                    try:
                        grpc_response:User_db_pb2.ResponseJwtToken = GRPC_User().user_login(email=os.environ.get("SERVER_ID"), password=os.environ.get("SERVER_PASSWORD"))
                        GRPC_Image().image_create(token=grpc_response.access_token.access, pot_code=pot_code, pot_name=None, image_file=data)
                    except _InactiveRpcError:
                        return await websocket.close(reason="gRPC server is cot connect")
            
            if not id in connect_socket.client_sockets:
                pass # client 연결 x
            else:
                await connect_socket.client_sockets[id].send_text(f"{data}")
    finally:
        connect_socket.pot_sockets.pop(pot_code)

