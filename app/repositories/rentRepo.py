from sqlalchemy import text

from app.repositories import pandasConnection as Connection
import pandas as pd


def get_rents():
    query = text("SELECT cl.name, m.model, t.type, ca.year, ca.traveled, ca.daily_price, r.rent_date, r.days "
                 "FROM rent r "
                 "JOIN client cl "
                 "ON r.client_id = cl.id_client "
                 "JOIN car ca "
                 "ON r.car_id = ca.id_car "
                 "JOIN model m "
                 "ON ca.model_id = m.id_model "
                 "JOIN type t "
                 "ON ca.type_id = t.id_type ")
    df = pd.read_sql(query, Connection.engine)
    return df.to_dict(orient='records')


def get_rent(id_rent):
    query = text("SELECT cl.name, m.model, t.type, ca.year, ca.traveled, ca.daily_price, r.rent_date, r.days "
                 "FROM rent r "
                 "JOIN client cl "
                 "ON r.client_id = cl.id_client "
                 "JOIN car ca "
                 "ON r.car_id = ca.id_car "
                 "JOIN model m "
                 "ON ca.model_id = m.id_model "
                 "JOIN type t "
                 "ON ca.type_id = t.id_type "
                 "WHERE id_rent = :id")
    df = pd.read_sql(query, Connection.engine, params={"id": id_rent})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None


def create_rent(rentDTO):
    query = text("INSERT INTO rent (client_id, car_id, rent_date, days) VALUES (:client_id, :car_id, :rent_date, :days)")
    with Connection.engine.begin() as db:
        db.execute(query, {
                "client_id": rentDTO.clientId,
                "car_id": rentDTO.carId,
                "rent_date": rentDTO.rentDate,
                "days": rentDTO.days
            }
        )
    if get_rent_by_date(rentDTO.rentDate):
        return "Rent created successfully!"


def get_rent_by_date(rentDate):
    query = text("SELECT * FROM rent WHERE rent_date = :rent_date")
    df = pd.read_sql(query, Connection.engine, params={"rent_date": rentDate})
    if not df.empty:
        return df.to_dict(orient='records')[0]
    return None


def update_rent(id_rent, rentDTO):
    query = text("UPDATE rent "
                 "SET client_id = :client_id, car_id = :car_id, rent_date = :rent_date, days = :days "
                 "WHERE id_rent = :id")
    with Connection.engine.begin() as db:
        result = db.execute(query, {
                "client_id": rentDTO.clientId,
                "car_id": rentDTO.carId,
                "rent_date": rentDTO.rentDate,
                "days": rentDTO.days,
                "id": id_rent
            }
        )
    if result.rowcount > 0:
        return "Rent updated successfully!"
    else:
        return "Rent not found or no changes were made."
