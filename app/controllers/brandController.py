from fastapi import APIRouter
import app.repositories.brandRepo as brandRepo

router = APIRouter()

@router.get("/getBrands")
async def getBrands():
    return brandRepo.get_brands()
