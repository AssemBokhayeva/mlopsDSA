import streamlit as st
import requests

st.title("Bank Marketing Predictor")

age = st.slider("Age", 18, 80)
balance = st.number_input("Balance")
duration = st.number_input("Call duration")
campaign = st.number_input("Number of contacts")

if st.button("Predict"):

    data = {
        "age": age,
        "balance": balance,
        "duration": duration,
        "campaign": campaign
    }

    response = requests.post(
        "http://localhost:8000/predict",
        json=data
    )

    prediction = response.json()["prediction"]

    if prediction == 1:
        st.success("Client will subscribe")
    else:
        st.error("Client will not subscribe")
        