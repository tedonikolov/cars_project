from pydantic import BaseModel


class ModelDTO(BaseModel):
    name: str
    brandId: int
