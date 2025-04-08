import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=42)

agnes = AgglomerativeClustering(n_clusters=3)

agnes.fit(X)
labels = agnes.labels_

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50)
plt.title("AGNES - Agglomerative Clustering")
plt.show()

linked = linkage(X, method='ward')
plt.figure(figsize=(10, 7))
dendrogram(linked)
plt.title("Dendrogram for AGNES")
plt.show()
