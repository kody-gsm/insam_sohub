from fastapi import APIRouter, Body, Header
from fastapi.responses import JSONResponse as HTTP_Response
from pydantic import BaseModel
from logic._grpc.grpc_user import GRPC_User
from logic._grpc.protos import base_pb2, User_db_pb2
from logic._grpc import utils
from grpc._channel import _InactiveRpcError
from typing import Annotated
 
router = APIRouter(
    prefix="/account"
)

class UserBody(BaseModel):
    email:str
    password:str

@router.post("/sign-up")
def post_sign_up(body:UserBody):
    try:
        grpc_response:base_pb2.Response = GRPC_User().user_create(body.email, body.password)
    except _InactiveRpcError:
        return HTTP_Response(content={"message":"gRPC server is cot connect"}, status_code=500)
    
    status_code, message = utils.check_status_code(grpc_response)

    if status_code // 100 == 2:
        content = {"message":"success"}
    else:
        content = {"message":message}

    return HTTP_Response(content=content, status_code=status_code)

@router.post("/login")
def post_login(body:UserBody):
    try:
        grpc_response:User_db_pb2.ResponseJwtToken = GRPC_User().user_login(body.email, body.password)
    except _InactiveRpcError:
        return HTTP_Response(content={"message":"gRPC server is cot connect"}, status_code=500)
    
    status_code, message = utils.check_status_code(grpc_response)

    if status_code // 100 == 2:
        content = {"refresh_token":grpc_response.refresh_token.refresh, 
                    "access_token":grpc_response.access_token.access}
    else:
        content = {"message":message}

    return HTTP_Response(content=content, status_code=status_code)

@router.post("/refresh")
def refresh(refresh=Body(Annotated[str, None])):
    # 예외 처리
    if not refresh:
        return HTTP_Response(content={"message":"token does not exist"}, status_code=403)
    try:
        grpc_response:User_db_pb2.ResponseAccessToken = GRPC_User().refresh_token(refresh)
    except _InactiveRpcError:
        return HTTP_Response(content={"message":"gRPC server is cot connect"}, status_code=500)

    status_code, message = utils.check_status_code(grpc_response)

    if status_code // 100 == 2:
        content = {"access_token":grpc_response.access_token.access}
    else:
        content = {"message":message}

    return HTTP_Response(content=content, status_code=status_code)

@router.post("/password")
def password(body:UserBody):
    try:
        grpc_response:base_pb2.Response = GRPC_User().password_update(body.email, body.password)
    except _InactiveRpcError:
        return HTTP_Response(content={"message":"gRPC server is cot connect"}, status_code=500)
    
    status_code, message = utils.check_status_code(grpc_response)

    if status_code // 100 == 2:
        content = {"message":"success"}
    else:
        content = {"message":message}

    return HTTP_Response(content=content, status_code=status_code)