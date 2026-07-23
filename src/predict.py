import joblib
import pandas as pd

MODEL_PATH = "models/student_risk_model.pkl"

model = joblib.load(MODEL_PATH)

def predict(data):
    df = pd.DataFrame([data])
    prediction = model.predict(df)
    return prediction[0]

if __name__ == "__main__":

    sample = {
        "age": 18,
        "studytime": 2,
        "failures": 0,
        "absences": 4
    }

    print("Prediction:", predict(sample))