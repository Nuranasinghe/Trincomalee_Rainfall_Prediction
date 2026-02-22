from src.data_preprocessing import *
from src.feature_engineering import *
from src.train_model import *
from src.evaluate_model import *


import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np


def main():
    df = load_data("data/raw/SriLanka_Weather_Dataset_V1.csv")
    df = filter_trincomalee(df)
    df = clean_data(df)
    df = create_features(df)
    
    save_clean_data(df, "data/processed/cleaned_weather.csv")
    
    model, X_test, y_test = train(df)
    y_pred = model.predict(X_test)
    evaluate(model, X_test, y_test)
    save_model(model, "models/rainfall_model.pkl")

    # print("MAE:", mean_absolute_error(y_test, y_pred))
    # print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
    # print("R2 Score:", r2_score(y_test, y_pred))

    # Actual vs Predicted Plot
    plt.figure(figsize=(6,6))
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Rainfall")
    plt.ylabel("Predicted Rainfall")
    plt.title("Actual vs Predicted Rainfall")

    plt.plot([y_test.min(), y_test.max()],
             [y_test.min(), y_test.max()],
             color='red')

    plt.show()

if __name__ == "__main__":
    main()