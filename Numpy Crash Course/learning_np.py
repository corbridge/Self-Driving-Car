## Just introducing with numpy

import numpy as np

# array_two = np.arange(1,4) ** 2
# # print(array_two)

# print(np.power(np.array([1,2,3]),4))

x = np.arange(3)
y = np.arange(3,6)
z = np.arange(6,9)

multi_array = np.array([x,y,z])
# print(multi_array)

x = np.arange(18).reshape(2,3,3)
# print(x)

a = np.arange(9).reshape(3,3)
# print(a)

revel_array = a.ravel()
# print(revel_array)

flat_array = a.flatten()
flat_array[2] = 1000
# print(flat_array)

b = np.arange(9)
b.shape = [3,3]
print(b.transpose)