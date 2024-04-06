from sqlalchemy import text

from app.repositories import pandasConnection as Connection
import pandas as pd


def get_clients():
    query = text("SELECT name, address, telephone FROM client")
    df = pd.read_sql(query, Connection.engine)
    return df.to_dict(orient='records')


def get_client(id_client):
    query = text("SELECT name, address, telephone FROM client WHERE id_client = :id")
    df = pd.read_sql(query, Connection.engine, params={"id": id_client})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None


def create_client(clientDTO):
    query = text("INSERT INTO client (name, address, telephone) VALUES (:name, :address, :telephone)")
    with Connection.engine.begin() as db:
        db.execute(query, {
                "name": clientDTO.name,
                "address": clientDTO.address,
                "telephone": clientDTO.telephone
            }
        )
    if get_client_by_name(clientDTO.name):
        return "Client created successfully!"


def get_client_by_name(name):
    query = text("SELECT * FROM client WHERE name = :name")
    df = pd.read_sql(query, Connection.engine, params={"name": name})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None


def update_client(id_client, clientDTO):
    query = text("UPDATE client SET name = :name, address = :address, telephone = :telephone WHERE id_client = :id")
    with Connection.engine.begin() as db:
        result = db.execute(query, {
                "name": clientDTO.name,
                "address": clientDTO.address,
                "telephone": clientDTO.telephone,
                "id": id_client
            }
        )
    if result.rowcount > 0:
        return "Client updated successfully!"
    else:
        return "Client not found or no changes were made."
