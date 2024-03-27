from user import User_db_pb2 as pb2, User_db_pb2_grpc as pb2_grpc
from base import base_pb2 as base_pb2
from grpc_manager import GRPC_Manager

class GRPC_User(GRPC_Manager):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance.stub = pb2_grpc.UserTraffic(cls._instance.channel)

    def __init__(self):
        self.stub:pb2_grpc.UserTrafficStub

    def user_create(self, email:str, password:str) -> base_pb2.Response:
        user = pb2.User(email, password)
        return self.stub.user_create(user)
        
    def user_delete(self, token:str) -> base_pb2.Response:
        access_token = base_pb2.AccessToken(token)
        return self.stub.user_delete(access_token)
        
    def user_update(self, token:str) -> base_pb2.Response:
        access_token = base_pb2.AccessToken(token)
        return self.stub.user_update(access_token)

    def user_login(self, email:str, password:str) -> pb2.JWTToken:
        user = pb2.User(email, password)
        return self.stub.user_login(user)
        
    def refresh_token(self, token:str) -> pb2.RefreshToken:
        access_token = base_pb2.AccessToken(token)
        return self.stub.refresh_token(access_token)