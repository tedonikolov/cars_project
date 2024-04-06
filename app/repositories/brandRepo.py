from sqlalchemy import text

from app.repositories import pandasConnection as Connection
import pandas as pd


def get_brands():
    query = text("SELECT * FROM brand")
    df = pd.read_sql(query, Connection.engine)
    return df.to_dict(orient='records')


def create_brand(brandDTO):
    query = text("INSERT INTO brand (brand) VALUES (:brand)")
    with Connection.engine.begin() as db:
        db.execute(query, {"brand": brandDTO.name})
    if get_brand_by_name(brandDTO.name):
        return "Brand created successfully!"


def get_brand(id):
    query = text("SELECT * FROM brand WHERE id_brand = :id")
    df = pd.read_sql(query, Connection.engine, params={"id": id})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None


def get_brand_by_name(name):
    query = text("SELECT * FROM brand WHERE brand = :name")
    df = pd.read_sql(query, Connection.engine, params={"name": name})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None


def update_brand(id, brandDTO):
    query = text("UPDATE brand SET brand = :brand WHERE id_brand = :id")
    with Connection.engine.begin() as db:
        db.execute(query, {"brand": brandDTO.name, "id": id})
    if get_brand(id).__getitem__("brand") == brandDTO.name:
        return "Brand updated successfully!"
    return None
