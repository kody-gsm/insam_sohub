from fastapi import APIRouter
from .pot import router as pot_router

router = APIRouter(
    prefix="/pot"
)

router.include_router(router=pot_router)