from pot import Pot_db_pb2 as pb2, Pot_db_pb2_grpc as pb2_grpc
from base import base_pb2 as base_pb2
from grpc_manager import GRPC_Manager

class GRPC_Pot(GRPC_Manager):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance.stub = pb2_grpc.PotTrafficStub(cls._instance.channel)

    def __init__(self):
        self.stub:pb2_grpc.PotTrafficStub

    def pot_create(self, pot_code:str, pot_name:str):
        pot = pb2.Pot(pot_code, pot_name)
        return self.stub.pot_create(pot)
    
    def pot_delete(self, token:str, pot_code:str, pot_name:str):
        access_token = base_pb2.AccessToken(token)
        pot = pb2.Pot(pot_code, pot_name)
        certified_pot = pb2.CertifiedPot(access_token, pot)
        return self.stub.pot_delete(certified_pot)
    
    def pot_update(self, token:str, pot_code:str, pot_name:str):
        access_token = base_pb2.AccessToken(token)
        pot = pb2.Pot(pot_code, pot_name)
        certified_pot = pb2.CertifiedPot(access_token, pot)
        return self.stub.pot_update(certified_pot)
    
    def pot_read(self, token:str):
        access_token = base_pb2.AccessToken(token)
        return self.stub.pot_read(access_token)
    
    def pot_read_list(self, token:str):
        access_token = base_pb2.AccessToken(token)
        for pot in self.stub.pot_read_list(access_token):
            yield pot