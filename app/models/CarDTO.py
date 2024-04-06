from pydantic import BaseModel


class CarDTO(BaseModel):
    modelId: int
    typeId: int
    year: int
    traveled: int
    dailyPrice: int