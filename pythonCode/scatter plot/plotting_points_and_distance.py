#!/usr/bin/env python
# coding: utf-8

# In[58]:

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
# 5 Data points with 2 features
data = np.array([[1,1],[2,2],[3,3],[4,4]])
print("data:",data)


# In[59]:


# Plotting the data
fig = plt.figure()
plt.scatter(data[:,:1], data[:,1:2])
fig.suptitle('Scatter Plot', fontsize=20)
plt.xlabel('feature1', fontsize=16)
plt.ylabel('feature2', fontsize=16)
fig.savefig('ScatterPlot.jpg')


# In[60]:


# 5 Data points with each has 5 features
data2 = np.array([[10,3,3,5,10],
                  [5,4,5,3,6],
                  [10,4,6,4,9],
                  [8,6,2,6,3],
                  [9,2,1,2,11]])
print("data2:",data2)


# In[61]:


# Manhattan distance between row 1 and row 4. Remember in numpy array, index start with 0. So row 1 means second row.
man_dist = np.sum(abs(data2[1]-data2[4]))
print("manhattan distance using math:", man_dist)


# In[62]:


# Euclidean distance between row 1 and row 4. Remember in numpy array, index start with 0. So row 1 means second row.
euclidean_dist = np.sqrt(np.sum((data2[1]-data2[4])**2))
print("euclidean distance using math:", euclidean_dist)


# In[63]:


# Manhattan distance using scipy library
from scipy.spatial import distance
man_dist2 = distance.cityblock(data2[1],data2[4])
print("manhattan distance using scipy:", man_dist2)


# In[64]:


# Euclidean distance using scipy library
from scipy.spatial import distance
euclidean_dist2 = distance.euclidean(data2[1],data2[4])
print("euclidean distance using scipy:",euclidean_dist2)


# In[ ]:
