import pandas as pd

def load_dataset(path: str) -> pd.DataFrame:
    df = pd.read_csv("data/winequality-red.csv")
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns.")
    return df