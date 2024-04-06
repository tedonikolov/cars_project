from fastapi import APIRouter

import app.repositories.rentRepo as rentRepo
import app.models.RentDTO as Rent

router = APIRouter(prefix="/api/v1/rent", tags=["rent"], responses={404: {"description": "Not found"}, 200: {"description": "Success"}})


@router.get("/all", summary="Get all rents")
async def get_rents():
    return rentRepo.get_rents()


@router.get("/{id}", summary="Get a rent by id")
async def get_rent(id: int):
    return rentRepo.get_rent(id)


@router.post("", summary="Create a rent")
async def create_rent(rentDTO: Rent.RentDTO):
    return rentRepo.create_rent(rentDTO)


@router.put("/{id}", summary="Update a rent")
async def update_rent(id: int, rentDTO: Rent.RentDTO):
    return rentRepo.update_rent(id, rentDTO)
