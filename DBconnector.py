from sqlalchemy import create_engine
import pandas as pd

class DatabaseConnector:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)

    def read_table(self, table):
        return pd.read_sql(f"SELECT * FROM {table}", self.engine)

    def write_table(self, df, table):
        df.to_sql(table, self.engine, if_exists="replace", index=False)
