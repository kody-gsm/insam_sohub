from fastapi import APIRouter, WebSocket
from logic._grpc.grpc_pot import GRPC_Pot

router = APIRouter(
    prefix=""
)

pot_connections:dict[str, WebSocket]={}

@router.websocket("/connect")
async def connect_pot(websocket:WebSocket):
    if websocket.headers["pot_code"] in pot_connections:
        raise "pot_code 중복"
    await websocket.accept()
    pot_connections[websocket.headers["pot_code"]] = websocket
    
    GRPC_Pot().pot_create(pot_code=websocket.headers["pot_code"])


    
