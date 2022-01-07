# importing required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression

# importing the dataset
data = pd.read_csv(r'excel\AdvertisingBudgetandSales.csv', index_col=0)

# viewing the 6 sample records from the dataset
# print(data.sample(6))

# view the dataset size
# print(data.size)

# view the shape of dataset
# print(data.shape)

# view the columns
# print(data.columns)

# print(data.info())
# print(data.isnull().any())


# Creating object for independent variables
X_features = data[['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)']]
# print(X_features.head())

Y_target = data['Sales ($)']
# print(Y_target.head())

# print(X_features.shape)
# print(Y_target.shape)

X_train, X_test, y_train, y_test = train_test_split(X_features, Y_target, test_size=0.2)

reg = LinearRegression()
reg.fit(X_train,y_train)
pred = reg.predict(X_test)
print('Score = ', round(reg.score(X_test,y_test)*100,2))