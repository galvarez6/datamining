from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score
import pandas as pd
#import numpy as np

# Create a dataframe from csv
df = pd.read_csv('iris-data.txt', delimiter='\t', header=None)
f = pd.read_csv('iris-labels.txt', delimiter='\n', header=None)

myData = df.values
benchmark = f.values
flatBench = []
for i in benchmark:
    for j in i:
        flatBench.append(j)

km = KMeans(n_clusters=3, random_state=20).fit(myData)

print(benchmark)
print(flatBench)

print("kMeans assignments are:")

print(km.labels_)

count = 0
counter2 = 0
results = []
for i in km.labels_:
    counter2 +=1
    results.append(i)

for i in results:
    count = count+1

print(counter2)
print("this: ")
print(results)
print(count)

bothLists = []
bothLists.append(results)
bothLists.append(flatBench)

print(bothLists)

tp = 0
fp = 0
tn = 0
fn = 0
array_length = len(bothLists)
print("HERE")
print(adjusted_rand_score(results,flatBench))
print(adjusted_rand_score(flatBench,results))

print(results[0], flatBench[0])
print(bothLists[0][0])
print(bothLists[1][0])








#print("Centroids: ")
#print(km.cluster_centers_)

#print("Sum of squared distances (SSD) of samples to their closest cluster center:")
#print(km.inertia_);
