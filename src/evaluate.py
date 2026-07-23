import joblib

from sklearn.metrics import accuracy_score, classification_report

from src.data import load_data
from src.features import preprocess_data


def evaluate():

    # Load dataset
    df = load_data()

    # Split data
    X_train, X_test, y_train, y_test = preprocess_data(df)

    # Load trained model
    model = joblib.load("models/student_risk_model.pkl")

    # Predict
    predictions = model.predict(X_test)

    # Evaluate
    print("Accuracy:", accuracy_score(y_test, predictions))
    print(classification_report(y_test, predictions, zero_division=0))


if __name__ == "__main__":
    evaluate()