# src/features.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


def preprocess_data(df):

    df = df.copy()

    # ==============================
    # Create Target Variable
    # ==============================

    # Student risk:
    # G3 < 10 => Risk (1)
    # G3 >= 10 => No Risk (0)

    df["risk"] = (df["G3"] < 10).astype(int)


    # ==============================
    # Encode Categorical Features
    # ==============================

    categorical_cols = [
        "school",
        "sex",
        "address",
        "schoolsup",
        "famsup",
        "higher"
    ]


    for col in categorical_cols:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])


    # ==============================
    # Feature Selection
    # ==============================

    features = [

        "school",
        "sex",
        "age",
        "address",

        "Medu",
        "Fedu",

        "studytime",
        "failures",

        "schoolsup",
        "famsup",
        "higher",

        "absences",

        "G1",
        "G2"
    ]


    X = df[features]
    y = df["risk"]


    # ==============================
    # Train Test Split
    # ==============================

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )


    return X_train, X_test, y_train, y_test