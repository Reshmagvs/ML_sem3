import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
\
data = load_iris()
X = data.data 
y = data.target  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

log_reg = LogisticRegression(random_state=42)
decision_tree = DecisionTreeClassifier(random_state=42)
svc = SVC(probability=True, random_state=42)

ensemble_model = VotingClassifier(estimators=[
    ('lr', log_reg),
    ('dt', decision_tree),
    ('svc', svc)
], voting='soft') 

ensemble_model.fit(X_train, y_train)


y_pred = ensemble_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy of Ensemble Model: {accuracy * 100:.2f}%')

print("\nIndividual Model Performance:")
for clf, label in zip([log_reg, decision_tree, svc], ['Logistic Regression', 'Decision Tree', 'SVC']):
    clf.fit(X_train, y_train)
    y_pred_individual = clf.predict(X_test)
    print(f'{label} Accuracy: {accuracy_score(y_test, y_pred_individual) * 100:.2f}%')
