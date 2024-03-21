from fastapi import APIRouter, WebSocket

router = APIRouter(
    prefix=""
)

pot_connections:dict[str, WebSocket]={}

@router.websocket("/connect")
async def connect_pot(websocket:WebSocket):
    if not websocket.headers["pot_code"]:
        raise "pot_code 없음"
    if websocket.headers["pot_code"] in pot_connections:
        raise "pot_code 중복"
    else:
        await websocket.accept()
        pot_connections[websocket.headers["pot_code"]] = websocket

    
