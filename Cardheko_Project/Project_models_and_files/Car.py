# import streamlit as st
# import joblib
# import pandas as pd
# from PIL import Image
# import os
# import pickle

# # Page configuration
# st.set_page_config(layout="wide", page_title="Car Dheko - Price Prediction", page_icon="🚗")

# # Title and description
# st.markdown(
#     '<p style="color: darkgreen; font-size: 30px; font-weight: bold; text-align: center;">Car Dheko - Used Car Price Predictor</p>',
#     unsafe_allow_html=True,
# )
# st.markdown(
#     '<p style="color: black; font-size: 20px; text-align: center;">Get an estimated price for your car based on specifications and history.</p>',
#     unsafe_allow_html=True,
# )

# # File paths
# logo_path = "D:/Projects/CarDheko/cardekho-logo.png"
# dataset_path = "D:/Projects/CarDheko/Preprocessed_dataset.csv"
# model_path = "D:/Projects/CarDheko/pipeline_model.pkl"  # <-- Fixed here

# # Load and display logo
# if os.path.exists(logo_path):
#     try:
#         logo_image = Image.open(logo_path)
#         st.image(logo_image, caption="Car Dekho", use_container_width=True)
#     except Exception as e:
#         st.warning(f"Error loading logo: {e}")
# else:
#     st.warning("Logo file not found.")

# # Load dataset
# def load_data():
#     if os.path.exists(dataset_path):
#         try:
#             return pd.read_csv(dataset_path)
#         except Exception as e:
#             st.error(f"Error reading dataset: {e}")
#             return None
#     else:
#         st.error("Dataset file not found.")
#         return None

# # Load model
# def load_model():
#     st.write("Model path exists:", os.path.exists(model_path))  # Debug line
#     if os.path.exists(model_path):
#         try:
#             with open(model_path, "rb") as file:
#                 return joblib.load(file)
#         except Exception as e:
#             st.error(f"Error loading model: {e}")
#             return None
#     else:
#         st.error("Model file not found.")
#         return None

# # Initialize
# df = load_data()
# model = load_model()

# # Main app logic
# if df is not None and model is not None:
#     st.sidebar.markdown("<p class='sidebar-content'><b>Car Specifications</b></p>", unsafe_allow_html=True)

#     # Sidebar inputs
#     brand = st.sidebar.selectbox("Car Brand", options=sorted(df['Brand'].dropna().unique()))
#     fuel_type = st.sidebar.selectbox("Fuel Type", ['Petrol', 'Diesel', 'Lpg', 'Cng', 'Electric'])
#     body_type = st.sidebar.selectbox("Body Type", sorted(df['body type'].dropna().unique()))

#     filtered_models = df[
#         (df['Brand'] == brand) &
#         (df['body type'] == body_type) &
#         (df['Fuel type'] == fuel_type)
#     ]['model'].dropna().unique()

#     car_model = st.sidebar.selectbox("Car Model", options=filtered_models if len(filtered_models) > 0 else ["No models available"])

#     transmission = st.sidebar.selectbox("Transmission", ['Manual', 'Automatic'])
#     seats = st.sidebar.selectbox("Seats", sorted(df['Seats'].dropna().unique()))
#     insurance_type = st.sidebar.selectbox("Insurance Type", df['Insurance Type'].dropna().unique())
#     color = st.sidebar.selectbox("Color", df['Color'].dropna().unique())
#     city = st.sidebar.selectbox("City", df['City'].dropna().unique())

#     # Numeric inputs
#     model_year = st.sidebar.number_input("Manufacturing Year", min_value=1980, max_value=2025, step=1)
#     mileage = st.sidebar.number_input("Mileage (in km/l)", min_value=1.0, max_value=50.0, step=0.1)
#     owner_no = st.sidebar.number_input("Owner Number", min_value=1, max_value=5, step=1)
#     kms_driven = st.sidebar.number_input("Kilometers Driven", min_value=100, max_value=1000000, step=1000)

#     # Predict button
#     if st.button("🚗 Predict Car Price"):
#         if car_model != "No models available":
#             input_data = pd.DataFrame({
#                 'Fuel type': [fuel_type],
#                 'body type': [body_type],
#                 'transmission': [transmission],
#                 'ownerNo': [owner_no],
#                 'Brand': [brand],
#                 'model': [car_model],
#                 'modelYear': [model_year],
#                 'Insurance Type': [insurance_type],
#                 'Kms Driven': [kms_driven],
#                 'Mileage': [mileage],
#                 'Seats': [seats],
#                 'Color': [color],
#                 'City': [city]
#             })

