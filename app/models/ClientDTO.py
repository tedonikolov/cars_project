from pydantic import BaseModel


class ClientDTO(BaseModel):
    name: str
    address: str
    telephone: str
