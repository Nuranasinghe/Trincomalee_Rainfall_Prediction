# Trincomalee Rainfall Prediction using Machine Learning

A machine learning project that predicts **monthly rainfall in Trincomalee, Sri Lanka** using historical weather data.  
The model is built using **Random Forest Regression** and deployed via a **Streamlit web application**.


# Project Overview

Rainfall prediction is essential for:

- Agricultural planning  
- Flood and drought management  
- Water resource optimization  
- Climate monitoring  

This project uses meteorological features such as temperature, radiation, evapotranspiration, and previous month rainfall to predict monthly rainfall amounts.


# Project Structure

Trincomalee_Rainfall_Prediction/
│
├── data/
│ ├── raw/
│ │ └── SriLanka_Weather_Dataset_V1.csv
│ └── processed/
│ └── cleaned_weather.csv
│
├── notebooks/
│ └── EDA.ipynb
│
├── src/
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── train_model.py
│ ├── evaluate_model.py
│ └── predict.py
│
├── models/
│ └── rainfall_model.pkl
│
├── app/
│ └── app.py
│
├── requirements.txt
├── main.py
└── README.md




# Dataset Information

# Data Source
The dataset utilized in this study was collected from publicly accessible databases. The selected dataset includes climate-related observations from selected cities in Sri Lanka spanning the period between January 2010 and January 2023.

# Dataset Size
The complete dataset consists of 147,481 observations(rows) collected from selected cities in Sri Lanka. After filtering the data for Trincomalee city, a total of 4,915 records were retained for analysis.
 

# Target Variable
- `rain_sum` → Monthly rainfall (mm)

# Features Used
- `month`
- `year`
- `rainfall_lag1`
- `apparent_temperature_mean`
- `shortwave_radiation_sum`
- `et0_fao_evapotranspiration`
- `elevation`


# Data Preprocessing

- Filtered dataset for **Trincomalee**
- Removed missing values
- Created lag feature (`rainfall_lag1`)
- No normalization required (tree-based model)


# Model Used

Algorithm: Random Forest Regressor  

# Hyperparameters:
- `n_estimators = 100`
- `random_state = 42`

Random Forest was chosen because:

- Handles nonlinear relationships
- Reduces overfitting
- Works well with structured/tabular data
- Provides feature importance for interpretation



#  Model Evaluation

The model was evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

#  Results

| Metric | Value |
|--------|--------|
| MAE | 2.237 |
| RMSE | 5.482 |
| R² Score | 0.617 |

**Interpretation:**

- The model explains approximately **61.7%** of rainfall variance.
- Average prediction error is approximately **2.24 mm**.



## 🧠 Model Explainability

Feature importance analysis shows that:

- `rainfall_lag1` (previous month rainfall) is highly influential.
- Temperature and radiation significantly impact rainfall.
- Results align with meteorological knowledge (temporal rainfall patterns).


##  Running the Project

# Clone Repository

git clone <your-repository-link>
cd Trincomalee_Rainfall_Prediction

# Install Requirments

pip install -r requirements.txt

# Train Model
python main.py

# Run Steamlit App
python -m streamlit run app/app.py

