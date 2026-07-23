import pandas as pd
from pathlib import Path

def load_data():
    base_dir = Path(__file__).resolve().parent.parent
    csv_path = base_dir / "data" / "raw" / "student-mat.csv"

    df = pd.read_csv(csv_path)
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())