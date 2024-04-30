import asyncio, websockets

SERVER_URL = "ws://127.0.0.1:8000/pot/connect"
SOCKET:websockets.WebSocketClientProtocol
async def main():

    # socket 연결
    try:
        async with websockets.connect(SERVER_URL, extra_headers={"pot_code":"sds"}) as socket:
            global SOCKET
            SOCKET = socket
            while True:
                msg = await socket.recv()
                print(msg)
                asyncio.create_task(process_task(msg))
                
    except websockets.ConnectionClosedOK:
        print("socket end")

async def process_task(msg):
    await asyncio.sleep(1)
    await SOCKET.send(f"{msg}+p")

if __name__ == "__main__":
    asyncio.run(main())