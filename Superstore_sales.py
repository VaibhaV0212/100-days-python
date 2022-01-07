import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
Q1. What is the overall sales trend?
Q2. Which are the Top 10 products by sales?
Q3. Which are the Most Selling Products?
Q4. Which is the most preferred Ship Mode?
Q5. Which are the Most Profitable Category and Sub-Category?
'''

data = pd.read_excel('superstore_sales.xlsx')
# print(data.head())
# print(data.columns)
'''
['order_id', 'order_date', 'ship_date', 'ship_mode', 'customer_name',
       'segment', 'state', 'country', 'market', 'region', 'product_id',
       'category', 'sub_category', 'product_name', 'sales', 'quantity',
       'discount', 'profit', 'shipping_cost', 'order_priority', 'year']
'''
# print('describe\n = ', data.describe())
# print('info\n=', data.info())
# print(data.isnull().sum())

# '''''''''''''''Q1. What is the overall sales trend? '''''''''''''''''''''''''''

#print(data['order_date'].min())  #2011-01-01 00:00:00
#print(data['order_date'].max())  #2014-12-31 00:00:00

# Fetching the year and month from the date
data['month_year'] = data['order_date'].apply(lambda x : x.strftime('%Y-%m'))
# print(data['month_year'])
# print(data.groupby('month_year').sum())

# Grouping month year
df_trend = data.groupby('month_year').sum()['sales']

# Plotting a line graph
plt.figure(figsize=(15,6))
plt.plot(df_trend)
plt.xticks(rotation='vertical', size=8)
# plt.show()

# '''''''''''''''Q2. Which are the Top 10 products by sales? '''''''''''''''''''''''''''
# print(data.head())

df_product_sales = pd.DataFrame(data.groupby('product_name').sum()['sales'])
# print(df_product_sales.sort_values('sales', ascending=False))


# '''''''''''''''Q3. Which are the Most Selling Products? '''''''''''''''''''''''''''

most_selling = pd.DataFrame(data.groupby('product_name').sum()['quantity'])
# print(most_selling.sort_values('quantity', ascending=False)[0:10])


# '''''''''''''''Q4. Which is the most preferred Ship Mode? '''''''''''''''''''''''''''
# plt.figure(figsize=(10,9))
# sns.countplot(ddat['ship_mode'])
# plt.show()


# '''''''''''''''Q5. Which are the Most Profitable Category and Sub-Category?'''''''''''''''''''''''''''
cat_subcat = pd.DataFrame(data.groupby(['category', 'sub_category']).sum()['profit'])
# print(cat_subcat.sort_values(['category','profit'], ascending=False))