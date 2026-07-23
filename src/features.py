from sklearn.model_selection import train_test_split
import os


def preprocess_data(df):

    df = df.copy()

    # Create target column
    df["risk"] = (df["G3"] < 10).astype(int)


    features = [
        "age",
        "studytime",
        "failures",
        "absences"
    ]


    # Processed data create
    processed_df = df[features + ["risk"]]


    # Create folder
    os.makedirs(
        "data/processed",
        exist_ok=True
    )


    # Save processed CSV
    processed_df.to_csv(
        "data/processed/model_ready_data.csv",
        index=False
    )


    print("Processed data saved ✅")


    # ML data split
    X = processed_df[features]
    y = processed_df["risk"]


    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

if __name__ == "__main__":

    import pandas as pd

    data = pd.read_csv(
        "data/interim/cleaned_student_data.csv"
    )

    preprocess_data(data)