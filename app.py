import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car.csv')
st.title("Welcome to Car Price Predictor 🚗")

# ---- Dropdown Data (customize as per your dataset) ----
companies = sorted(car['company'].unique())
models = sorted(car['name'].unique())
year= sorted(car['year'].unique(), reverse=True)
fuel_types = sorted(car['fuel_type'].unique())

# ---- UI Inputs ----
company = st.selectbox("Select Company:", companies)

name = st.selectbox("Select Model:", models)

year = st.selectbox("Select Year of Purchase:", year)

fuel_type = st.selectbox("Select Fuel Type:", fuel_types)

kms_driven = st.number_input("Enter Number of Kilometers travelled:", min_value=0)

# ---- Prediction Button ----
if st.button("Predict Price"):
    input_df = pd.DataFrame(
        [[name, company, year, kms_driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    )

    prediction = model.predict(input_df)

    st.success(f"Estimated Price: ₹ {int(prediction[0]):,}")