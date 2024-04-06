from fastapi import FastAPI
from app.controllers import brandController

app = FastAPI()

app.include_router(brandController.router)