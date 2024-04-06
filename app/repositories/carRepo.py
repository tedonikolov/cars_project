from sqlalchemy import text

from app.repositories import pandasConnection as Connection
import pandas as pd


def get_cars():
    query = text(
        "SELECT id_car, brand, model, type, year, traveled, daily_price FROM car JOIN model m on m.id_model = car.model_id JOIN brand b on b.id_brand = m.brand_id JOIN type t on t.id_type = car.type_id ORDER BY id_car")
    df = pd.read_sql(query, Connection.engine)
    return df.to_dict(orient='records')


def get_car(id):
    query = text(
        "SELECT id_car, brand, model, type, year, traveled, daily_price FROM car JOIN model m on m.id_model = car.model_id JOIN brand b on b.id_brand = m.brand_id JOIN type t on t.id_type = car.type_id WHERE id_car = :id")
    df = pd.read_sql(query, Connection.engine, params={"id": id})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None


def get_car_by_car(modelId, typeId, year, traveled, dailyPrice):
    query = text(
        "SELECT * FROM car WHERE model_id = :modelId AND type_id = :typeId AND year = :year AND traveled = :traveled AND daily_price = :dailyPrice")
    df = pd.read_sql(query, Connection.engine,
                     params={"modelId": modelId, "typeId": typeId, "year": year, "traveled": traveled,
                             "dailyPrice": dailyPrice})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None


def create_car(carDTO):
    query = text(
        "INSERT INTO car (model_id, type_id, year, traveled, daily_price) VALUES (:model_id, :type_id, :year, :traveled, :daily_price)")
    with Connection.engine.begin() as db:
        db.execute(query, {"model_id": carDTO.modelId, "type_id": carDTO.typeId, "year": carDTO.year,
                           "traveled": carDTO.traveled, "daily_price": carDTO.dailyPrice})
    if get_car_by_car(carDTO.modelId, carDTO.typeId, carDTO.year, carDTO.traveled, carDTO.dailyPrice):
        return "Car created successfully!"
    return None


def update_car(id, carDTO):
    query = text(
        "UPDATE car SET model_id = :model_id, type_id = :type_id, year = :year, traveled = :traveled, daily_price = :daily_price WHERE id_car = :id")
    with Connection.engine.begin() as db:
        db.execute(query, {"model_id": carDTO.modelId, "type_id": carDTO.typeId, "year": carDTO.year,
                           "traveled": carDTO.traveled, "daily_price": carDTO.dailyPrice, "id": id})
    if get_car(id).__getitem__("model") == carDTO.modelId and get_car(id).__getitem__(
            "type") == carDTO.typeId and get_car(id).__getitem__("year") == carDTO.year and get_car(id).__getitem__(
            "traveled") == carDTO.traveled and get_car(id).__getitem__("daily_price") == carDTO.dailyPrice:
        return "Car updated successfully!"
    return None
