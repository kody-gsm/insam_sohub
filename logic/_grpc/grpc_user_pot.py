from protos import base_pb2, Pot_db_pb2_grpc, Pot_db_pb2 as pot_pb2
from grpc_manager import GRPC_Manager
from typing import Generator

class GRPC_UserPot(GRPC_Manager):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance.manager = GRPC_Manager()
            cls._instance.stub = Pot_db_pb2_grpc.UserPotTraffic(cls._instance.manager.channel)
        return cls._instance

    def __init__(self):
        self.manager:GRPC_Manager
        self.stub:Pot_db_pb2_grpc.UserPotTrafficStub

    def user_add_pot(self, token:str, pot_code:str, pot_name:str=None):
        access_token = base_pb2.AccessToken(token)
        pot = pot_pb2.Pot(pot_code, pot_name)
        certified_pot = pot_pb2.CertifiedPot(access_token, pot)
        return self.stub.user_add_pot(certified_pot)
    
    def user_remove_pot(self, token:str, pot_code:str, pot_name:str=None):
        access_token = base_pb2.AccessToken(token)
        pot = pot_pb2.Pot(pot_code, pot_name)
        certified_pot = pot_pb2.CertifiedPot(access_token, pot)
        return self.stub.user_remove_pot(certified_pot)
    
    def user_read_pot_list(self, token:str) -> Generator[pot_pb2.Pot]:
        access_token = base_pb2.AccessToken(token)
        for pot in self.stub.user_read_pot_list(access_token):
            yield pot