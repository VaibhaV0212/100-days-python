import pandas as pd
import numpy as np

''' Create a Series '''
s1 = pd.Series([5,3,2,1])
# print(s1)
# print(s1.values)
# print(s1.index)
# print(s1.index.values)

''' Create Series from numpy with custom index'''
arr1 = np.array([1,2,3,4])
s2 = pd.Series(arr1, index = ['ola','uber','sride','drive'])
# print(s2)

''' Filtering on certain condition '''
# print(s2>2)
# print(s2[s2>2])

''' Checking whether a element is in the Series or not '''
# print('b' in s2)

''' to_dict() '''
new_dict = s2.to_dict()
# print(new_dict)

''' Assinging name to a Series and its index '''
s2.name = 'Company - Revenue'
s2.index.name = 'Company name'
# print(s2)


''' CREATING A DATAFRAME '''   
''' go on google search 'table of data' :

First name	Last name	Age
Tinu	Elejogun	14
Javier	Zapata	28
Lily	McGarrett	18
Olatunkbo	Chijiaku	22
Adrienne	Anthoula	22
Axelia	Athanasios	22
Jon-Kabat	Zinn	22
Thabang	Mosoa	15
Kgaogelo	Mosoa	11
'''
# df = pd.read_clipboard()  
data = [
    {'First name':'Tinu', 'Last name':'Elejogun', 'Age': 22},
    {'First name':'Javier', 'Last name':'Zapata', 'Age': 23},
    {'First name':'Lily', 'Last name':'McGarrett', 'Age': 24},
    {'First name':'Olatunkbo', 'Last name':'Chijiaku', 'Age': 25},
    {'First name':'Adrienne', 'Last name':'Anthoula', 'Age': 26},
    ]
df = pd.DataFrame(data)
# print(df)

'''Display column names'''
# print(df.columns)

'''Access 1 or more columns '''
# print(df[['First name','Age']])

''' NAN values'''
df['rank'] = np.nan
df['new_rank'] = np.nan
# print(df.head(3))

''' Assign values to dataframe using 1. Numpy 2. Series'''
array_1 = np.arange(1,6)
# print(array_1)
array_2 = pd.Series([2,3,4,5,6,7])

df['rank'] = array_1
df['new_rank'] = array_2
# print(df.head())

''' Delete a column'''
# df.drop(['new_rank'], axis=1, inplace=True)

'''Renaming a column'''
df = df.rename(index= {'new_rank':'new rank'})
# print(df)

x = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
x = x.reindex(['a','b','c','d','e','f','g'])
x = x.reindex(['a','b','c','d','e','f','g','h'], fill_value=100)  #fill_value only fill the value for the recently added index
# print(x)

''' Reindexing in Dataframe'''
df1 = pd.DataFrame(np.random.randn(25).reshape(5,5) , index=['a','b','c','d','e'] , columns=['c1','c2','c3','c4','c5'])
df1 = df1.reindex(index=['a','b','c','d','e','f'] , columns=['c1','c2','c3','c4','c5','c6'])
# print(df1.isnull())
# df1 = df1.dropna(how='all')
# df1 = df1.dropna(thresh=2)  # 2 values should be present and should not be nan
# df1 = df1.fillna(0)
df1 = df1.fillna({'f':50, 'c6':40})
print(df1)