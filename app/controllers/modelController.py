from fastapi import APIRouter

import app.repositories.modelRepo as modelRepo
import app.models.ModelDTO as Model

router = APIRouter(prefix="/api/v1/model", tags=["model"], responses={404: {"description": "Not found"}, 200: {"description": "Success"}})

@router.get("/all", summary="Get all models")
async def get_models():
    return modelRepo.get_models()

@router.get("/{id}", summary="Get a model by id")
async def get_model(id: int):
    return modelRepo.get_model(id)

@router.post("", summary="Create a model")
async def create_model(modelDTO: Model.ModelDTO):
    return modelRepo.create_model(modelDTO)

@router.put("/{id}", summary="Update a model")
async def update_model(id: int, modelDTO: Model.ModelDTO):
    return modelRepo.update_model(id, modelDTO)
