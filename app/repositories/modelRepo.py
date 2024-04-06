from sqlalchemy import text

from app.repositories import pandasConnection as Connection
import pandas as pd

def get_models():
    query = text("SELECT id_model,model,brand FROM model join brand b on b.id_brand = model.brand_id")
    df = pd.read_sql(query, Connection.engine)
    return df.to_dict(orient='records')

def create_model(modelDTO):
    query = text("INSERT INTO model (model, brand_id) VALUES (:model, :brand_id)")
    with Connection.engine.begin() as db:
        db.execute(query, {"model": modelDTO.name, "brand_id": modelDTO.brandId})
    if get_model_by_name(modelDTO.name):
        return "Model created successfully!"


def get_model(id):
    query = text("SELECT id_model,model,brand FROM model join brand b on b.id_brand = model.brand_id WHERE id_model = :id")
    df = pd.read_sql(query, Connection.engine, params={"id": id})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None

def get_model_by_name(name):
    query = text("SELECT * FROM model WHERE model = :name")
    df = pd.read_sql(query, Connection.engine, params={"name": name})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None

def update_model(id, modelDTO):
    query = text("UPDATE model SET model = :model, brand_id = :brand_id WHERE id_model = :id")
    with Connection.engine.begin() as db:
        db.execute(query, {"model": modelDTO.name, "brand_id": modelDTO.brandId, "id": id})
    if get_model(id).__getitem__("model") == modelDTO.name:
        return "Model updated successfully!"
    return None