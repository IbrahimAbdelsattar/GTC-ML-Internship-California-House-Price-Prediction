import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load("house_price_model_lgm.pkl")

# App Title
st.title("🏠 House Price Prediction App")
st.write("This app predicts the **median house value** based on housing features.")

# Sidebar for input
st.sidebar.header("Input Features")

def user_input_features():
    longitude = st.sidebar.number_input("Longitude", -125.0, -114.0, -120.0)
    latitude = st.sidebar.number_input("Latitude", 32.0, 43.0, 35.0)
    housing_median_age = st.sidebar.slider("Housing Median Age", 1, 55, 20)
    total_rooms = st.sidebar.number_input("Total Rooms", 1, 50000, 2000)
    total_bedrooms = st.sidebar.number_input("Total Bedrooms", 1, 10000, 500)
    population = st.sidebar.number_input("Population", 1, 20000, 800)
    households = st.sidebar.number_input("Households", 1, 5000, 400)
    median_income = st.sidebar.slider("Median Income (10,000s)", 0.0, 15.0, 3.0)
    ocean_proximity = st.sidebar.selectbox("Ocean Proximity", 
                                           ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"])
    
    # Encode ocean_proximity (must match training preprocessing!)
    ocean_dict = {"<1H OCEAN":0, "INLAND":1, "ISLAND":2, "NEAR BAY":3, "NEAR OCEAN":4}
    ocean_encoded = ocean_dict[ocean_proximity]

    data = {
        'longitude': longitude,
        'latitude': latitude,
        'housing_median_age': housing_median_age,
        'total_rooms': total_rooms,
        'total_bedrooms': total_bedrooms,
        'population': population,
        'households': households,
        'median_income': median_income,
        'ocean_proximity': ocean_encoded
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

# Prediction
if st.button("Predict House Price"):
    prediction = model.predict(input_df)
    st.success(f"🏡 Predicted Median House Value: ${prediction[0]:,.2f}")
