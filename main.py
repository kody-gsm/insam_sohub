from fastapi import FastAPI, WebSocket

from app.pot.router import router as pot_router
from app.user.router import router as user_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 origin을 허용하거나, 필요한 경우 특정 origin만 허용할 수 있습니다.
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드를 허용하거나 필요한 메서드만 허용할 수 있습니다.
    allow_headers=["*"],  # 모든 헤더를 허용하거나 필요한 헤더만 허용할 수 있습니다.
)

app.include_router(router=pot_router)
app.include_router(router=user_router)

@app.get("/image-add")
async def add_img():
    from logic.socket import connect_socket
 
    for pot_code in connect_socket.pot_sockets:
        await connect_socket.pot_sockets[pot_code].send_text(data="server#s4")

@app.get("/")
def hello():
    return "hello"

if __name__ == "__main__":
    import uvicorn
    from app.user.image import sched

    sched.start()
    uvicorn.run(app=app, host="0.0.0.0", port=25565)

