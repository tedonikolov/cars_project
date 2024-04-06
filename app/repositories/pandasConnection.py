from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1234@localhost:5555/cars_serviceDB')