from fastapi import APIRouter, Request, Body
from fastapi.responses import JSONResponse as HTTP_Response
from pydantic import BaseModel
from logic._grpc.grpc_user import GRPC_User
from logic._grpc.protos import base_pb2, User_db_pb2
from typing import Annotated
 
router = APIRouter(
    prefix="/account"
)

class UserBody(BaseModel):
    email:str
    password:str

@router.post("/sign-up")
def post_sign_up(body:UserBody):
    response:base_pb2.Response = GRPC_User().user_create(body.email, body.password)

    htc = response.http_code.split("/")
    status_code = htc[0]
    if len(htc) == 2:
        message = htc[1]
        return HTTP_Response(content={"message":message}, status_code=int(status_code))
    print("what", status_code)
    return HTTP_Response(content={}, status_code=int(status_code))

@router.post("/login")
def post_login(body:UserBody):
    token:User_db_pb2.ResponseJwtToken = GRPC_User().user_login(body.email, body.password)
    htc = token.response.http_code.split("/")
    status_code = htc[0]
    if len(htc) == 2:
        message = htc[1]
        return HTTP_Response(content={"message":message}, status_code=int(status_code))
    response = HTTP_Response(content={"refresh_token":token.refresh_token.refresh}, status_code=int(status_code))
    response.set_cookie("access_token", token.access_token.access)
    return response

@router.post("/refresh")
def refresh(refresh=Body(Annotated[str, None])):
    if not refresh:
        return HTTP_Response(content={}, status_code=404)
    token:User_db_pb2.ResponseAccessToken = GRPC_User().refresh_token(refresh)
    htc = token.response.http_code.split("/")
    status_code = htc[0]
    if len(htc) == 2:
        message = htc[1]
        return HTTP_Response(content={"message":message}, status_code=int(status_code))
    return HTTP_Response(content={}, status_code=int(status_code))

@router.post("/password")
def password(body:UserBody):
    response:base_pb2.Response = GRPC_User().password_update(body.email, body.password)

    htc = response.http_code.split("/")
    status_code = htc[0]
    if len(htc) == 2:
        message = htc[1]
        return HTTP_Response(content={"message":message}, status_code=int(status_code))
    return HTTP_Response(content={}, status_code=int(status_code))

# ? 인증 만들 생각이였는데 뭐지
# def authentication(func:function):
#     def wrapped_func(*arg, **kwarg):
#         request:Request = kwarg["request"]
#         (request.cookies["access_token"])