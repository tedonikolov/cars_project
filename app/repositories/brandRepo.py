from app.repositories import pandasConnection as connection
import pandas as pd

def get_brands():
    query = 'SELECT * FROM brand'
    df = pd.read_sql(query, connection.engine)
    return df.to_dict(orient='records')