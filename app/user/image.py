from apscheduler.schedulers.background import BackgroundScheduler
from logic.socket import connect_socket
 
sched = BackgroundScheduler(timezone='Asia/Seoul')

@sched.scheduled_job(hour='12',minute='00', id='image_add')
async def image_add():
    for pot_code in connect_socket.pot_sockets:
        await connect_socket.pot_sockets[pot_code].send(message="server#s4")

@sched.scheduled_job(hour='12',minute='00', id='test')
async def test():
    print("test")