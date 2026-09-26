<div align="center">

# 💰 Loan Approval Prediction

### 🤖 Machine Learning • Streamlit • Supabase

**An end-to-end Machine Learning application that predicts loan approval using Logistic Regression and provides a real-time web interface with database integration.**

<br>

<a href="YOUR_STREAMLIT_APP_URL">
  <img src="https://img.shields.io/badge/🚀%20LIVE%20DEMO-00C853?style=for-the-badge&logo=streamlit&logoColor=white" alt="Live Demo"/>
</a>
&nbsp;
<a href="YOUR_GITHUB_REPOSITORY_URL">
  <img src="https://img.shields.io/badge/💻%20SOURCE%20CODE-181717?style=for-the-badge&logo=github&logoColor=white" alt="Source Code"/>
</a>

<br><br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
<img src="https://img.shields.io/badge/Supabase-Database-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/GitHub-Version%20Control-181717?style=for-the-badge&logo=github&logoColor=white"/>

</div>

---

## 🌟 Project Overview

**Loan Approval Prediction** is an end-to-end Machine Learning project that predicts whether a loan application is **Approved** or **Rejected** based on applicant information.

The project combines:

* 🧠 Machine Learning
* 🐍 Python
* 📊 Data preprocessing
* 🔤 One-Hot Encoding
* 📏 Feature scaling
* 🤖 Logistic Regression
* 🖥️ Streamlit
* 🗄️ Supabase
* ☁️ Cloud deployment

The application allows a user to enter applicant details, receive a prediction, and store the application information in a Supabase database.

---

# 🎯 Problem Statement

Loan applications contain multiple attributes such as:

* Applicant age
* Income
* Credit score
* Loan amount
* Loan term
* Employment type
* Existing loans

Evaluating these attributes manually can be time-consuming.

This project demonstrates how a classification model can learn patterns from historical loan application data and produce an **Approved / Rejected** prediction.

---

# 🚀 Project Objective

The main objectives are:

✅ Build a Logistic Regression classification model.

✅ Handle categorical features using One-Hot Encoding.

✅ Apply feature preprocessing before model training.

✅ Evaluate the classification model.

✅ Save the trained ML pipeline.

✅ Build an interactive Streamlit application.

✅ Store applicant information and predictions in Supabase.

✅ Deploy the application so it can be accessed online.

---

# 🧠 Machine Learning Workflow

```text
                 📊 Dataset
                     │
                     ▼
              🔍 Feature Selection
                     │
                     ▼
             ✂️ Train / Test Split
                     │
                     ▼
          🔤 Categorical Encoding
                     │
                     ▼
              📏 Feature Scaling
                     │
                     ▼
          🤖 Logistic Regression
                     │
                     ▼
              📈 Model Evaluation
                     │
                     ▼
               💾 Save Model
                     │
                     ▼
             🖥️ Streamlit App
                     │
                     ▼
             🔮 Loan Prediction
                     │
             ┌───────┴────────┐
             ▼                ▼
        ✅ APPROVED       ❌ REJECTED
             │                │
             └───────┬────────┘
                     ▼
              🗄️ Supabase
```

---

# 📋 Dataset Features

The model uses the following features:

| Feature           | Description              | Type        |
| ----------------- | ------------------------ | ----------- |
| `Age`             | Applicant age            | Numerical   |
| `Income`          | Applicant income         | Numerical   |
| `Credit_Score`    | Applicant credit score   | Numerical   |
| `Loan_Amount`     | Requested loan amount    | Numerical   |
| `Loan_Term`       | Loan repayment term      | Numerical   |
| `Employment_Type` | Employment category      | Categorical |
| `Existing_Loans`  | Number of existing loans | Numerical   |
| `Dependents`      | Number of dependents     | Numerical   |

### 🎯 Target

```text
Loan_Approved
```

The target represents the loan approval classification.

```text
1 → Approved
0 → Rejected
```

---

# 🔤 Feature Preprocessing

The dataset contains a categorical feature:

```text
Employment_Type
```

with values such as:

```text
Salaried
Self-employed
```

Instead of manually converting these values, the project uses:

```python
OneHotEncoder(handle_unknown="ignore")
```

This allows the model to process categorical values safely.

The preprocessing and model are combined into a pipeline:

```text
Input Data
    ↓
ColumnTransformer
    ↓
OneHotEncoder
    ↓
Numerical Features
    ↓
Logistic Regression
```

This also ensures that the **same preprocessing used during training is applied when making predictions in the Streamlit application**.

---

# 🤖 Machine Learning Model

## Logistic Regression

