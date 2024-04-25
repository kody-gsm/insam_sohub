from fastapi import APIRouter, WebSocket, Request
from logic._grpc.grpc_pot import GRPC_Pot
from logic._grpc.protos import base_pb2
from logic._grpc.protos import Pot_db_pb2
from app.pot.pot import pot_connections
import time
import asyncio

router = APIRouter(
    prefix="/cam"
)


@router.websocket("/{pot_code}")
async def connect_pot(pot_code:str, request:Request, websocket:WebSocket):
    if not "access_token" in request.headers:
        raise "권한 x"
    grpc_response:Pot_db_pb2.ResponsePot = GRPC_Pot().pot_read(request.headers["access_token"])
    htc = grpc_response.response.http_code.split("/")
    status_code = htc[0]
    if len(htc) == 2:
        message = htc[1]
        raise message
    if not pot_code in pot_connections:
        raise "화분 연결 x"
    await websocket.accept()
    
    await pot_connections[pot_code].send_text("s4stream")

    async def send_cam():
        while True:
            await websocket.send(pot_connections[pot_code].receive_text())
    task = asyncio.create_task(send_cam())
    while True:
        if "s4stop" == await websocket.receive_text():
            task.cancel()
            await pot_connections[pot_code].send_text("s4stop")
            await websocket.close()
            