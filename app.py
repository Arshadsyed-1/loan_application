import streamlit as st
import pandas as pd
import joblib
from supabase import create_client

st.set_page_config(
    page_title="Loan Approval",
    page_icon="💰"
)

model = joblib.load("model.pkl")

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

st.title("💰 Loan Approval Prediction")
st.write("Enter applicant details")

age_input = st.text_input("Age")
income_input = st.text_input("Income")
credit_input = st.text_input("Credit Score")
loan_amount_input = st.text_input("Loan Amount")
loan_term_input = st.text_input("Loan Term")

employment = st.selectbox(
    "Employment Type",
    ["","Salaried", "Self-employed"]
)

existing_loans_input = st.text_input("Existing Loans")

if st.button("Check Loan Approval"):

    if (
        not age_input
        or not income_input
        or not credit_input
        or not loan_amount_input
        or not loan_term_input
        or not existing_loans_input
    ):
        st.warning("Please enter all details.")

    else:
        age = int(age_input)
        income = int(income_input)
        credit_score = int(credit_input)
        loan_amount = int(loan_amount_input)
        loan_term = int(loan_term_input)
        existing_loans = int(existing_loans_input)

        new_applicant = pd.DataFrame({
            "Age": [age],
            "Income": [income],
            "Credit_Score": [credit_score],
            "Loan_Amount": [loan_amount],
            "Loan_Term": [loan_term],
            "Employment_Type": [employment],
            "Existing_Loans": [existing_loans]
        })

        result = model.predict(new_applicant)

        approved = bool(result[0] == 1)

        data = {
            "age": age,
            "income": income,
            "credit_score": credit_score,
            "loan_amount": loan_amount,
            "loan_term": loan_term,
            "employment_type": employment,
            "existing_loans": existing_loans,
            "loan_approved": approved
        }

        try:
            supabase.table("loan_app").insert(data).execute()

            if approved:
                st.success("✅ LOAN APPROVED")
            else:
                st.error("❌ LOAN REJECTED")

        except Exception as e:
            st.error(f"Database Error: {e}") 