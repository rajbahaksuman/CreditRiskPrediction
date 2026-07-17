import numpy as np
import joblib
import streamlit as st

model = joblib.load('model.pkl')

st.title("Credit Risk Prediction")

st.divider()

age = st.number_input("Enter your age ", min_value=0.0)

ed = st.number_input("Enter your ed ", value=0.0)

employ = st.number_input("Enter your Employeee number ",value=0.0)

address = st.number_input("Enter your address number",value=0.0)

income = st.number_input("Enter your income ", value=0.0)

debtinc = st.number_input("Enter your debit income",value=0.0)

creddebt = st.number_input("Enter yoour credit debt", value=0.0)

otherdebt = st.number_input("Enter your other debt ", value=0.0)

Predictbutton = st.button('Predict')

st.divider()

if Predictbutton:
    features = np.array([[age, ed, employ, address, income, debtinc, creddebt, otherdebt]])
    prediction = model.predict(features)[0]

    st.success(f"Default value is: {prediction}")

else:
    st.write("Please enter the values and use predict button")



