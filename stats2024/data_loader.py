import pandas as pd 

def load(filename: str) -> pd.DataFrame:
    return pd.read_csv(f'data/{filename}')
    