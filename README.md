# 🌩️ Storm Prediction System (Machine Learning + Streamlit + OpenWeather API)

This project is a **Storm Prediction System** that uses **Machine Learning**, **Weather API integration**, and a **Streamlit Web App** to predict whether a storm is expected based on real-time weather parameters.

The system fetches **3-day weather forecasts** for multiple cities using the **OpenWeatherMap API**, preprocesses the data, and predicts storm occurrence using a trained **Random Forest Classifier**.

---

## 🚀 Features

### 🔹 1. Weather Data Fetching (OpenWeatherMap)
- Fetch **3-day future weather forecast**
- Collects:
  - Temperature
  - Humidity
  - Pressure
  - Wind Speed

### 🔹 2. Machine Learning Model
- ML model: **Random Forest Classifier**
- Scaler: **StandardScaler**
- Files generated:
  - `storm_prediction_model.pkl`
  - `scaler.pkl`

### 🔹 3. Visualizations
Using **Matplotlib** and **Seaborn**:
- Wind Speed Forecast (Line Plot)
- Temperature Forecast (Bar Chart)

### 🔹 4. Streamlit Web Application
- Predicts storm using:
  - Temperature  
  - Humidity  
  - Pressure  
  - Wind Speed  
- Output:
  - 🌪️ Storm Expected  
  - ✅ No Storm  

### 🔹 5. Ngrok Integration
- Enables **public URL** sharing for hosting Streamlit app
- Useful for:
  - Mobile demo
  - College project presentation
  - Sharing with faculty

---

## 📁 Project Structure

