import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

df = pd.read_csv("newcsv.csv")

actual = df['Actual']
predicted = df['Predicted']

cm = confusion_matrix(actual, predicted)

TP, FP, FN, TN = cm.ravel()

accuracy = (TP + TN) / (TP + FP + TN + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
error_rate = (FP + FN) / (TP + TN + FP + FN)
specificity = TN / (TN + FP)

print("acccuracy")
print("precision")
print("recall")
print("error_rate")
print("specificity")

plt.show()

