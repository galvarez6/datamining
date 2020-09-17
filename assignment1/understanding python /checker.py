import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
# Create a dataframe from csv
df = pd.read_csv('practice.txt', delimiter='\t')

myData = df.values

def minMaxVec(vec1,vec2):
    #for jaccard
    minimums=[]
    maximums=[]
    for i in range(0, len(vec1)):
        minimums.append(min( vec1[i] , vec2[i]))
    for i in range(0, len(vec1)):
        maximums.append(max( vec1[i] , vec2[i]))
    return minimums, maximums


def euclid(vec1, vec2):
    ### Write your code here and return an appropriate value
    euclidean_dist = np.sqrt(np.sum((vec1-vec2)**2))
    return euclidean_dist
    #return None

def manhattan_distance(vec1, vec2):
    ### Write your code here and return an appropriate value
    man_dist = np.sum(abs(vec1-vec2))
    return man_dist
    #return None

def cosine(vec1, vec2):
    ### Write your code here and return an appropriate value
    numerator = np.dot(vec1 , vec2)
    denominator = np.sqrt(sum(vec1**2))* np.sqrt(sum(vec2**2))
    cosinesim =  numerator/denominator
    return cosinesim
    #return None

def jaccard(vec1, vec2):
    ### Write your code here and return an appropriate value
    minimums, maximums = minMaxVec(vec1,vec2)
    jaccard = sum(minimums)/sum(maximums);
    return jaccard
    #return None

def tanimoto(vec1, vec2):
    ### Write your code here and return an appropriate value
    numerator = np.dot( vec1 , vec2)
    denominator = (sum(vec1**2)+sum(vec2**2))-numerator
    tanimoto = numerator/denominator
    return tanimoto
    #return None

def sortKey(item):
    return item[1]

def knearest(vec, data, k, method):
    # Write code to return the indices of k nearest
    # neighbors of vec in data using method
    result = []
    for row in range (0, len(data)):
        distance = euclid(vec, data[row])
        result.append([row, distance])
    sortedResult = sorted(result, key=sortKey)
    indicies = []
    if k<len(data):
        for r in range(0, k):
            indicies.append(sortedResult[r][0])
    else:
        indicies = [i[0] for i in sortedResult]
    return indicies
    #return None


print("Euclidean distance between row 0 and 1: ", euclid(myData[0], myData[1]))
print("Manhattan distance between row 0 and 1: ", manhattan_distance(myData[0], myData[1]))
print("Cosine similarity between row 0 and 1: ", cosine(myData[0], myData[1]))
print("Jaccard similarity between row 0 and 1: ", jaccard(myData[0], myData[1]))
print("Tanimoto similarity between row 0 and 1: ", tanimoto(myData[0], myData[1]))
print("***************************************")

print("knn of row 100 using euclidean distance: ", knearest(myData[100], myData, k=5, method = "euclidean"))
#print("knn of row 100 using manhattan distance: ", knearest(myData[100], myData, k=5, method = "manhattan"))
