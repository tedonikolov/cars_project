from fastapi import FastAPI
from app.controllers import brandController

tags_metadata = [
    {
        "name": "brand",
        "description": "Operations with brands.",
    },
]

app = FastAPI(
    title="Cars rent API",
    summary="Everything you need to rent a car.",
    version="0.0.1",
    description="This is a simple API to rent cars.",
    openapi_url="/api/v1/openapi.json",
    openapi_tags=tags_metadata,
)

app.include_router(brandController.router)