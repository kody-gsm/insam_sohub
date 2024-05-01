from fastapi import APIRouter, WebSocket, Request, Header
from fastapi.responses import JSONResponse as HTTP_Response
from pydantic import BaseModel
from logic._grpc.grpc_user_pot import GRPC_UserPot
from logic._grpc.grpc_pot import GRPC_Pot
from logic._grpc.protos import base_pb2, Pot_db_pb2
from logic._grpc import utils
from grpc._channel import _InactiveRpcError
import time
from logic.socket import connect_socket

router =APIRouter(
    prefix="/pot"
)

class PotBody(BaseModel):
    code:str
    name:str|None = None

@router.post("/add")
def user_add_pot(request:Request, body:PotBody, access_token:str|None = Header(default=None)):
    if not access_token:
        return HTTP_Response(content={"message", "token does not exist"}, status_code=403)
    
    try:
        grpc_response:base_pb2.Response = GRPC_UserPot().user_add_pot(token=access_token, 
                              pot_code=body.code, 
                              pot_name=body.name)
    except _InactiveRpcError:
        return HTTP_Response(content={"message":"gRPC server is cot connect"}, status_code=500)
    
    status_code, message = utils.check_status_code(grpc_response)

    if status_code // 100 == 2:
        content = {"message":"success"}
    else:
        content = {"message":message}

    return HTTP_Response(content=content, status_code=status_code)

@router.post("/update")
def user_update_pot(request:Request, body:PotBody, access_token:str|None = Header(default=None)):
    if not access_token:
        return HTTP_Response(content={"message", "token does not exist"}, status_code=403)
    
    try:
        grpc_response:base_pb2.Response = GRPC_Pot().pot_update(token=access_token,
                              pot_code=body.code, 
                              pot_name=body.name)
    except _InactiveRpcError:
        return HTTP_Response(content={"message":"gRPC server is cot connect"}, status_code=500)

    status_code, message = utils.check_status_code(grpc_response)

    if status_code // 100 == 2:
        content = {"message":"success"}
    else:
        content = {"message":message}

    return HTTP_Response(content=content, status_code=status_code)


@router.post("/remove")
def user_remove_pot(request:Request, body:PotBody, access_token:str|None = Header(default=None)):
    if not access_token:
        return HTTP_Response(content={"message", "token does not exist"}, status_code=403)
    try:
        grpc_response:base_pb2.Response = GRPC_UserPot().user_remove_pot(token=access_token, 
                              pot_code=body.code, 
                              pot_name=body.name)
    except _InactiveRpcError:
        return HTTP_Response(content={"message":"gRPC server is cot connect"}, status_code=500)
    
    status_code, message = utils.check_status_code(grpc_response)

    if status_code // 100 == 2:
        content = {"message":"success"}
    else:
        content = {"message":message}

    return HTTP_Response(content=content, status_code=status_code)

@router.get("/read")
def user_remove_pot(request:Request, access_token:str|None = Header(default=None)):
    if not access_token:
        return HTTP_Response(content={"message", "token does not exist"}, status_code=403)
    
    try:
        grpc_response = GRPC_UserPot().user_read_pot_list(token=access_token)
    except _InactiveRpcError:
        return HTTP_Response(content={"message":"gRPC server is cot connect"}, status_code=500)

    def r(li, pot:Pot_db_pb2.ResponsePot):
        status_code, message = utils.check_status_code(pot.response)
        if status_code // 100 != 2:
            return li
        is_active = False
        if pot.pot.pot_code in connect_socket.sockets:
            is_active = True
        return li + [{"pot_code":pot.pot.pot_code, "pot_name":pot.pot.pot_name, "is_active":is_active}]
    
    from functools import reduce
    return HTTP_Response(content=reduce(r, grpc_response, []))
        

async def get_info(websocket:WebSocket, func_code:str):
    await websocket.send_text(func_code)
    return await websocket.receive_text()

@router.websocket("/{pot_code}")
async def pot_info(websocket:WebSocket, pot_code:str):
    await websocket.accept() 

    try:
        grpc_response:Pot_db_pb2.ResponsePot = GRPC_Pot().pot_read(await websocket.receive_text(), pot_code)
    except _InactiveRpcError:
        return await websocket.close(reason="gRPC server is cot connect")

    status_code, message = utils.check_status_code(grpc_response.response)

    if status_code // 100 != 2:
        return await websocket.close(reason=message)

    id = connect_socket.get_uuid()
    connect_socket.sockets[id] = websocket

    try:
        while True:
            func_code = await websocket.receive_text()
            if func_code == "exit":
                return await websocket.close()
            
            if not pot_code in connect_socket.sockets:
                return await websocket.close(reason="화분 연결 x")
            
            await connect_socket.sockets[pot_code].send_text(f"{id}#{func_code}")
    finally:
        connect_socket.sockets.pop(id)