
# from __future__ import print_function
# import logging
# import grpc
# import users_pb2
# import users_pb2_grpc


# def run():
#     with grpc.insecure_channel("localhost:50051") as channel:
#         stub = users_pb2_grpc.UserServiceStub(channel)
#         response = stub.GetUsers(users_pb2.GetUsersRequest())
#     print(response.users)


# if __name__ == "__main__":
#     logging.basicConfig()
#     run()

import grpc
import users_pb2
import users_pb2_grpc

def run():
    channel = grpc.insecure_channel('127.0.0.1:50052')
    stub = users_pb2_grpc.UserServiceStub(channel)
    try:
        response = stub.GetUsers(users_pb2.GetUsersRequest(), timeout=10)  # Increase timeout
        print("Response received:", response)
    except grpc.RpcError as e:
        print(f"RPC failed: {e.code()} - {e.details()}")
        print("Debug Error String:", e.debug_error_string())

if __name__ == '__main__':
    run()




