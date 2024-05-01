from fastapi import APIRouter, WebSocket, Request
from logic._grpc.grpc_pot import GRPC_Pot
from logic._grpc.protos import base_pb2
from logic._grpc.protos import Pot_db_pb2
from logic._grpc import utils
from grpc._channel import _InactiveRpcError
import asyncio

router = APIRouter(
    prefix="/cam"
)


@router.websocket("/{pot_code}")
async def connect_pot(pot_code:str, request:Request, websocket:WebSocket):
    await websocket.accept()
    try:
        grpc_response:Pot_db_pb2.ResponsePot = GRPC_Pot().pot_read(await websocket.receive_text(), pot_code)
    except _InactiveRpcError:
        await websocket.close(reason="gRPC server is cot connect")

    status_code, message = utils.check_status_code(grpc_response.response)

    # if status_code // 100 != 2:
    #     await websocket.close(reason=message)
    
    # await msg_queue[pot_code].send_text("s4stream")

    # async def send_cam():
    #     while True:
    #         await websocket.send(msg_queue[pot_code].receive_text())
            
    # task = asyncio.create_task(send_cam())
    # while True:
    #     if "s4stop" == await websocket.receive_text():
    #         task.cancel()
    #         await msg_queue[pot_code].send_text("s4stop")
    #         await websocket.close()
            