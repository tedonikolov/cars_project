from fastapi import FastAPI
from app.controllers import brandController
from app.controllers import modelController
from app.controllers import typeController
from app.controllers import carController
from app.controllers import clientController


tags_metadata = [
    {
        "name": "brand",
        "description": "Operations with brands.",
    },
    {
        "name": "model",
        "description": "Operations with models.",
    },
    {
        "name": "type",
        "description": "Operations with types.",
    },
    {
        "name": "car",
        "description": "Operations with cars.",
    },
    {
        "name": "client",
        "description": "Operations with clients."
    }
]

app = FastAPI(
    title="Cars rent API",
    summary="Everything you need to rent a car.",
    version="0.0.1",
    openapi_url="/api/v1/openapi.json",
    openapi_tags=tags_metadata,
)

app.include_router(brandController.router)
app.include_router(modelController.router)
app.include_router(typeController.router)
app.include_router(carController.router)
app.include_router(clientController.router)