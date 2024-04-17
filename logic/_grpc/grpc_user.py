from logic._grpc.protos import base_pb2, User_db_pb2_grpc, User_db_pb2 as user_pb2
from logic._grpc.grpc_manager import GRPC_Manager

class GRPC_User():
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance.manager = GRPC_Manager()
            cls._instance.stub = User_db_pb2_grpc.UserTrafficStub(cls._instance.manager.channel)
        return cls._instance

    def __init__(self):
        self.manager:GRPC_Manager
        self.stub:User_db_pb2_grpc.UserTrafficStub

    def user_create(self, email:str, password:str) -> base_pb2.Response:
        user = user_pb2.User(user_email=email, user_password=password)
        return self.stub.user_create(user)
        
    def user_delete(self, token:str) -> base_pb2.Response:
        access_token = base_pb2.AccessToken(token)
        return self.stub.user_delete(access_token)
        
    def email_find(self, email:str) -> base_pb2.Response:
        user = user_pb2.User(email, None)
        return self.stub.email_find(user)

    def user_login(self, email:str, password:str) -> user_pb2.ResponseJwtToken:
        user = user_pb2.User(email, password)
        return self.stub.user_login(user)
    
    def password_update(self, email:str, password:str) -> base_pb2.Response:
        user = user_pb2.User(email, password)
        return self.stub.password_update(user)
        
    def refresh_token(self, token:str) -> user_pb2.ResponseAccessToken:
        access_token = base_pb2.AccessToken(token)
        return self.stub.refresh_token(access_token)
