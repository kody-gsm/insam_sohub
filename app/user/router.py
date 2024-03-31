from fastapi import APIRouter
from account import router as account_router

router = APIRouter(
    prefix="/user"
)

router.include_router(account_router)