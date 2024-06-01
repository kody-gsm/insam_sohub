from concurrent import futures
import grpc
from logic._grpc.protos import User_db_pb2_grpc, User_db_pb2, base_pb2

SUPER_TOKEN = "IT'S_SUPER_TOKEN"
SUPER_REFRESH_TOKEN = "IT'S_SUPER_REFRESH_TOKEN"

USER_EMAIL = "test@test.test"
USER_PASSWORD = "itistestPW"

class UserService(User_db_pb2_grpc.UserTrafficServicer):
    def user_login(self, User:User_db_pb2.User):
        print(User)
        if User.user_email != USER_EMAIL or User.user_password != USER_PASSWORD:
            response = base_pb2.Response("404/user not found")
            return User_db_pb2.ResponseJwtToken(
            response=response)

        access_token = base_pb2.AccessToken(SUPER_TOKEN)
        refresh_token = User_db_pb2.RefreshToken(SUPER_REFRESH_TOKEN)
        response = base_pb2.Response("200")

        return User_db_pb2.ResponseJwtToken(
            access_token=access_token,
            refresh_token=refresh_token,
            response=response)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    User_db_pb2_grpc.add_UserTrafficServicer_to_server(UserService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()