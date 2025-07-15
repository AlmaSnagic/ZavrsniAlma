import pandas as pd
import numpy as np
from scipy import stats

def clean_dataset(df):
    print(f"Početni broj redova: {len(df)}")

    # 1. Uklanjanje duplikata
    df = df.drop_duplicates()
    print(f"Nakon uklanjanja duplikata: {len(df)}")

    # 2. Popunjavanje nedostajućih vrijednosti sa nulama
    df = df.fillna(0)

    # 3. Uklanjanje ekstremnih outliera koristeći Z-score
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    df = df[(np.abs(stats.zscore(df[numeric_cols])) < 3).all(axis=1)]
    print(f"Nakon uklanjanja outliera: {len(df)}")

    # 4. Uklanjanje negativnih vrijednosti za kolone gdje nema smisla (npr. pH, alcohol)
    for col in ['pH', 'alcohol', 'fixed_acidity', 'volatile_acidity']:
        if col in df.columns:
            df = df[df[col] >= 0]
    print(f"Nakon uklanjanja negativnih vrijednosti: {len(df)}")

    # 5. Normalizacija odabranih numeričkih kolona (Min-Max)
    for col in ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar', 'chlorides']:
        if col in df.columns:
            min_val = df[col].min()
            max_val = df[col].max()
            if max_val - min_val > 0:
                df[col] = (df[col] - min_val) / (max_val - min_val)

    # 6. Brza analiza: prikaz osnovne statistike
    print("\n📊 Statistika nakon čišćenja:")
    print(df.describe())

    return df