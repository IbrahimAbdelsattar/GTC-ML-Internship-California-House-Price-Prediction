import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

# List of model features (must match training exactly)
model_features = [
    'longitude', 'latitude', 'housing_median_age', 'total_rooms',
    'total_bedrooms', 'population', 'households', 'median_income',
    'ocean_proximity_INLAND', 'ocean_proximity_ISLAND',
    'ocean_proximity_NEAR BAY', 'ocean_proximity_NEAR OCEAN'
]

# App Title
st.title("🏠 House Price Prediction App")
st.write("This app predicts the **median house value** based on housing features.")

# Sidebar for input
st.sidebar.header("Input Features")

def user_input_features():
    # Numeric inputs
    longitude = st.sidebar.number_input("Longitude", -125.0, -114.0, -120.0)
    latitude = st.sidebar.number_input("Latitude", 32.0, 43.0, 35.0)
    housing_median_age = st.sidebar.slider("Housing Median Age", 1, 55, 20)
    total_rooms = st.sidebar.number_input("Total Rooms", 1, 50000, 2000)
    total_bedrooms = st.sidebar.number_input("Total Bedrooms", 1, 10000, 500)
    population = st.sidebar.number_input("Population", 1, 20000, 800)
    households = st.sidebar.number_input("Households", 1, 5000, 400)
    median_income = st.sidebar.slider("Median Income (10,000s)", 0.0, 15.0, 3.0)

    # Categorical input
    ocean_input = st.sidebar.selectbox(
        "Ocean Proximity",
        ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
    )

    # Create base dataframe
    data = {
        'longitude': longitude,
        'latitude': latitude,
        'housing_median_age': housing_median_age,
        'total_rooms': total_rooms,
        'total_bedrooms': total_bedrooms,
        'population': population,
        'households': households,
        'median_income': median_income
    }

    df = pd.DataFrame(data, index=[0])

    # One-hot encode ocean_proximity (drop <1H OCEAN as reference)
    ocean_categories = ["INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"]
    for ocean in ocean_categories:
        df[f'ocean_proximity_{ocean}'] = 1 if ocean_input == ocean else 0

    # Reorder columns to match model features
    df = df[model_features]

    return df

input_df = user_input_features()

# Prediction
if st.button("Predict House Price"):
    try:
        prediction = model.predict(input_df)
        st.success(f"🏡 Predicted Median House Value: ${prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
