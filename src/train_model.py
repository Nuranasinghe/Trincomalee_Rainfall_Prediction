from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

def train(df):
     
    X = df[
    [
        'month',
        'year',
        'rainfall_lag1',
        'apparent_temperature_mean',
        'shortwave_radiation_sum',
        'et0_fao_evapotranspiration',
        'elevation'
    ]
]
    y = df['rain_sum']
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    return model, X_test, y_test

def save_model(model, path):
    with open(path, 'wb') as f:
        pickle.dump(model, f)