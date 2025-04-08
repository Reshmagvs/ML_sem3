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

print(f"Accuracy: {accuracy:.2f}")
print(f"Recall: {recall:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Specificity: {specificity:.2f}")
print(f"Error Rate: {error_rate:.2f}")

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Predicted 0', 'Predicted 1'], yticklabels=['Actual 0', 'Actual 1'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
