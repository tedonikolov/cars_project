from datetime import date

from pydantic import BaseModel


class RentDTO(BaseModel):
    clientId: int
    carId: int
    rentDate: date
    days: int
