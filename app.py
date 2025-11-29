import streamlit as st
import pandas as pd
import numpy as np
import joblib

# -----------------------------
# Load Model & Scaler
# -----------------------------
model = joblib.load("storm_prediction_model.pkl")
scaler = joblib.load("scaler.pkl")

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Storm Prediction System", page_icon="🌩️")

st.title("🌩️ Storm Prediction System")
st.write("Enter the weather parameters below to check if a storm is expected.")

# Input fields
temp = st.number_input("Temperature (°C)", min_value=-50.0, max_value=60.0, value=30.0)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=70.0)
pressure = st.number_input("Pressure (hPa)", min_value=800.0, max_value=1100.0, value=1010.0)
wind_speed = st.number_input("Wind Speed (m/s)", min_value=0.0, max_value=100.0, value=5.0)

# Predict Button
if st.button("Predict Storm"):
    input_data = pd.DataFrame([[temp, humidity, pressure, wind_speed]], 
                              columns=["Temperature", "Humidity", "Pressure", "Wind Speed"])
    
    # Scaling
    scaled_input = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(scaled_input)

    # Display result
    if prediction[0] == 1:
        st.error("🌪️ **Storm Expected**")
    else:
        st.success("✅ **No Storm — Weather Looks Normal**")

st.write("---")
st.caption("Developed using Streamlit · Machine Learning · OpenWeather API")
