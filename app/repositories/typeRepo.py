from sqlalchemy import text

from app.repositories import pandasConnection as Connection
import pandas as pd


def get_types():
    query = text("SELECT * FROM type")
    df = pd.read_sql(query, Connection.engine)
    return df.to_dict(orient='records')


def get_type(id):
    query = text("SELECT * FROM type WHERE id_type = :id")
    df = pd.read_sql(query, Connection.engine, params={"id": id})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None


def get_type_by_name(name):
    query = text("SELECT * FROM type WHERE type = :name")
    df = pd.read_sql(query, Connection.engine, params={"name": name})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None


def create_type(typeDTO):
    query = text("INSERT INTO type (type) VALUES (:type)")
    with Connection.engine.begin() as db:
        db.execute(query, {"type": typeDTO.name})
    if get_type_by_name(typeDTO.name):
        return "Type created successfully!"
    return None


def update_type(id, typeDTO):
    query = text("UPDATE type SET type = :type WHERE id_type = :id")
    with Connection.engine.begin() as db:
        db.execute(query, {"type": typeDTO.name, "id": id})
    if get_type(id).__getitem__("type") == typeDTO.name:
        return "Type updated successfully!"
    return None

