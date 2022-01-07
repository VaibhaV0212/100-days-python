import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

data = pd.read_csv('googleplaystore.csv')
df = data.copy()
# print(df.head())

df.boxplot()
# plt.show()

# print(df.info())

''' Count the no. of missing values '''
total_null = pd.isnull(df)
# print(total_null.sum())
total_nan = df.isna()
# print('total_nan = ', total_nan.sum())
# print(total_nan.any())


''' Check how many ratings are more than 5 - Outliers'''
print(df[df.Rating > 5])
# print(df.loc[10472])

# DROP THAT OUTLIER
# df.drop([10472], inplace=True)
# print(df[10470:10475])

''' Data Manipulation'''
# print(df.Rating.isnull().sum())

# FILLING THE NUMERICAL DATA WITH meadian() VALUES
median_rating = (df.Rating.median())
print(median_rating)
df.Rating = df.Rating.fillna(median_rating)

# FILLING THE CATEGORICAL DATA WITH mode() VALUES
type_mode = (df['Type'].mode()[0])
current_ver_mode = (df['Current Ver'].mode()[0])
android_ver_mode = (df['Android Ver'].mode()[0])
# print(type_mode, current_ver_mode, android_ver_mode)

df['Type'].fillna(type_mode, inplace=True)
df['Current Ver'].fillna(current_ver_mode, inplace=True)
df['Android Ver'].fillna(android_ver_mode, inplace=True)
# print(df.isnull().sum())

''' Converting Rating, Review and Price cols in NUMERICAL Data from CATEGORICAL data'''
# print(df.Price[2252:2271])
df.drop([10472], inplace=True)
# x = str(df.Price)
# new = [x.replace('$','') if '$' in str(x) else str(x)]
# df.Price.apply((new))
# print(df.Price[2252])
df.Price = df.Price.apply(lambda x: str(x).replace('$','') if '$' in str(x) else str(x))
df['Price'] = df['Price'].apply(lambda x : float(x))

df['Installs'] = df['Installs'].apply(lambda x: str(x).replace('+','') if '+' in str(x) else (str(x)))
df['Installs'] = df['Installs'].apply(lambda x: str(x).replace(',','') if ',' in str(x) else (str(x)))
df['Installs'] = df['Installs'].apply(lambda x : float(x))

df['Reviews'] = pd.to_numeric(df.Reviews)
# print(df.head(10))
# print(df.describe())
