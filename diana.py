import numpy as np
from sklearn.metrics import pairwise_distances
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs 

def diana(X):
    clusters = [list(range(len(X)))] 
    distances = pairwise_distances(X)
    cluster_labels = np.zeros(len(X))

    while len(clusters) < len(X): 
        
        largest_cluster = max(clusters, key=len)

        if len(largest_cluster) > 1: 
            sub_distances = distances[largest_cluster][:, largest_cluster]
            farthest_point = largest_cluster[np.argmax(sub_distances.sum(axis=1))]

            new_cluster = [i for i in largest_cluster if distances[i, farthest_point] > np.median(sub_distances)]
            if new_cluster: 
                clusters.append(new_cluster)
            clusters.remove(largest_cluster)

            for point in new_cluster:
                cluster_labels[point] = len(clusters) - 1
        else: 
            break 
    return cluster_labels

X, _ = make_blobs(n_samples=100, centers=3, cluster_std=0.60, random_state=42)

labels = diana(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50)
plt.title("DIANA - Divisive Clustering")
plt.show()
