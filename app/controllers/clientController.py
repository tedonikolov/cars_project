from fastapi import APIRouter

import app.repositories.clientRepo as clientRepo
import app.models.ClientDTO as Client

router = APIRouter(prefix="/api/v1/client", tags=["client"], responses={404: {"description": "Not found"}, 200: {"description": "Success"}})


@router.get("/all", summary="Get all clients")
async def get_clients():
    return clientRepo.get_clients()


@router.get("/{id}", summary="Get a client by id")
async def get_client(id: int):
    return clientRepo.get_client(id)


@router.post("", summary="Create a client")
async def create_client(clientDTO: Client.ClientDTO):
    return clientRepo.create_client(clientDTO)


@router.put("/{id}", summary="Update a client")
async def update_client(id: int, clientDTO: Client.ClientDTO):
    return clientRepo.update_client(id, clientDTO)
