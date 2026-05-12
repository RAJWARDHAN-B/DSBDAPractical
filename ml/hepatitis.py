# ============================================================
# HEPATITIS DATASET ANALYSIS
# ============================================================
# Operations:
# q. Data Cleaning
# r. Error Correction (Outlier Detection & Removal)
# s. Data Transformation
# t. Build Models:
#       1. Regression
#       2. Naive Bayes
#    Compare Accuracy
# ============================================================

# =========================
# STEP 1: IMPORT LIBRARIES
# =========================

import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# =========================
# STEP 2: LOAD DATASET
# =========================

# Replace with your filename
# Example: hepatitis.csv

df = pd.read_csv("hepatitis.csv", header=None)

# =========================
# STEP 3: ADD COLUMN NAMES
# =========================

columns = [
    "Class",
    "Age",
    "Sex",
    "Steroid",
    "Antivirals",
    "Fatigue",
    "Malaise",
    "Anorexia",
    "LiverBig",
    "LiverFirm",
    "SpleenPalpable",
    "Spiders",
    "Ascites",
    "Varices",
    "Bilirubin",
    "AlkPhosphate",
    "Sgot",
    "Albumin",
    "Protime",
    "Histology"
]

df.columns = columns

print("\n================ ORIGINAL DATA ================\n")
print(df.head())

# ============================================================
# q. DATA CLEANING
# ============================================================

# =========================
# STEP 4: REPLACE ? WITH NaN
# =========================

df.replace("?", np.nan, inplace=True)

# =========================
# STEP 5: CONVERT TO NUMERIC
# =========================

for col in df.columns:
    df[col] = pd.to_numeric(df[col])

# =========================
# STEP 6: CHECK MISSING VALUES
# =========================

print("\n================ MISSING VALUES ================\n")
print(df.isnull().sum())

# =========================
# STEP 7: HANDLE MISSING VALUES
# =========================
# Fill missing values with median

imputer = SimpleImputer(strategy="median")

df_imputed = pd.DataFrame(
    imputer.fit_transform(df),
    columns=df.columns
)

print("\n================ CLEANED DATA ================\n")
print(df_imputed.head())

# =========================
# STEP 8: REMOVE NEGATIVE VALUES
# =========================

numeric_cols = df_imputed.columns

for col in numeric_cols:
    df_imputed = df_imputed[df_imputed[col] >= 0]

print("\nNegative values removed.")

# ============================================================
# r. ERROR CORRECTING
# OUTLIER DETECTION & REMOVAL
# ============================================================

# Using IQR Method

def remove_outliers_iqr(data):

    clean_data = data.copy()

    for col in clean_data.columns:

        Q1 = clean_data[col].quantile(0.25)
        Q3 = clean_data[col].quantile(0.75)

        IQR = Q3 - Q1

        lower = Q1 - 1.5 * IQR
        upper = Q3 + 1.5 * IQR

        clean_data = clean_data[
            (clean_data[col] >= lower) &
            (clean_data[col] <= upper)
        ]

    return clean_data

df_no_outliers = remove_outliers_iqr(df_imputed)

print("\n================ DATA AFTER OUTLIER REMOVAL ================\n")
print(df_no_outliers.shape)

# ============================================================
# s. DATA TRANSFORMATION
# ============================================================

# =========================
# STEP 9: FEATURE / TARGET SPLIT
# =========================

X = df_no_outliers.drop("Class", axis=1)

y = df_no_outliers["Class"]

# =========================
# STEP 10: STANDARDIZATION
# =========================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# =========================
# STEP 11: TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# ============================================================
# t. MODEL BUILDING
# ============================================================

# ============================================================
# MODEL 1: LOGISTIC REGRESSION
# ============================================================

log_model = LogisticRegression()

log_model.fit(X_train, y_train)

y_pred_log = log_model.predict(X_test)

# =========================
# LOGISTIC REGRESSION RESULTS
# =========================

print("\n================ LOGISTIC REGRESSION ================\n")

print("Accuracy:",
      accuracy_score(y_test, y_pred_log))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred_log))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred_log))

# ============================================================
# MODEL 2: NAIVE BAYES
# ============================================================

nb_model = GaussianNB()

nb_model.fit(X_train, y_train)

y_pred_nb = nb_model.predict(X_test)

# =========================
# NAIVE BAYES RESULTS
# =========================

print("\n================ NAIVE BAYES ================\n")

print("Accuracy:",
      accuracy_score(y_test, y_pred_nb))

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred_nb))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred_nb))

# ============================================================
# FINAL COMPARISON
# ============================================================

log_acc = accuracy_score(y_test, y_pred_log)
nb_acc = accuracy_score(y_test, y_pred_nb)

print("\n================ MODEL COMPARISON ================\n")

print("Logistic Regression Accuracy :", log_acc)
print("Naive Bayes Accuracy         :", nb_acc)

if log_acc > nb_acc:
    print("\nLogistic Regression performed better.")
elif nb_acc > log_acc:
    print("\nNaive Bayes performed better.")
else:
    print("\nBoth models performed equally.")