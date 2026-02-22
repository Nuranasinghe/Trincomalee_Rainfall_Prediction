import streamlit as st
import pandas as pd
from src.predict import load_model

# Load the model
model = load_model("models/rainfall_model.pkl")

st.set_page_config(
    page_title="Trincomalee Rainfall Predictor",
    page_icon="🌧️",
    layout="wide"
)

st.markdown(
    "<h1 style='text-align: center; color: white;'>🌧 Trincomalee Rainfall Prediction 🌦</h1>",
    unsafe_allow_html=True
)
st.markdown("---")

# Sidebar Inputs

st.sidebar.header("Enter Weather Data")

month = st.sidebar.number_input("Month", 1, 12, value=1)
year = st.sidebar.number_input("Year", 2024, 2030, value=2024)
lag1 = st.sidebar.number_input("Previous Month Rainfall (mm)", value=100)
temp = st.sidebar.number_input("Mean Temperature (°C)", value=28.0)
radiation = st.sidebar.number_input("Radiation (MJ/m²)", value=20.0)
et0 = st.sidebar.number_input("Evapotranspiration (mm)", value=4.0)
elevation = st.sidebar.number_input("Elevation (m)", value=5)

 
model_input = pd.DataFrame({
    'month': [month],
    'year': [year],
    'rainfall_lag1': [lag1],
    'apparent_temperature_mean': [temp],
    'shortwave_radiation_sum': [radiation],
    'et0_fao_evapotranspiration': [et0],
    'elevation': [elevation]
})

display_input = pd.DataFrame({
    'Previous Month Rainfall (mm)': [lag1],
    'Mean Temperature (°C)': [temp],
    'Radiation (MJ/m²)': [radiation],
    'Evapotranspiration (mm)': [et0],
    'Elevation (m)': [elevation]
})

# Display table
st.subheader("Your Input Data")
col1, col2 = st.columns(2)

col1.markdown(f"<h3>Year: {year}</h3>", unsafe_allow_html=True)
col2.markdown(f"<h3>Month: {month}</h3>", unsafe_allow_html=True)
st.table(display_input)

 
if st.button("Predict Rainfall"):
    prediction = model.predict(model_input)
    st.markdown(
        f"<h2 style='text-align: center; color: darkblue;'>🌧 Predicted Rainfall: {prediction[0]:.2f} mm</h2>",
        unsafe_allow_html=True
    )
  