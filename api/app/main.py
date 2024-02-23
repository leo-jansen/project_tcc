from typing import Union

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from .routes.auth.auth_router import router as auth_router
from .routes.user.user_router import router as user_router
from .util.consts import APP_HOST, APP_PORT

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)


def start_server():
    uvicorn.run(app="app.main:app", host=str(APP_HOST), port=int(APP_PORT), reload=True)


if __name__ == "__main__":
    start_server()
