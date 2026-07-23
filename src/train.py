import os
import joblib

from sklearn.ensemble import RandomForestClassifier

from src.data import load_data
from src.features import preprocess_data


def train():
    df = load_data()

    X_train, X_test, y_train, y_test = preprocess_data(df)

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/student_risk_model.pkl")

    print("Model saved successfully.")


if __name__ == "__main__":
    train()