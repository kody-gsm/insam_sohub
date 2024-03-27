from image import Image_db_pb2 as pb2, Image_db_pb2_grpc as pb2_grpc
from base import base_pb2 as base_pb2
from pot import Pot_db_pb2 as pot_pb2
from grpc_manager import GRPC_Manager

class GRPC_UserPot(GRPC_Manager):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance.stub = pb2_grpc.ImageTraffic(cls._instance.channel)

    def __init__(self):
        self.stub:pb2_grpc.ImageTrafficStub

    def image_create(self, token:str, pot_code:str, pot_name, image:str):
        access_token = base_pb2.AccessToken(token)
        pot = pot_pb2.Pot(pot_code, pot_name)
        certified_image = pb2.CertifiedImage(access_token, pot, image)
        return self.stub.image_create(certified_image)
    
    def image_delete(self, token:str, pot_code:str, pot_name, image:str):
        access_token = base_pb2.AccessToken(token)
        pot = pot_pb2.Pot(pot_code, pot_name)
        certified_image = pb2.CertifiedImage(access_token, pot, image)
        return self.stub.image_delete(certified_image)
    
    def image_read(self, token:str, pot_code:str, pot_name, image:str):
        access_token = base_pb2.AccessToken(token)
        pot = pot_pb2.Pot(pot_code, pot_name)
        certified_image = pb2.CertifiedImage(access_token, pot, image)
        return self.stub.image_read(certified_image)
    
    def image_read_list(self, token:str, pot_code:str, pot_name:str):
        access_token = base_pb2.AccessToken(token)
        pot = pot_pb2.Pot(pot_code, pot_name)
        certified_pot = pot_pb2.CertifiedPot(access_token, pot)
        for image in self.stub.image_read_list(certified_pot):
            yield image