import numpy as np
a = np.array([1,2,3])
print(a*3)
b = np.array([[1,2,3],[4,5,6]])
print(b.shape)#ouput:(2, 3)
print(b.ndim)#output:2
print(b.dtype)#output:int64
c = np.zeros((2,2))
print(c)#output:
# [[0. 0.]
#  [0. 0.]]
d = np.ones((2,2))
print(d)
#output:
# [[1. 1.]
#  [1. 1.]]
a1 = np.array([10,20,30,40])
print(a1[1:3])#output:[20 30]
b1 = np.array([[1,2,3,30],[4,5,6,45],[7,8,9,10]])
# print(b1.shape)
# print(b1.reshape(2,6))
#output:
# [[ 1  2  3 30  4  5]
#  [ 6 45  7  8  9 10]]
print(b1.reshape(4,3))#output:
# [[ 1  2  3]
#  [30  4  5]
#  [ 6 45  7]
#  [ 8  9 10]]
# a3 = np.array([1,2,3])
# print(a3 + 5)#output:[6 7 8]
# a4 = np.array([[1,2],[3,4]]) 
# print(a4.sum())#output:10
a4 = np.array([[1,2,6],[3,4,12]])
print(a4.mean())# output average 4.666666666666667
print((1+2+6+3+4+12)/6)
#sum() → total of elements
#mean() → average of elements
a5 = np.arange(1,10,2)#(start=1, range=10, step=2)
print(a5)#[1 3 5 7 9]




