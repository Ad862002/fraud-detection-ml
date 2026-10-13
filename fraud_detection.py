import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("fraud_detection_pipeline.pkl")

# App title
st.title("Fraud Detection Prediction App")

st.markdown("Please enter the transaction details and use the predict button.")

st.divider()

# Transaction type
transaction_type = st.selectbox(
    "Transaction Type",
    ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"]
)

# Transaction amount
amount = st.number_input(
    "Amount",
    min_value=0.0,
    value=1000.0
)

# Sender's old balance
oldbalanceOrg = st.number_input(
    "Old Balance (Sender)",
    min_value=0.0,
    value=10000.0
)

# Sender's new balance
newbalanceOrig = st.number_input(
    "New Balance (Sender)",
    min_value=0.0,
    value=9000.0
)

# Receiver's old balance
oldbalanceDest = st.number_input(
    "Old Balance (Receiver)",
    min_value=0.0,
    value=0.0
)

# Receiver's new balance
newbalanceDest = st.number_input(
    "New Balance (Receiver)",
    min_value=0.0,
    value=0.0
)

# Prediction button
if st.button("Predict"):

    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("This transaction can be fraud.")
    else:
        st.success("This transaction looks like it is not a fraud.")