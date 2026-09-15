import pandas as pd


def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df["TotalCharges"] = df["TotalCharges"].fillna(0)

    return df