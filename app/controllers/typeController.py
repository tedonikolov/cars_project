from fastapi import APIRouter

import app.repositories.typeRepo as typeRepo
import app.models.TypeDTO as Type

router = APIRouter(prefix="/api/v1/type", tags=["type"], responses={404: {"description": "Not found"}, 200: {"description": "Success"}})

@router.get("/all", summary="Get all types")
async def get_types():
    return typeRepo.get_types()

@router.get("/{id}", summary="Get a type by id")
async def get_type(id: int):
    return typeRepo.get_type(id)

@router.post("", summary="Create a type")
async def create_type(typeDTO: Type.TypeDTO):
    return typeRepo.create_type(typeDTO)

@router.put("/{id}", summary="Update a type")
async def update_type(id: int, typeDTO: Type.TypeDTO):
    return typeRepo.update_type(id, typeDTO)