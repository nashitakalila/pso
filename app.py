from flask import Flask, request, render_template
import streamlit as st
import pandas as pd

# Load the dataset
data = pd.read_csv('healthcare-dataset-stroke-data.csv')

# Function to make predictions based on input data
def predict_stroke(age, avg_glucose_level, bmi, gender, ever_married, work_type, residence_type, smoking_status):
    result = data[
        (data['age'] == age) &
        (data['avg_glucose_level'] == avg_glucose_level) &
        (data['bmi'] == bmi) &
        (data['gender'].str.lower() == gender.lower()) &
        (data['ever_married'].str.lower() == ever_married.lower()) &
        (data['work_type'].str.lower() == work_type.lower()) &
        (data['residence_type'].str.lower() == residence_type.lower()) &
        (data['smoking_status'].str.lower() == smoking_status.lower())
    ]

    if not result.empty:
        return result.iloc[0]['stroke']
    else:
        return 'Data tidak ditemukan'

# Streamlit UI
st.title('Stroke Prediction App')

st.header('Input Patient Data')
age = st.number_input('Age', min_value=0, max_value=120, step=1)
avg_glucose_level = st.number_input('Average Glucose Level', min_value=0.0, step=0.1)
bmi = st.number_input('BMI', min_value=0.0, step=0.1)
gender = st.selectbox('Gender', options=['Male', 'Female'])
ever_married = st.selectbox('Ever Married', options=['Yes', 'No'])
work_type = st.selectbox('Work Type', options=['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked'])
residence_type = st.selectbox('Residence Type', options=['Urban', 'Rural'])
smoking_status = st.selectbox('Smoking Status', options=['smokes', 'formerly smoked', 'never smoked', 'Unknown'])

if st.button('Predict'):
    prediction = predict_stroke(age, avg_glucose_level, bmi, gender, ever_married, work_type, residence_type, smoking_status)
    st.write(f'Prediction: {prediction}')