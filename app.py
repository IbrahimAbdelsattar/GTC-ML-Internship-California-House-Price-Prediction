import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

# App Title
st.title("🏠 California Housing Price Prediction")
st.write("Fill in the details below to predict the **Median House Value**.")

# Input Form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        longitude = st.number_input("Longitude", -125.0, -114.0, -120.0)
        latitude = st.number_input("Latitude", 32.0, 43.0, 35.0)
        housing_median_age = st.slider("Housing Median Age", 1, 55, 20)
        total_rooms = st.number_input("Total Rooms", 1, 50000, 2000)
        total_bedrooms = st.number_input("Total Bedrooms", 1, 10000, 500)
    
    with col2:
        population = st.number_input("Population", 1, 20000, 800)
        households = st.number_input("Households", 1, 5000, 400)
        median_income = st.slider("Median Income (10,000s)", 0.0, 15.0, 3.0)
        ocean_proximity = st.selectbox(
            "Ocean Proximity", 
            ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
        )
    
    # Submit button inside form
    submit_button = st.form_submit_button("Predict House Price")

# Encode categorical variable
ocean_dict = {"<1H OCEAN":0, "INLAND":1, "ISLAND":2, "NEAR BAY":3, "NEAR OCEAN":4}
ocean_encoded = ocean_dict[ocean_proximity]

# Build dataframe for prediction
input_df = pd.DataFrame({
    "longitude": [longitude],
    "latitude": [latitude],
    "housing_median_age": [housing_median_age],
    "total_rooms": [total_rooms],
    "total_bedrooms": [total_bedrooms],
    "population": [population],
    "households": [households],
    "median_income": [median_income],
    "ocean_proximity": [ocean_encoded]
})

# Prediction
if submit_button:
    prediction = model.predict(input_df)
    price_usd = prediction[0] * 100000  # Convert back to USD
    st.success(f"🏡 Predicted Median House Value: ${price_usd:,.0f}")
