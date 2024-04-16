from fastapi import APIRouter, Response as HTTP_Response, Request, Body
from pydantic import BaseModel
from logic._grpc.grpc_user import GRPC_User
from logic._grpc.protos import base_pb2, User_db_pb2
 
router = APIRouter(
    prefix="/account"
)

class UserBody(BaseModel):
    email:str
    password:str

@router.post("/sign-up")
def post_sign_up(body:UserBody):
    print(body.password)
    response:base_pb2.Response = GRPC_User().user_create(body.email, body.password)
    return HTTP_Response(status_code=int(response.http_code))

@router.post("/login")
def post_login(body:UserBody):
    token:User_db_pb2.ResponseJwtToken = GRPC_User().user_login(body.email, body.password)
    if token.access_token:
        response = HTTP_Response({"message":"success",
                              "refresh_token":token.refresh_token.refresh}, int(status_code=token.response.http_code))
        response.set_cookie("access_token", token.access_token.access)
        return response
    return HTTP_Response(status_code=int(token.response.http_code))


# ? 인증 만들 생각이였는데 뭐지
# def authentication(func:function):
#     def wrapped_func(*arg, **kwarg):
#         request:Request = kwarg["request"]
#         (request.cookies["access_token"])