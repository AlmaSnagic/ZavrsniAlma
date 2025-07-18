from sqlalchemy import create_engine, text
import pandas as pd

# Connection string sa SQLAlchemy stilom
connection_string = "mssql+pyodbc://DESKTOP-36F1SCR\\SQLEXPRESS/Wine?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"

# Kreiranje engine konekcije
engine = create_engine(connection_string)

def pokreni_upite():
    with engine.connect() as connection:
        print("\n1️⃣ Top 10 redova:")
        df1 = pd.read_sql(text("SELECT TOP 10 * FROM winequality_red"), connection)
        print(df1)

        print("\n2️⃣ Broj vina po kvaliteti:")
        df2 = pd.read_sql(text("""
            SELECT quality, COUNT(*) AS broj_vina
            FROM winequality_red
            GROUP BY quality
            ORDER BY quality
        """), connection)
        print(df2)

        print("\n3️⃣ Prosječan alkohol po kvaliteti:")
        df3 = pd.read_sql(text("""
            SELECT quality, ROUND(AVG(alcohol), 2) AS prosjecan_alkohol
            FROM winequality_red
            GROUP BY quality
            ORDER BY quality
        """), connection)
        print(df3)

        print("\n4️⃣ Top 5 vina sa najviše alkohola:")
        df4 = pd.read_sql(text("""
            SELECT TOP 5 * FROM winequality_red ORDER BY alcohol DESC
        """), connection)
        print(df4)

        print("\n5️⃣ Broj vina sa pH < 3.2 i kvalitetom >= 7:")
        df5 = pd.read_sql(text("""
            SELECT COUNT(*) AS broj_vina
            FROM winequality_red
            WHERE pH < 3.2 AND quality >= 7
        """), connection)
        print(df5)