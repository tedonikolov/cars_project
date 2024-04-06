from fastapi import APIRouter

import app.repositories.brandRepo as brandRepo
import app.models.BrandDTO as Brand

router = APIRouter(prefix="/api/v1/brand", tags=["brand"], responses={404: {"description": "Not found"}, 200: {"description": "Success"}})


@router.get("/all", summary="Get all brands")
async def get_brands():
    return brandRepo.get_brands()


@router.get("/{id}", summary="Get a brand by id")
async def get_brand(id: int):
    return brandRepo.get_brand(id)


@router.post("", summary="Create a brand")
async def create_brand(brandDTO: Brand.BrandDTO):
    return brandRepo.create_brand(brandDTO)


@router.put("/{id}", summary="Update a brand")
async def update_brand(id: int, brandDTO: Brand.BrandDTO):
    return brandRepo.update_brand(id, brandDTO)
