def clean_dataset(df):
    df = df.drop_duplicates()
    df = df.fillna(0)
    return df