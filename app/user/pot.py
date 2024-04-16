from fastapi import APIRouter, Request, Response as HTTP_Response, WebSocket
from pydantic import BaseModel
from logic._grpc.grpc_user_pot import GRPC_UserPot
from logic._grpc.grpc_pot import GRPC_Pot
from logic._grpc.protos import base_pb2
from logic._grpc.protos import Pot_db_pb2
from app.pot.pot import pot_connections
import time

router =APIRouter(
    prefix="/pot"
)

class PotBody(BaseModel):
    code:str
    name:str|None = None

@router.post("/add")
def user_add_pot(request:Request, body:PotBody):
    grpc_response:base_pb2.Response = GRPC_UserPot().user_add_pot(token=request.cookies["access_token"], 
                              pot_code=body.code, 
                              pot_name=body.name)
    return HTTP_Response(status_code=int(grpc_response.http_code))


@router.post("/add")
def user_update_pot(request:Request, body:PotBody):
    grpc_response:base_pb2.Response = GRPC_Pot().pot_update(token=request.cookies["access_token"], 
                              pot_code=body.code, 
                              pot_name=body.name)
    return HTTP_Response(status_code=int(grpc_response.http_code))

@router.post("/remove")
def user_remove_pot(request:Request, body:PotBody):
    grpc_response:base_pb2.Response = GRPC_UserPot().user_remove_pot(token=request.cookies["access_token"], 
                              pot_code=body.code, 
                              pot_name=body.name)
    return HTTP_Response(status_code=int(grpc_response.http_code))

@router.get("/read")
def user_remove_pot(request:Request):
    grpc_response = GRPC_UserPot().user_read_pot_list(token=request.cookies["access_token"])
    def r(li, pot:Pot_db_pb2.ResponsePot):
        if int(pot.response.http_code) // 100 != 2:
            return li
        return li + [{"pot_code":pot.pot.pot_code, "pot_name":pot.pot.pot_name}]
    from functools import reduce
    return HTTP_Response(content=reduce(r, grpc_response, []))
        

async def get_info(websocket:WebSocket, func_code:str):
    await websocket.send(func_code)
    return await websocket.receive_text()

@router.get("/{pot_code}")
async def pot_info(request:Request, websocket:WebSocket, pot_code:str):
    grpc_response:Pot_db_pb2.ResponsePot = GRPC_Pot().pot_read(request.cookies["access_token"])
    if int(grpc_response.response.http_code) == 403:
        raise "권한 x"
    if not pot_code in pot_connections:
        raise "화분 연결 x"
    while True:
        await websocket.send(get_info(pot_connections[pot_code], await websocket.receive_text()))