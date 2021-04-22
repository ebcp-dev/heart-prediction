import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import sys

sc = StandardScaler()
data = pd.read_csv('./model/heart-disease.csv')
model = joblib.load('./model/randomforestmodel.joblib')


def show_head():
    return data.head()


def predict_test():
    return model.predict(sc.transform(
        [[20, 1, 2, 110, 230, 1, 1, 140, 1, 2.2, 2, 0, 2]]))
