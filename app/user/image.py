from apscheduler.schedulers.background import BackgroundScheduler
from logic.socket import connect_socket
 
sched = BackgroundScheduler(timezone='Asia/Seoul')

@sched.scheduled_job(trigger="cron", hour='12',minute='00', id='image_add')
async def image_add():
    for pot_code in connect_socket.pot_sockets:
        await connect_socket.pot_sockets[pot_code].send(message="server#s4")

# @sched.scheduled_job(trigger="interval", hour='1', id='feed_water')
# async def feed_water():
#     for pot_code in connect_socket.pot_sockets:
#         await connect_socket.pot_sockets[pot_code].send(message="server#s4")

from fastapi import APIRouter, WebSocket, Request, Header
from fastapi.responses import JSONResponse as HTTP_Response
from grpc._channel import _InactiveRpcError
from logic._grpc.grpc_image import GRPC_Image
from logic._grpc.protos.Image_db_pb2 import ResponseImage
from logic._grpc import utils

route = APIRouter(
    prefix="/image"
)


@route.get("/{pot_code}")
async def image_read_list(request:Request, pot_code:str, access_token:str|None = Header(default=None, convert_underscores=False)):
    if not access_token:
        return HTTP_Response(content={"message":"token does not exist"}, status_code=403)
    try:
        grpc_response:ResponseImage = GRPC_Image().image_read_list(token=access_token, pot_code=pot_code)
    except _InactiveRpcError:
        return HTTP_Response(content={"message":"gRPC server is not connect"}, status_code=500)
    
    data = [image_to_dict(i) for i in grpc_response]

    def image_to_dict(image:ResponseImage):
        status_code, message = utils.check_status_code(image.response)
        if status_code // 100 != 2:
            return {"status":status_code, "message":message}
        return {
            "image_id":image.image.image_id,
            "image_time":image.image.image_time,
            "image":image.image.image_file
        }
    
    return HTTP_Response(content=data)