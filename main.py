from fastapi import FastAPI
from models.api import router

app = FastAPI()

app.include_router(router)
