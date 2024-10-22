# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 05:14:15 2024

@author: DThomas
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:32:01 2022

@author: dthomas
"""
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

def main():
    array = np.array([[  9.77075874,   3.27621022],
       [ -9.71349666,  11.27451802],
       [ -6.91330582,  -9.34755911],
       [-10.86185913, -10.75063497],
       [ -8.50038027,  -4.54370383]])
    
    # K means clustering
    kmeans = KMeans(n_clusters=2, max_iter=10)
    clusterAssignments = kmeans.fit_predict(array)
    print("Cluster assignments:", clusterAssignments)
    print("Centroids", kmeans.cluster_centers_)
    print("SSE:", kmeans.inertia_)
    
    # Plot points
    #plt.scatter(array[:,0], array[:,1])
    #plt.scatter(array[:,0], array[:,1], c=clusterAssignments)
    #plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], color="black", marker="x")
    
    X, y_true = make_blobs(n_samples=2000, centers=17,
                       cluster_std=0.60, random_state=3)
    
    kmeans = KMeans(n_clusters=7, max_iter=5)
    prediction = kmeans.fit_predict(X)
    print(prediction)
    print(kmeans.cluster_centers_)
    print("SSE:", kmeans.inertia_)
    plt.scatter(X[:,0], X[:,1],c=prediction)
    plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], color="black", marker="x")
    plt.savefig("KMeansImage.png")
    
main()