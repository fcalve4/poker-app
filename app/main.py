from fastapi import FastAPI
from app.api import router

app = FastAPI(title="Poker Engine API")
app.include_router(router)