from logic._grpc.protos import base_pb2, Image_db_pb2 as image_pb2, Image_db_pb2_grpc, Pot_db_pb2 as pot_pb2
from logic._grpc.grpc_manager import GRPC_Manager

class GRPC_Image():
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance.manager = GRPC_Manager()
            cls._instance.stub = Image_db_pb2_grpc.ImageTrafficStub(cls._instance.manager.channel)
        return cls._instance

    def __init__(self):
        self.manager:GRPC_Manager
        self.stub:Image_db_pb2_grpc.ImageTrafficStub

    def image_create(self, token:str, pot_code:str, pot_name:str, 
                      image_file:str):
        access_token = base_pb2.AccessToken(access=token)
        pot = pot_pb2.Pot(pot_code=pot_code, pot_name=pot_name)
        image = image_pb2.Image(image_id=None, image_file=image_file, image_time=None)
        certified_image = image_pb2.CertifiedImage(access_token=access_token, pot=pot, image=image)
        return self.stub.image_create(certified_image)
    
    def image_delete(self, token:str, pot_code:str, pot_name:str, 
                    image_id:str):
        access_token = base_pb2.AccessToken(access=token)
        pot = pot_pb2.Pot(pot_code=pot_code, pot_name=pot_name)
        image = image_pb2.Image(image_id=image_id, image_file=None, image_time=None)
        certified_image = image_pb2.CertifiedImage(access_token=access_token, pot=pot, image=image)
        return self.stub.image_delete(certified_image)
    
    def image_read(self, token:str, pot_code:str, pot_name:str, 
                   image_id:str):
        access_token = base_pb2.AccessToken(access=token)
        pot = pot_pb2.Pot(pot_code=pot_code, pot_name=pot_name)
        image = image_pb2.Image(image_id=image_id, image_file=None, image_time=None)
        certified_image = image_pb2.CertifiedImage(access_token=access_token, pot=pot, image=image)
        return self.stub.image_read(certified_image)
    
    def image_read_list(self, token:str, pot_code:str, pot_name:str|None=None):
        access_token = base_pb2.AccessToken(access=token)
        pot = pot_pb2.Pot(pot_code=pot_code, pot_name=pot_name)
        certified_pot = pot_pb2.CertifiedPot(access_token=access_token, pot=pot)
        for image in self.stub.image_read_list(certified_pot):
            yield image