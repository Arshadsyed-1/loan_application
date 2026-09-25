import streamlit as st
import pandas as pd
import joblib


# Load model
model = joblib.load("model.pkl")


from supabase import create_client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


st.set_page_config(
    page_title="Loan Approval",
    page_icon="💰"
)


st.title("💰 Loan Approval Prediction")
st.write("Enter applicant details")


age = st.number_input("Age")

income = st.number_input("Income")

credit_score = st.number_input(
    "Credit Score"
)

loan_amount = st.number_input(
    "Loan Amount"
)

loan_term = st.number_input(
    "Loan Term (Months)"
)

employment = st.selectbox(
    "Employment Type",
    [" ","Salaried", "Self-employed"]
)

existing_loans = st.number_input(
    "Existing Loans")



if st.button("Check Loan Approval"):

    new_applicant = pd.DataFrame({
        "Age": [age],
        "Income": [income],
        "Credit_Score": [credit_score],
        "Loan_Amount": [loan_amount],
        "Loan_Term": [loan_term],
        "Employment_Type": [employment],
        "Existing_Loans": [existing_loans],
    })

    # Model prediction
    result = model.predict(new_applicant)

    # Convert prediction to True/False
    approved = bool(result[0] == 1)

    # Save to Supabase
    data = {
    "age": int(age),
    "income": int(income),
    "credit_score": int(credit_score),
    "loan_amount": int(loan_amount),
    "loan_term": int(loan_term),
    "employment_type": str(employment),
    "existing_loans": int(existing_loans),
    "loan_approved": bool(approved)
}

try:
    response = supabase.table("loan_app").insert(data).execute()

    st.success("Application saved successfully!")

except Exception as e:
    st.error(f"Supabase Error: {e}")