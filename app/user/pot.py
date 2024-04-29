from fastapi import APIRouter, WebSocket, Request
from fastapi.responses import JSONResponse as HTTP_Response
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
    if not "access_token" in request.headers:
        return HTTP_Response(content={}, status_code=403)
    grpc_response:base_pb2.Response = GRPC_UserPot().user_add_pot(token=request.headers["access_token"], 
                              pot_code=body.code, 
                              pot_name=body.name)
    htc = grpc_response.http_code.split("/")
    status_code = htc[0]
    if len(htc) == 2:
        message = htc[1]
        return HTTP_Response(content={"message":message}, status_code=int(status_code))
    return HTTP_Response(content={}, status_code=int(status_code))


@router.post("/update")
def user_update_pot(request:Request, body:PotBody):
    if not "access_token" in request.headers:
        return HTTP_Response(content={}, status_code=403)
    grpc_response:base_pb2.Response = GRPC_Pot().pot_update(token=request.headers["access_token"],
                              pot_code=body.code, 
                              pot_name=body.name)
    htc = grpc_response.http_code.split("/")
    status_code = htc[0]
    if len(htc) == 2:
        message = htc[1]
        return HTTP_Response(content={"message":message}, status_code=int(status_code))
    return HTTP_Response(content={}, status_code=int(status_code))


@router.post("/remove")
def user_remove_pot(request:Request, body:PotBody):
    if not "access_token" in request.headers:
        return HTTP_Response(content={}, status_code=403)
    grpc_response:base_pb2.Response = GRPC_UserPot().user_remove_pot(token=request.headers["access_token"], 
                              pot_code=body.code, 
                              pot_name=body.name)
    htc = grpc_response.http_code.split("/")
    status_code = htc[0]
    if len(htc) == 2:
        message = htc[1]
        return HTTP_Response(content={"message":message}, status_code=int(status_code))
    return HTTP_Response(content={}, status_code=int(status_code))

@router.get("/read")
def user_remove_pot(request:Request):
    if not "access_token" in request.headers:
        return HTTP_Response(content={}, status_code=403)
    grpc_response = GRPC_UserPot().user_read_pot_list(token=request.headers["access_token"])
    def r(li, pot:Pot_db_pb2.ResponsePot):
        htc = pot.response.http_code.split("/")
        status_code = htc[0]
        if len(htc) == 2:
            message = htc[1]
            return li
        is_active = False
        if pot.pot.pot_code in pot_connections:
            is_active = True
        return li + [{"pot_code":pot.pot.pot_code, "pot_name":pot.pot.pot_name, "is_active":is_active}]
    from functools import reduce
    return HTTP_Response(content=reduce(r, grpc_response, []))
        

async def get_info(websocket:WebSocket, func_code:str):
    await websocket.send_text(func_code)
    return await websocket.receive_text()

@router.websocket("/{pot_code}")
async def pot_info(websocket:WebSocket, pot_code:str):
    print("whaat")
    if not pot_code in pot_connections:
        raise "화분 연결 x"
    await websocket.accept() 
    # grpc_response:Pot_db_pb2.ResponsePot = GRPC_Pot().pot_read(await websocket.receive_text(), pot_code)
    # htc = grpc_response.response.http_code.split("/")
    # status_code = htc[0]
    # if len(htc) == 2:
    #     message = htc[1]
    #     websocket.close(reason=F"{status_code}:{message}")
    #     return
    while True:
        func_code = await websocket.receive_text()
        if func_code == "exit":
            websocket.close()
            return
        await websocket.send_text(await get_info(pot_connections[pot_code], func_code))