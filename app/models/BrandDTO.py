from pydantic import BaseModel


class BrandDTO(BaseModel):
    name: str
