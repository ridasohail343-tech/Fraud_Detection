import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("fraud_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Credit Card Fraud Detection")

st.write("Enter transaction details:")

features = []

for i in range(30):
    value = st.number_input(f"Feature {i + 1}", value=0.0)
    features.append(value)

if st.button("Predict"):
    data = np.array(features).reshape(1, -1)

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Fraudulent Transaction")
    else:
        st.success("Normal Transaction")