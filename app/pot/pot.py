from fastapi import APIRouter, WebSocket
from logic._grpc.grpc_pot import GRPC_Pot
import asyncio

router = APIRouter(
    prefix=""
)

pot_connections:dict[str, WebSocket] = {}

@router.websocket("/connect")
async def connect_pot(websocket:WebSocket):
    await websocket.accept()
    pot_connections[websocket.headers["pot_code"]] = websocket
    GRPC_Pot().pot_create(pot_code=websocket.headers["pot_code"])


    
