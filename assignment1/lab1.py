# You have two input files. One is, practice.txt
# and the other is data.txt. Some expected answers
# for practice.txt are provided here in this
# file. You will have to answer the questions
# on Blackboard using data.txt.

# Complete coding for this file using the data
# in practice.txt. Check if the results match
# with the results provided in the comments.

# Answer the questions on Blackboard using
# the data.txt file as the input data. Submit
# the completed code file on Blackboard.

import pandas as pd
import numpy as np
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

def jaccard(vec1, vec2):
    ### Write your code here and return an appropriate value
    minimums, maximums = minMaxVec(vec1,vec2)
    jaccard = sum(minimums)/sum(maximums);
    return jaccard
    #return None

def cosine(vec1, vec2):
    ### Write your code here and return an appropriate value
    numerator = np.dot(vec1 , vec2)
    denominator = np.sqrt(sum(vec1**2))* np.sqrt(sum(vec2**2))
    cosinesim =  numerator/denominator
    return cosinesim
    #return None

def tanimoto(vec1, vec2):
    ### Write your code here and return an appropriate value
    numerator = np.dot( vec1 , vec2)
    denominator = (sum(vec1**2)+sum(vec2**2))-numerator
    tanimoto = numerator/denominator
    return tanimoto
    #return None

def sortkey(item):
    return item[1]

def knearest(vec, data, k, method):
    # Write code to return the indices of k nearest
    # neighbors of vec in data using method
    result = []
    if method == "euclidean":
        for row in range (0, len(data)):
            distance = euclid(vec, data[row])
            result.append([row, distance])
    elif method == "manhattan":
        for row in range (0, len(data)):
            distance = manhattan_distance(vec, data[row])
            result.append([row, distance])
    sortedResult = sorted(result, key=sortkey)
    indicies = []
    if k<len(data):
        for r in range(0, k):
            indicies.append(sortedResult[r][0])
    else:
        indicies = [i[0] for i in sortedResult]
    return indicies
    #return None


print("***************************************")

# Distance and similarity between row 0 and 1:
print("Euclidean distance between row 0 and 1: ", euclid(myData[0], myData[1]))
print("Manhattan distance between row 0 and 1: ", manhattan_distance(myData[0], myData[1]))
print("Cosine similarity between row 0 and 1: ", cosine(myData[0], myData[1]))
print("Jaccard similarity between row 0 and 1: ", jaccard(myData[0], myData[1]))
print("Tanimoto similarity between row 0 and 1: ", tanimoto(myData[0], myData[1]))


# Expected output for row 0 and row 1 using practice.txt:
# Euclidean distance between row 0 and 1: 0.30000000000000016
# Manhattan distance between row 0 and 1: 0.5000000000000002
# Cosine similarity between row 0 and 1: 0.9987914527303724
# Jaccard similarity between row 0 and 1: 0.9484536082474225
# Tanimoto similarity between row 0 and 1: 0.9973973395026026

print("***************************************")

# Distance and similarity between row 5 and 100:
print("Euclidean distance between row 5 and 100: ", euclid(myData[5], myData[100]))
print("Manhattan distance between row 5 and 100: ", manhattan_distance(myData[5], myData[100]))
print("Cosine similarity between row 5 and 100: ", cosine(myData[5], myData[100]))
print("Jaccard similarity between row 5 and 100: ", jaccard(myData[5], myData[100]))
print("Tanimoto similarity between row 5 and 100: ", tanimoto(myData[5], myData[100]))

# Expected output for row 5 and row 100 using practice.txt:
# Euclidean distance between row 5 and 100:  4.263801121065568
# Manhattan distance between row 5 and 100:  7.199999999999999
# Cosine similarity between row 5 and 100:  0.8797042812407445
# Jaccard similarity between row 5 and 100:  0.5555555555555556
# Tanimoto similarity between row 5 and 100:  0.705587044534413

print("***************************************")

# K nearest neighbors of row 0 (The expected output is given for row 0 for validating your code)
print("knn of row 0 using euclidean distance: ", knearest(myData[0], myData, k=5, method = "euclidean"))
print("knn of row 0 using manhattan distance: ", knearest(myData[0], myData, k=5, method = "manhattan"))

# Expected output for row 0 of practice.txt:
# knn of row 0 using euclidean distance:  [0, 44, 11, 8, 33]
# knn of row 0 using manhattan distance:  [0, 44, 11, 24, 8]

print("***************************************")

# K nearest neighbors of row 100 (The expected output is given for row 0 for validating your code)
print("knn of row 100 using euclidean distance: ", knearest(myData[100], myData, k=5, method = "euclidean"))
print("knn of row 100 using manhattan distance: ", knearest(myData[100], myData, k=5, method = "manhattan"))

# Expected output for row 100 of practice.txt:
# knn of row 100 using euclidean distance:  [100, 141, 112, 120, 148]
# knn of row 100 using manhattan distance:  [100, 141, 112, 82, 148]

print("***************************************")
print("Distance and similarity between row 30 and 120")
print("Euclidean distance: ", euclid(myData[30], myData[120]))
print("Manhattan distance: ", manhattan_distance(myData[30], myData[120]))
print("Cosine similarity: ", cosine(myData[30], myData[120]))
print("Jaccard similarity: ", jaccard(myData[30], myData[120]))
print("Tanimoto similarity: ", tanimoto(myData[30], myData[120]))

print("***************************************")

print("Jaccard similarity between Row 55 and Row 137: ", jaccard(myData[55], myData[137]))

print("***************************************")
print("knn of row 148 using euclidean distance: ", knearest(myData[148], myData, k=5, method = "euclidean"))

print("***************************************")
print("Tanimoto similarity between row 9 and 148: ", tanimoto(myData[9], myData[148]))
