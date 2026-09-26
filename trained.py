import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
# Load data
df = pd.read_csv("loan_approval_100_records.csv")


# Features
X = df[
    [
        "Age",
        "Income",
        "Credit_Score",
        "Loan_Amount",
        "Loan_Term",
        "Employment_Type",
        "Existing_Loans",
    ]
]


# Target
y = df["Loan_Approved"]


# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Columns
categorical_columns = ["Employment_Type"]

numerical_columns = [
    "Age",
    "Income",
    "Credit_Score",
    "Loan_Amount",
    "Loan_Term",
    "Existing_Loans"
]


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        ),
        (
            "numerical",
            StandardScaler(),
            numerical_columns
        )
    ]
)


# Pipeline
model = Pipeline([
    ("preprocessing", preprocessor),
    ("logistic_regression", LogisticRegression(max_iter=1000))
])


# Train
model.fit(X_train, y_train)


# Save
joblib.dump(model, "model.pkl")

print("Model saved successfully!")