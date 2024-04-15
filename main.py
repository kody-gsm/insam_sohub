from fastapi import FastAPI

from app.pot.router import router as pot_router
from app.user.router import router as user_router

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(router=pot_router)
app.include_router(router=user_router)

app.get("/")
def hello():
    return "hello"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app)