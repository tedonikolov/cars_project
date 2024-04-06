from fastapi import APIRouter

import app.repositories.carRepo as carRepo
import app.models.CarDTO as Car

router = APIRouter(prefix="/api/v1/car", tags=["car"], responses={404: {"description": "Not found"}, 200: {"description": "Success"}})

@router.get("/all", summary="Get all cars")
async def get_cars():
    return carRepo.get_cars()

@router.get("/{id}", summary="Get a car by id")
async def get_car(id: int):
    return carRepo.get_car(id)

@router.post("", summary="Create a car")
async def create_car(carDTO: Car.CarDTO):
    return carRepo.create_car(carDTO)

@router.put("/{id}", summary="Update a car")
async def update_car(id: int, carDTO: Car.CarDTO):
    return carRepo.update_car(id, carDTO)