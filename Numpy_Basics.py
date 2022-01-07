import numpy as np
import array as arr

''' Creating 1D array '''
n1 = np.array([1,2,3,4])
# print(n1)

''' Creating 2D array '''
n2 = np.array([[1,2,3,4],[5,6,7,8]])
# print(n2)

''' Dimensions of array'''
# print(n2.shape)

''' Datatype of array'''
# print(n2.dtype)

''' Creating the zeros array'''
zeros = np.zeros([3,4])
# print(zeros)

''' Creating the ones array'''
ones = np.ones(2)
# print(ones)

zeros_like = np.zeros_like(zeros)
# print(zeros_like)

''' Creating the empty array'''
empty = np.empty([3,4])
# print(empty)

''' Creating the eye function'''
# eye = np.eye(4)
identity = np.identity(5)
# print(identity)

''' Creating arrays using arange() '''
AP = np.arange(0,10,2)
# print(AP)

''' Scalar multiplication using * '''
n3 = n2 * n2
# print(n3)

''' Indexes '''
n4 = n3[1][1]
# print(n4)

''' Slicing '''
n5 = n3[0:,0:2]
# print(n5)

''' Updating '''
n3[1][0:2] = [123,125]
# print(n3)

''' Copying '''
n6 = n3
n7 = n6.copy()

''' Square root '''
n8 = np.sqrt(n7)
# print(n8)


''' Maximum '''
n9 = np.max(n7)
# print(n9)

''' Expo '''
n10 = np.exp(n7)
# print(n10)

''' Random '''
n11 = np.random.randn(5)
# print(n11)
n12 = np.random.randn(5,5)
# print(n12)

''' Saving single array '''
np.save('Saved_array',n1)

''' Loading single array '''
new_single = np.load('Saved_array.npy')
# print('new_single : ', new_single)


''' Saving and loading multiple array '''
n13 = np.arange(25)
n14 = np.arange(5)
np.savez('saved_archive.npz',x=n13, y=n14)
new_multiple = np.load('saved_archive.npz')
# print('new_multiple : ',new_multiple['x'])
# print('new_multiple : ',new_multiple['y'])


''' Saving array to txt file '''
np.savetxt('myarray', n13, delimiter=',')

''' Load a txt '''
load_file = np.loadtxt('myarray', delimiter=',')
print('load_file : ', load_file)