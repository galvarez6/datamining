import numpy as np
#from sklearn.neighbors import NearestNeighbors

#using this proximity measure
#vectors as parameters to compute euclidean distnce
def euclid(vec1, vec2):
    euclidean_dist = np.sqrt(sum((vec1-vec2)**2))
    return euclidean_dist

#fucntion to sort what you want to sort by
#second column
#def sortKey(item):
    #return item[1]

def knearest(vec, data, k):
    #to store distance of each row for sorting
    #empty array
    result = []
    #compute distance between given vec and each other row in the data table
    for row in range (0, len(data)):
        distance = euclid(vec, data[row])
        #store the distance to sort later
        #store the row and the distance number
        result.append([row, distance])
    #test
    #for i in range(len(data)):
       #print(data[i])
    #sort the results based on distance (2 column)
    #sorted is a function within python pass the array and what you want to sort
    #which is the second column
    #sortedResult = sorted(result, key=sortKey)

    #print('\033[1m' + "Sorted results" + '\033[0m')
    #for i in range(len(sortedResult)):
        #print(sortedResult[i])

    indicies = []

    if k<len(data):
        for r in range(0, k):
            indicies.append(sortedResult[r][0])
    else:
        indicies = [i[0] for i in sortedResult]

    return indicies


data = np.array([[10,3,3,5,10],
                [5,4,5,3,6],
                [10,4,6,4,9],
                [8,6,2,6,3],
                [10,3,3,5,8],
                [9,2,1,2,11],
                [9,3,1,2,11]])




#find k nearest neighbors of reference vector
givenVec = data[1];
for i in range(len(data)):
    print(data[i])
knn = knearest(givenVec, data, 7)
#print('\033[1m' + "3 nearest neighbors of row 0" + '\033[0m')
print("knn: ", knn)

##### another way #####
#print()
#nbrs = NearestNeighbors(n_neighbors=7, algorithm='ball_tree').fit(data)
#distances, indices = nbrs.kneighbors(data)

#print(distances)
#print(indices)
