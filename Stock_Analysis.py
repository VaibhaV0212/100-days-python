import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

data = pd.read_csv('stock_analysis.csv' , parse_dates=True , index_col='Date')
df = data.copy()
# print(df.head())
print(df.describe())
print(df.info())
print(df.shape)
print(df.columns)
# print(df.index)