#             try:
#                 prediction = model.predict(input_data)
#                 st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")
#             except Exception as e:
#                 st.error(f"Prediction error: {e}")
#         else:
#             st.warning("Please select valid options for all fields.")

import streamlit as st
import joblib
import pandas as pd
from PIL import Image
import os

# Page configuration
st.set_page_config(layout="wide", page_title="Car Dheko - Price Prediction", page_icon="🚗")

# Title and description
st.markdown(
    '<p style="color: darkgreen; font-size: 30px; font-weight: bold; text-align: center;">Car Dheko - Used Car Price Predictor</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="color: black; font-size: 20px; text-align: center;">Get an estimated price for your car based on specifications and history.</p>',
    unsafe_allow_html=True,
)

# File paths
logo_path = "D:/Projects/CarDheko/cardekho-logo.png"
dataset_path = "D:/Projects/CarDheko/Preprocessed_dataset.csv"
model_path = "D:/Projects/CarDheko/pipeline_model.pkl"

# Load and display logo
if os.path.exists(logo_path):
    try:
        logo_image = Image.open(logo_path)
        st.image(logo_image, caption="Car Dekho", use_container_width=True)
    except Exception as e:
        st.warning(f"Error loading logo: {e}")
else:
    st.warning("Logo file not found.")

# Load dataset
def load_data():
    if os.path.exists(dataset_path):
        try:
            return pd.read_csv(dataset_path)
        except Exception as e:
            st.error(f"Error reading dataset: {e}")
            return None
    else:
        st.error("Dataset file not found.")
        return None

# Load model
def load_model():
    if os.path.exists(model_path):
        try:
            with open(model_path, "rb") as file:
                return joblib.load(file)
        except Exception as e:
            st.error(f"Error loading model: {e}")
            return None
    else:
        st.error("Model file not found.")
        return None

# Initialize
df = load_data()
model = load_model()

# Main app logic
if df is not None and model is not None:
    st.sidebar.markdown("<p class='sidebar-content'><b>Car Specifications</b></p>", unsafe_allow_html=True)

    # Step 1: Brand selection
    brand = st.sidebar.selectbox("Car Brand", options=sorted(df['Brand'].dropna().unique()))

    # Step 2: Filter models by brand
    filtered_models = df[df['Brand'] == brand]['model'].dropna().unique()
    car_model = st.sidebar.selectbox("Car Model", options=filtered_models)

    # Step 3: Filter remaining fields based on Brand and Model
    filtered_df = df[(df['Brand'] == brand) & (df['model'] == car_model)]

    fuel_type = st.sidebar.selectbox("Fuel Type", sorted(filtered_df['Fuel type'].dropna().unique()))
    body_type = st.sidebar.selectbox("Body Type", sorted(filtered_df['body type'].dropna().unique()))
    transmission = st.sidebar.selectbox("Transmission", sorted(filtered_df['transmission'].dropna().unique()))
    seats = st.sidebar.selectbox("Seats", sorted(filtered_df['Seats'].dropna().unique()))
    insurance_type = st.sidebar.selectbox("Insurance Type", sorted(filtered_df['Insurance Type'].dropna().unique()))
    color = st.sidebar.selectbox("Color", sorted(filtered_df['Color'].dropna().unique()))
    city = st.sidebar.selectbox("City", sorted(filtered_df['City'].dropna().unique()))

    # Numeric inputs
    model_year = st.sidebar.number_input("Manufacturing Year", min_value=1980, max_value=2025, step=1)
    mileage = st.sidebar.number_input("Mileage (in km/l)", min_value=11.0, max_value=50.0, step=0.1)
    owner_no = st.sidebar.number_input("Owner Number", min_value=1, max_value=5, step=1)
    kms_driven = st.sidebar.number_input("Kilometers Driven", min_value=100, max_value=1000000, step=1000)

    # Predict button
    if st.button("🚗 Predict Car Price"):
        input_data = pd.DataFrame({
            'Fuel type': [fuel_type],
            'body type': [body_type],
            'transmission': [transmission],
            'ownerNo': [owner_no],
            'Brand': [brand],
            'model': [car_model],
            'modelYear': [model_year],
            'Insurance Type': [insurance_type],
            'Kms Driven': [kms_driven],
            'Mileage': [mileage],
            'Seats': [seats],
            'Color': [color],
            'City': [city]
        })

        try:
            prediction = model.predict(input_data)
            st.success(f"Estimated Price: ₹ {prediction[0]:,.2f}")
        except Exception as e:
            st.error(f"Prediction error: {e}")
