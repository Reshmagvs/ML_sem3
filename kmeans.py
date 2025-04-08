import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, y = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=42)

plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Dataset before Clustering")
plt.show()

kmeans = KMeans(n_clusters=3, random_state=42)

kmeans.fit(X)

y_kmeans = kmeans.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75, marker='x', label='Centroids')
plt.title("K-Means Clustering Results")
plt.legend()
plt.show()
