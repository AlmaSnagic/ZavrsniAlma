from sqlalchemy import create_engine

def load_to_mssql(df, table_name, connection_string):
    engine = create_engine(connection_string)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f"Data loaded to table: {table_name}")