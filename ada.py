import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = load_iris()
X = data.data  
y = data.target 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

base_estimator = DecisionTreeClassifier(max_depth=1) 

ada_boost = AdaBoostClassifier(estimator=base_estimator, n_estimators=50, learning_rate=1.0, random_state=42)

ada_boost.fit(X_train, y_train)

y_pred = ada_boost.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy of AdaBoost: {accuracy * 100:.2f}%')

feature_importances = ada_boost.feature_importances_
plt.figure(figsize=(8, 6))
plt.bar(range(X.shape[1]), feature_importances, color='b', align='center')
plt.xticks(range(X.shape[1]), data.feature_names, rotation=45)
plt.title('Feature Importances in AdaBoost')
plt.xlabel('Feature')
plt.ylabel('Importance')
plt.show()

