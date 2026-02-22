import pandas as pd

def create_features(df):
    df['date'] = pd.to_datetime(df['time'])
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    
    # Lag feature (previous rainfall)
    df['rainfall_lag1'] = df['rain_sum'].shift(1)
    
    df = df.dropna()
    return df