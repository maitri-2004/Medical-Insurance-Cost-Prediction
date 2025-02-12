# -- coding: utf-8 --
"""
Created on MON FEB 2

@author: MAITRI
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib


DATA_PATH = "E:/ML/medical insurance/insurance.csv"
MODEL_PATH = "E:/ML/medical insurance/medical_insurance.sav"

data = pd.read_csv(DATA_PATH)

# Load trained model
model = joblib.load(MODEL_PATH)

# Streamlit UI
st.title("Medical Insurance Cost Prediction")
st.write("Enter your details below to predict the insurance cost.")

# User input fields (No default values)
age = st.text_input("Age", "")
sex = st.selectbox("Sex", ("Select", "Male", "Female"))
bmi = st.text_input("BMI (Body Mass Index)", "")
children = st.text_input("Number of Children", "")
smoker = st.selectbox("Smoker", ("Select", "Yes", "No"))
region = st.selectbox("Region", ("Select", "Southwest", "Southeast", "Northwest", "Northeast"))

# Ensure all inputs are valid before prediction
if st.button("Predict Cost"):
    if not age or not bmi or not children or sex == "Select" or smoker == "Select" or region == "Select":
        st.error("Please fill in all fields correctly.")
    else:
        # Convert inputs
        age = int(age)
        bmi = float(bmi)
        children = int(children)
        sex = 0 if sex == "Male" else 1
        smoker = 0 if smoker == "Yes" else 1
        region_dict = {"Southeast": 0, "Southwest": 1, "Northeast": 2, "Northwest": 3}
        region = region_dict[region]

        # Predict
        input_data = np.array([[age, sex, bmi, children, smoker, region]])
        prediction = model.predict(input_data)[0]
        st.success(f"Estimated Insurance Cost: ${prediction:.2f}")
