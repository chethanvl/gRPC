
from concurrent import futures
import logging

import grpc
import users_pb2
import users_pb2_grpc


class Users(users_pb2_grpc.UserServiceServicer):
    def GetUsers(self, request, context):
        return users_pb2.GetUsersResponse(users=[
            users_pb2.User(
                id="1", 
                name='Chethan Lakshminarayana', 
                email='chethanvl@outlook.com', 
                password='chethan@123'
                )
            ])


def serve():
    port = "50052"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserServiceServicer_to_server(Users(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
