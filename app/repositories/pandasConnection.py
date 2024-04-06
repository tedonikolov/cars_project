from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1234@cars_db:5432/cars_serviceDB')