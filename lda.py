import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

data = load_iris()
X = data.data  
y = data.target  

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

lda = LDA(n_components=2)  
X_lda = lda.fit_transform(X_scaled, y)

plt.figure(figsize=(8, 6))
plt.scatter(X_lda[:, 0], X_lda[:, 1], c=y, cmap='viridis', s=50, alpha=0.7)
plt.title('LDA Dimensionality Reduction (Iris Dataset)')
plt.xlabel('LD 1')
plt.ylabel('LD 2')
plt.colorbar(label='Classes')
plt.show()

explained_variance = lda.explained_variance_ratio_
print("Explained variance ratio:", explained_variance)

