from fastapi import APIRouter
from app.user.account import router as account_router
from app.user.pot import router as pot_router
from app.user.image import route as image_router

router = APIRouter(
    prefix="/user"
)

router.include_router(account_router)
router.include_router(pot_router)
router.include_router(image_router)