import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def filter_trincomalee(df):
    df = df[df['city'] == 'Trincomalee']
    return df

def clean_data(df):
    df = df.dropna()
    return df

def save_clean_data(df, path):
    df.to_csv(path, index=False)