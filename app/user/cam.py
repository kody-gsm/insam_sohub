from fastapi import APIRouter, WebSocket, Request
from ...logic._grpc.grpc_pot import GRPC_Pot
from ...logic._grpc.protos import base_pb2
from ..pot.pot import pot_connections
import time

router = APIRouter(
    prefix="/cam"
)


@router.websocket("/{pot_code}")
async def connect_pot(pot_code:str, request:Request, websocket:WebSocket):
    grpc_response:base_pb2.Response = GRPC_Pot.pot_read(request.cookies["access_token"])
    if not grpc_response.check:
        raise "권한 x"
    if not pot_code in pot_connections:
        raise "화분 연결 x"
    GRPC_Pot.pot_create(pot_code=websocket.headers["pot_code"])
    await websocket.accept()

    async def get_cam(websocket:WebSocket):
        await websocket.send("cam")
        return await websocket.receive_text()
    
    while True:
        await websocket.send(get_cam(pot_connections[pot_code]))
        time.sleep(1)

    