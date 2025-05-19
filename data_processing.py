import snowflake.connector
import pandas as pd

def fetch_data():
    conn = snowflake.connector.connect(
        user='YOUR_USERNAME',
        password='YOUR_PASSWORD',
        account='YOUR_ACCOUNT'
    )
    query = "SELECT * FROM tourism_data;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
