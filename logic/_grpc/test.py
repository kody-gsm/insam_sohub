from logic._grpc.grpc_user import GRPC_User
from grpc_image import GRPC_Image, GRPC_Manager
print(GRPC_Manager())
print(GRPC_User().user_create("sad","asdd"))
print(GRPC_Image())