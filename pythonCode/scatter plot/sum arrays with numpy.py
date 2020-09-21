import numpy as np
data1 = np.array([1,2,3,4])
data2 = np.array([2,3,4,5])
data3 = np.array([[1,2,3,4],
                 [1,2,3,4]])
data4 = np.array([3,2,1,2])
#add both arrays(aka rows aka vectors)
print(data1+data2)
#sqare each feature with the power of two
print(data1**2)
#power of two and sum all features in the vector
print(np.sum(data1**2))
#multiply the vetors together
print(np.matmul(data1,data2))


print(np.matmul(data3,data4))