Logistic Regression is used because this project is a **binary classification problem**.

The model predicts two possible outcomes:

```text
0 → Loan Rejected
1 → Loan Approved
```

The model estimates the probability of an applicant belonging to the positive class.

### Model Pipeline

```python
Pipeline([
    ("preprocessing", preprocessor),
    ("logistic_regression", LogisticRegression())
])
```

---

# 📊 Model Evaluation

The model is evaluated using classification metrics such as:

* Accuracy
* Confusion Matrix
* Precision
* Recall
* F1-score

### Results

> Replace the values below with your **actual test results**.

| Metric    |            Score |
| --------- | ---------------: |
| Accuracy  |  `YOUR_ACCURACY` |
| Precision | `YOUR_PRECISION` |
| Recall    |    `YOUR_RECALL` |
| F1 Score  |  `YOUR_F1_SCORE` |

### Confusion Matrix

Add your actual confusion matrix screenshot here:

```text
📸 YOUR_CONFUSION_MATRIX_IMAGE
```

For example, you can upload the image into the repository and use:

```markdown
![Confusion Matrix](images/confusion_matrix.png)
```

---

# 🖥️ Application

The Streamlit application provides a simple interface where users can enter:

```text
👤 Name
🎂 Age
💰 Income
📊 Credit Score
💵 Loan Amount
📅 Loan Term
💼 Employment Type
🏦 Existing Loans
```

The user then clicks:

### 🔮 Check Loan Approval

The trained model generates the prediction.

---

# ✅ Prediction Output

### Approved

```text
╔══════════════════════════════╗
║      ✅ LOAN APPROVED        ║
╚══════════════════════════════╝
```

### Rejected

```text
╔══════════════════════════════╗
║      ❌ LOAN REJECTED        ║
╚══════════════════════════════╝
```

---

# 🗄️ Supabase Database

The application stores submitted loan applications in Supabase.

### Stored information

```text
name
age
income
credit_score
loan_amount
loan_term
employment_type
existing_loans
dependents
loan_approved
```

### Database Flow

```text
Streamlit
    │
    │ Applicant Details
    ▼
ML Model
    │
    │ Prediction
    ▼
Approved / Rejected
    │
    ▼
Supabase
    │
    ▼
loan_app table
```

Supabase credentials are stored using **Streamlit Secrets** and are not included in the source code.

---

# 🏗️ System Architecture

```text
                         👤 USER
                           │
                           ▼
                 ┌───────────────────┐
                 │     Streamlit     │
                 │    Frontend UI    │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   Input Validation│
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   ML Pipeline     │
                 │                   │
                 │ OneHotEncoder     │
                 │        +          │
                 │ Feature Scaling   │
                 │        +          │
                 │ LogisticRegression│
                 └─────────┬─────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   Prediction    │
                  └───────┬─────────┘
                          │
                  ┌───────┴───────┐
                  ▼               ▼
             ✅ APPROVED      ❌ REJECTED
                  │               │
                  └───────┬───────┘
                          ▼
                 ┌───────────────────┐
                 │     Supabase      │
                 │     Database      │
                 └───────────────────┘
```

---

# 📸 Application Screenshots

## 🏠 Loan Application

Add your Streamlit application screenshot here:

```markdown
![Loan Application](images/loan_application.png)
```

## ✅ Loan Approved

```markdown
![Loan Approved](images/loan_approved.png)
```

## ❌ Loan Rejected

```markdown
![Loan Rejected](images/loan_rejected.png)
```

## 🗄️ Supabase Database

```markdown
![Supabase Database](images/supabase_database.png)
```

---

# 🛠️ Technology Stack

<div align="center">

| Technology             | Purpose              |
| ---------------------- | -------------------- |
| 🐍 Python              | Programming          |
| 🐼 Pandas              | Data manipulation    |
| 🔢 NumPy               | Numerical operations |
| 🤖 Scikit-learn        | Machine Learning     |
| 📈 Logistic Regression | Classification       |
| 🔤 OneHotEncoder       | Categorical encoding |
| 📏 StandardScaler      | Feature scaling      |
| 🖥️ Streamlit          | Web application      |
| 🗄️ Supabase           | Database             |
| 💾 Joblib              | Model serialization  |
| 🐙 GitHub              | Version control      |
| ☁️ Streamlit Cloud     | Deployment           |

</div>

---

# 📂 Project Structure

```text
loan_application/
│
├── app.py
│
├── model.pkl
│
├── loan_approval_100_records.csv
│
├── requirements.txt
│
├── README.md
│
├── .gitignore
│
└── images/
    ├── loan_application.png
    ├── loan_approved.png
    ├── loan_rejected.png
    ├── confusion_matrix.png
    └── supabase_database.png
```

