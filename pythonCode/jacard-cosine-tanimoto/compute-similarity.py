import numpy as np

data = np.array([[3,9,20,10,3,3,5],
                  [1,11,18,11,4,5,3],
                  [5,8,14,9,4,6,4],
                  [6,7,3,8,6,2,6],
                  [6,4,12,31,15,10,20]])

VecIndex1=0;
VecIndex2=2;

# Compute Weighted Jaccard
print(data[VecIndex1])

print(data[VecIndex2])

minimums=[]

for i in range(0, len(data[VecIndex1])):
    minimums.append(min( data[VecIndex1][i] , data[VecIndex2][i]))

print("Minimumns: ", minimums)

maximums=[]

for i in range(0, len(data[VecIndex1])):
    maximums.append(max( data[VecIndex1][i] , data[VecIndex2][i]))

print("Maximums: ", maximums)

jaccard = sum(minimums)/sum(maximums);

print("Jaccard: ", jaccard)

# Compute cosine similarity

numerator = np.dot( data[VecIndex1] , data[VecIndex2])

denominator = np.sqrt(sum(data[VecIndex1]**2))* np.sqrt(sum(data[VecIndex2]**2))

cosinesim =  numerator/denominator;
print("Cosine: ", cosinesim)

# Compute Tanimoto similaroty

numerator = np.dot( data[VecIndex1] , data[VecIndex2])

denominator = (sum(data[VecIndex1]**2)+sum(data[VecIndex2]**2))-numerator

tanimoto = numerator/denominator;

print("Tanimoto: ", tanimoto)

