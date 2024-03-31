from pot import Pot_db_pb2 as pb2, Pot_db_pb2_grpc as pb2_grpc
from base import base_pb2 as base_pb2
from grpc_manager import GRPC_Manager
from typing import Generator

class GRPC_UserPot(GRPC_Manager):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance.manager = GRPC_Manager()
            cls._instance.stub = pb2_grpc.UserPotTraffic(cls._instance.manager.channel)
        return cls._instance

    def __init__(self):
        self.manager:GRPC_Manager
        self.stub:pb2_grpc.UserPotTrafficStub

    def user_add_pot(self, token:str, pot_code:str, pot_name:str=None):
        access_token = base_pb2.AccessToken(token)
        pot = pb2.Pot(pot_code, pot_name)
        certified_pot = pb2.CertifiedPot(access_token, pot)
        return self.stub.user_add_pot(certified_pot)
    
    def user_remove_pot(self, token:str, pot_code:str, pot_name:str=None):
        access_token = base_pb2.AccessToken(token)
        pot = pb2.Pot(pot_code, pot_name)
        certified_pot = pb2.CertifiedPot(access_token, pot)
        return self.stub.user_remove_pot(certified_pot)
    
    def user_read_pot_list(self, token:str) -> Generator[pb2.Pot]:
        access_token = base_pb2.AccessToken(token)
        for pot in self.stub.user_read_pot_list(access_token):
            yield pot