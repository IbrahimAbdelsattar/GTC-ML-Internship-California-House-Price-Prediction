import streamlit as st
import pandas as pd
import joblib
import os

# -------------------------------
# 1️⃣ Check if required files exist
# -------------------------------
required_files = ["house_price_model_lgm.pkl", "X_scaler.pkl", "y_scaler.pkl", "ocean_le.pkl"]

for f in required_files:
    if not os.path.exists(f):
        st.error(f"❌ Required file not found: {f}. Make sure it is in the app folder.")
        st.stop()  # stop execution if any file is missing

# -------------------------------
# 2️⃣ Load model, scalers, and LabelEncoder
# -------------------------------
model = joblib.load("house_price_model.pkl")
X_scaler = joblib.load("X_scaler.pkl")
y_scaler = joblib.load("y_scaler.pkl")
le = joblib.load("ocean_le.pkl")

# -------------------------------
# 3️⃣ Model features (must match training)
# -------------------------------
model_features = [
    'longitude', 'latitude', 'housing_median_age', 'total_rooms',
    'total_bedrooms', 'population', 'households', 'median_income', 'ocean_proximity'
]

# -------------------------------
# 4️⃣ App title and description
# -------------------------------
st.title("🏠 California House Price Prediction")
st.write("This app predicts the **median house value** based on housing features.")

# -------------------------------
# 5️⃣ Sidebar for user input
# -------------------------------
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
        le.classes_  # get categories from fitted LabelEncoder
    )

    # Encode ocean_proximity
    ocean_encoded = le.transform([ocean_input])[0]

    # Create dataframe
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

    df = pd.DataFrame(data, index=[0])

    # Scale numeric features
    numeric_features = ['longitude', 'latitude', 'housing_median_age', 'total_rooms',
                        'total_bedrooms', 'population', 'households', 'median_income']
    df[numeric_features] = X_scaler.transform(df[numeric_features])

    # Reorder columns to match model
    df = df[model_features]

    return df

input_df = user_input_features()

# Display user input
st.subheader("User Input Features")
st.write(input_df)

# -------------------------------
# 6️⃣ Prediction
# -------------------------------
if st.button("Predict House Price"):
    try:
        # Predict scaled target
        y_pred_scaled = model.predict(input_df)

        # Inverse transform to original house price
        y_pred = y_scaler.inverse_transform(y_pred_scaled.reshape(-1,1))

        st.success(f"🏡 Predicted Median House Value: ${y_pred[0,0]:,.2f}")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
