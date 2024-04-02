import grpc
import os

class GRPC_Manager(object):
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
            cls._instance.host = os.environ["grpc_host"]
            cls._instance.server_port = os.environ["grpc_server_port"]

            cls._instance.channel = grpc.insecure_channel(
                '{}:{}'.format(cls._instance.host, cls._instance.server_port))
        return cls._instance

    def __init__(self):
        self.stub:any
        self.host:str
        self.server_port:int
        self.channel:grpc.Channel