---

# ⚙️ Installation

## 1️⃣ Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2️⃣ Move into the project

```bash
cd loan_application
```

## 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Configure Supabase

Create Streamlit secrets:

```toml
SUPABASE_URL = "your_supabase_url"
SUPABASE_KEY = "your_supabase_key"
```

Do **not** commit your secrets to GitHub.

## 5️⃣ Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📦 Requirements

Example `requirements.txt`:

```text
streamlit
pandas
scikit-learn
joblib
supabase
```

If your trained model was created with a specific scikit-learn version, keep the training and deployment environments compatible.

---

# 🔐 Security

Sensitive credentials are not stored directly inside the source code.

Supabase credentials are loaded through:

```python
st.secrets["SUPABASE_URL"]
st.secrets["SUPABASE_KEY"]
```

The project should also include:

```text
.streamlit/secrets.toml
```

in `.gitignore`.

---

# 🚀 Deployment

The application can be deployed using **Streamlit Community Cloud**.

### Deployment flow

```text
GitHub Repository
       │
       ▼
Streamlit Community Cloud
       │
       ▼
Install requirements
       │
       ▼
Load model.pkl
       │
       ▼
Load Streamlit Secrets
       │
       ▼
🚀 Live Application
```

### 🌐 Live Application

**[🚀 Open Loan Approval Prediction App](YOUR_STREAMLIT_APP_URL)**

---

# 🧪 Example Prediction Flow

```text
Applicant
│
├── Age: 28
├── Income: 50000
├── Credit Score: 720
├── Loan Amount: 300000
├── Loan Term: 24
├── Employment: Salaried
└── Existing Loans: 1
        │
        ▼
   ML Pipeline
        │
        ▼
Logistic Regression
        │
        ▼
Prediction
        │
        ├── 1 → ✅ Approved
        │
        └── 0 → ❌ Rejected
```

---

# 💡 Key Learning Outcomes

Through this project, I worked with:

### 🧠 Machine Learning

* Supervised Learning
* Binary Classification
* Logistic Regression
* Train/Test Split
* Feature Selection
* Model Evaluation

### 📊 Data Preprocessing

* Categorical data
* One-Hot Encoding
* Feature scaling
* Data transformation
* ML pipelines

### 💻 Application Development

* Streamlit
* User input handling
* Model prediction
* Error handling
* Database integration

### 🗄️ Backend / Database

* Supabase
* PostgreSQL-backed data storage
* Application data insertion
* Secure credentials

### ☁️ Deployment

* Git
* GitHub
* Streamlit Community Cloud

---

# 🔮 Future Improvements

Potential future improvements include:

* 📊 Add probability/confidence display
* 📈 Add model performance dashboard
* 👤 Add user authentication
* 🔐 Add secure login/signup
* 📋 Add application history
* 🔎 Add search and filtering
* 📱 Improve responsive UI
* 🧠 Compare multiple classification algorithms
* 📊 Add feature importance / model interpretation
* 🗃️ Add an admin dashboard
* 📉 Monitor model performance over time

---

# 🎓 Project Type

```text
Machine Learning
        +
Classification
        +
Web Application
        +
Database
        +
Cloud Deployment
```

This project demonstrates an end-to-end workflow from **dataset → ML model → application → database → deployment**.

---

# 👨‍💻 Developer

<div align="center">

## Syed Arshad

**B.Tech — CSE (AI)**

Interested in:

`Machine Learning` • `Artificial Intelligence` • `Python` • `Data Analytics` • `Software Development`

<br>

<a href="YOUR_LINKEDIN_URL">
<img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
</a>

<a href="YOUR_GITHUB_PROFILE_URL">
<img src="https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge&logo=github&logoColor=white"/>
</a>

</div>

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Built with 🐍 Python + 🤖 Machine Learning + 🖥️ Streamlit + 🗄️ Supabase**

</div>
```

### Before pushing it to GitHub

Replace these placeholders:

```text
YOUR_STREAMLIT_APP_URL
YOUR_GITHUB_REPOSITORY_URL
YOUR_LINKEDIN_URL
YOUR_GITHUB_PROFILE_URL
YOUR_ACCURACY
YOUR_PRECISION
YOUR_RECALL
YOUR_F1_SCORE
```

And most importantly, add **4–5 real screenshots** in an `images` folder. That will make the README much more visually compelling than text alone.

For the strongest first impression, put your **Streamlit app screenshot immediately below the project title**, before the long technical sections.
