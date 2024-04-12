from fastapi import APIRouter
from account import router as account_router
from cam import router as cam_router
from pot import router as pot_router

router = APIRouter(
    prefix="/user"
)

router.include_router(account_router)
router.include_router(cam_router)
router.include_router(pot_router)