from fastapi import FastAPI

from app.pot.router import router as pot_router

app = FastAPI()

app.include_router(router=pot_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app)