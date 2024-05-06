import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error
import numpy as np
import os
import random


file_path = os.environ.get('data_path')

def prmse(y_true, y_pred):
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    range_y = np.max(y_true) - np.min(y_true)
    prmse_value = (rmse / range_y) * 100
    return prmse_value


if __name__ == "__main__":
    # col_name = sys.argv[1]
    col_name = os.environ.get("col_name")

    df = pd.read_csv(file_path)

    features = df.drop(columns=[col_name])
    target_variable = df[col_name]

    r_state = 42 + random.randint(1,100)

    X_train, X_test, y_train, y_test = train_test_split(
        features, target_variable, train_size=0.8, random_state=r_state)

    model = LinearRegression()

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    rmse = root_mean_squared_error(y_test, y_pred)
    print(rmse)