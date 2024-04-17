from logic._grpc.protos import base_pb2, Image_db_pb2 as image_pb2, Image_db_pb2_grpc, Pot_db_pb2 as pot_pb2
from logic._grpc.grpc_manager import GRPC_Manager

class GRPC_Image(GRPC_Manager):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance.manager = GRPC_Manager()
            cls._instance.stub = Image_db_pb2_grpc.ImageTrafficStub(cls._instance.manager.channel)
        return cls._instance

    def __init__(self):
        self.manager:GRPC_Manager
        self.stub:Image_db_pb2_grpc.ImageTrafficStub

    def image_create(self, token:str, pot_code:str, pot_name:str, 
                      image_file:str):
        access_token = base_pb2.AccessToken(token)
        pot = pot_pb2.Pot(pot_code, pot_name)
        image = image_pb2.Image(None, image_file, None)
        certified_image = image_pb2.CertifiedImage(access_token, pot, image)
        return self.stub.image_create(certified_image)
    
    def image_delete(self, token:str, pot_code:str, pot_name:str, 
                    image_id:str):
        access_token = base_pb2.AccessToken(token)
        pot = pot_pb2.Pot(pot_code, pot_name)
        image = image_pb2.Image(image_id, None, None)
        certified_image = image_pb2.CertifiedImage(access_token, pot, image)
        return self.stub.image_delete(certified_image)
    
    def image_read(self, token:str, pot_code:str, pot_name:str, 
                   image_id:str):
        access_token = base_pb2.AccessToken(token)
        pot = pot_pb2.Pot(pot_code, pot_name)
        image = image_pb2.Image(image_id, None, None)
        certified_image = image_pb2.CertifiedImage(access_token, pot, image)
        return self.stub.image_read(certified_image)
    
    def image_read_list(self, token:str, pot_code:str, pot_name:str):
        access_token = base_pb2.AccessToken(token)
        pot = pot_pb2.Pot(pot_code, pot_name)
        certified_pot = pot_pb2.CertifiedPot(access_token, pot)
        for image in self.stub.image_read_list(certified_pot):
            yield image