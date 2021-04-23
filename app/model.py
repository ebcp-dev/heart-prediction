import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

sc = StandardScaler()
data = pd.read_csv('app/model/heart-disease.csv')
model = joblib.load('app/model/randomforestmodel.joblib')
# Assign 13 features to X, and column 'target' to predictor y
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
# Split: the dataset into the Training set and Test set
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)
# Standardize the data so its distribution will have a mean of 0 and a standard deviation of 1.
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
# Train/Fit model
model.fit(x_train, y_train)


def predict(user_input):
    prediction = model.predict(sc.transform([user_input]))
    return prediction
