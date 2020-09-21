from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pandas as pd

df = pd.read_csv('theData.txt', delimiter='\t', header=None)
dl = pd.read_csv('theDataKnownAssignments.txt', delimiter='\t', header=None)

#you need to know what is the k means and what is the known assignment
#thats why it is 2 parameters
def RandIndex(assignments, known):
    #true pos
    tp = 0
    #true neg
    tn = 0
    #false pos
    fp = 0
    #false negative
    fn = 0
    #go over every pair in both arrays
    #both assignment and known should have the same length
    for i in (0, len(known)):
        for j in (i+1, len(known)):
            if assignments[i] == assignments[j]:
                #we have found a positive pair
                if known[i]==known[j]:
                    #we have found true positive pair
                    tp=tp+1
                else:
                    #false positive
                    fp=fp+1
            #i is not equal to j when checking assignments array
            else:
                #from 2 different cluster they are a negative pair
                if known[i]==known[j]:
                    #it should be a false negative
                    fn=fn+1
                else:
                    #true negative
                    tn=tn+1
    rand = (tp+tn)/(tp+tn+fp+fn)
    return rand



myData = df.values
#2d array
labels = dl.values
#but we want a 1d array
labels = labels[:,0]

km = KMeans(n_cluster=2, random_state=0).fit(myData)

print("kMeans assignment are:")
print(km.labels_)

print("centroids: ")
print(km.cluster_centers_)

print("\n")
r = RandIndex(km.labels_, labels)
print("RandIndex is: ", r)
