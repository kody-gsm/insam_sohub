from logic._grpc.protos import base_pb2
from grpc._channel import _InactiveRpcError
from fastapi.responses import JSONResponse as HTTP_Response

def check_status_code(grpc_response:base_pb2.Response) -> tuple[int, str|None]:
    htc = grpc_response.http_code.split("/")
    status_code = int(htc[0])
    if len(htc) == 2:
        return status_code, htc[1]
    else:
        return status_code, None
    