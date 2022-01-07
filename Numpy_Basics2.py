import numpy as np

x = np.array([100,115,150,170])
y = np.array([10,15,20,25])
condition = np.array([True,True,False,False])


''' using where condition'''
result = np.where(condition,x,y)
# print(result)

''' using std condition - sum, sum(0), mean(), std(), var() '''
x1 = x.sum()
# print(x1)
x3 = np.array([[1,2],[3,4]])
# print(x3.sum(0))
# print(x3.mean())
# print(x3.std())
# print(x3.var())


''' Logical AND, OR '''
condition = np.array([True,True,False,False])
# OR
new_cond = condition.any()
# print(new_cond)
# AND
new_cond_and = condition.all()
# print(new_cond_and)

''' sort() function '''
unsorted = np.array([1,2,5,3,8,0,9,4,4,1,2,0])
unsorted.sort()
# print(unsorted)

''' unique() function '''
# print(np.unique(unsorted))

''' inld() function - checks whether the value is present in one array or not '''
# print(np.inld([1,23,4], unsorted))