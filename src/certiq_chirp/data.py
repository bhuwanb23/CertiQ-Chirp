"""Loading and validating the supplied campaign workbook."""

import pandas as pd

from .config import WORKBOOK


def load_data():
    train = pd.read_excel(WORKBOOK, sheet_name="Stage1_Train")
    test = pd.read_excel(WORKBOOK, sheet_name="Stage1_Test")
    s2 = pd.read_excel(WORKBOOK, sheet_name="Stage2_Data")
    y = (train["y"] == "yes").astype(int).to_numpy()
    X = train.drop(columns=["customer_id", "y"])
    Xt = test.drop(columns=["customer_id"])
    return train, test, s2, X, y, Xt
