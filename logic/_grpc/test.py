# from logic._grpc.grpc_user import GRPC_User
# from grpc_image import GRPC_Image, GRPC_Manager
# print(GRPC_User().user_create("abc","abc"))
# print(GRPC_Image())

li = "asd"
def sp(n):
    for i in n:
        yield i
    return None

p1, p2 = sp(li.split())
print(p1)
print(p2)