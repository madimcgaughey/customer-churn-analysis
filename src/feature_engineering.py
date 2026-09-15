import pandas as pd


def add_risk_tier(df, probability_col="ChurnProbability"):
    df = df.copy()

    df["RiskTier"] = pd.cut(
        df[probability_col],
        bins=[0, 0.30, 0.60, 1.00],
        labels=["Low", "Medium", "High"],
        include_lowest=True
    )

    return df