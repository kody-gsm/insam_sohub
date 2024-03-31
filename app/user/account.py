from fastapi import APIRouter, Response as HTTP_Response, Request
from pydantic import BaseModel
from ...logic._grpc.grpc_user import GRPC_User
from ...logic._grpc.base import base_pb2
from ...logic._grpc.user import User_db_pb2
 
router = APIRouter(
    prefix="/account"
)

class UserBody(BaseModel):
    email:str
    password:str

@router.post("/sign-up")
def post_sign_up(body:UserBody):
    response:base_pb2.Response = GRPC_User.user_create(body.email, body.password)
    if response.check:
        return HTTP_Response({"message":"success"}, 200)
    return HTTP_Response({"message":"이미 유저가 존재함"}, 400)

@router.post("/login")
def post_login(body:UserBody):
    token:User_db_pb2.JWTToken = GRPC_User.user_login(body.email, body.password)
    if token.access:
        response = HTTP_Response({"message":"success",
                              "refresh_token":token.refresh}, 200)
        response.set_cookie("access_token", token.access)
        return response
    return HTTP_Response({"message":"이미 유저가 존재함"}, 400)


# ? 인증 만들 생각이였는데 뭐지
# def authentication(func:function):
#     def wrapped_func(*arg, **kwarg):
#         request:Request = kwarg["request"]
#         (request.cookies["access_token"])