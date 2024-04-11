from fastapi import APIRouter, Request, Response as HTTP_Response, WebSocket
from pydantic import BaseModel
from ...logic._grpc.grpc_user_pot import GRPC_UserPot
from ...logic._grpc.grpc_pot import GRPC_Pot
from ...logic._grpc.protos import base_pb2
from ...logic._grpc.grpc_pot import GRPC_Pot
from ..pot.pot import pot_connections
import time

router =APIRouter(
    prefix="/pot"
)

class PotBody(BaseModel):
    code:str
    name:str|None = None

@router.post("/add")
def user_add_pot(request:Request, body:PotBody):
    grpc_response:base_pb2.Response = GRPC_UserPot.user_add_pot(token=request.cookies["access_token"], 
                              pot_code=body.code, 
                              pot_name=body.name)
    if not grpc_response.check:
        return HTTP_Response({"message":"fail"}, 400)
    return HTTP_Response({"message":"success"}, 200)

@router.post("/add")
def user_update_pot(request:Request, body:PotBody):
    grpc_response:base_pb2.Response = GRPC_Pot.pot_update(token=request.cookies["access_token"], 
                              pot_code=body.code, 
                              pot_name=body.name)
    if not grpc_response.check:
        return HTTP_Response({"message":"fail"}, 400)
    return HTTP_Response({"message":"success"}, 200)

@router.post("/remove")
def user_remove_pot(request:Request, body:PotBody):
    grpc_response:base_pb2.Response = GRPC_UserPot.user_remove_pot(token=request.cookies["access_token"], 
                              pot_code=body.code, 
                              pot_name=body.name)
    if not grpc_response.check:
        return HTTP_Response({"message":"fail"}, 400)
    return HTTP_Response({"message":"success"}, 200)

@router.get("/read")
def user_remove_pot(request:Request):
    grpc_response = GRPC_UserPot.user_read_pot_list(token=request.cookies["access_token"])
    
    # 예외처리 x
    # if not grpc_response:
    #     return HTTP_Response({"message":"fail"}, 400)

    return HTTP_Response({"pot":list(grpc_response)}, 200)

async def get_info(websocket:WebSocket):
    await websocket.send("cam")
    return await websocket.receive_text()

@router.websocket("/cam/{pot_code}")
async def connect_pot(pot_code:str, request:Request, websocket:WebSocket):
    grpc_response:base_pb2.Response = GRPC_Pot.pot_read(request.cookies["access_token"])
    if not grpc_response.check:
        raise "권한 x"
    if not pot_code in pot_connections:
        raise "화분 연결 x"
    await websocket.accept()
    while True:
        await websocket.send(get_info(pot_connections[pot_code]))
        time.sleep(1)

@router.get("/{func_code}/{pot_code}")
async def pot_info(request:Request, websocket:WebSocket, func_code:str, pot_code:str):
    grpc_response:base_pb2.Response = GRPC_Pot.pot_read(request.cookies["access_token"])
    if not grpc_response.check:
        raise "권한 x"
    if not pot_code in pot_connections:
        raise "화분 연결 x"
    socket_resoponse = await websocket.send(get_info(pot_connections[pot_code]))
    return HTTP_Response({"info":socket_resoponse}, 200)