import asyncio, websockets

SOCKET:websockets.WebSocketClientProtocol

async def main():
    # socket 연결
    SERVER_URL = "ws://localhost:8000/pot/connect"
    try:
        async with websockets.connect(SERVER_URL, extra_headers={"pot_code":"asdadsd"}) as socket:
            global SOCKET
            SOCKET = socket
            while True:
                msg = await socket.recv()
                await switch(msg)
                
    except websockets.ConnectionClosedOK:
        print("socket end")

tasks:dict[str, asyncio.Task] = {}

async def switch(msg):
    global tasks
    key, stat = msg.split()
    if stat == "start":
        print("process start")
        tasks[key] = asyncio.create_task(f(key))
    elif stat == "end":
        if key in tasks:
            tasks[key].cancel()
            print("process end")


async def f(key):
    while True:
        await asyncio.sleep(0.5)
        print(key, "processing")

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(main())