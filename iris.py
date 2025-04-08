import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv('iris.csv')


print("Columns with null values:\n", df.isnull().sum())
print("\nRows with null values:\n", df[df.isnull().any(axis=1)])


df.fillna(df.mean(numeric_only=True), inplace=True)


plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='SepalLengthCm', y='SepalWidthCm', hue='Species', palette='Set1')
plt.title('Scatter Plot of Sepal Length vs Sepal Width by Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend(title='Species')
plt.show()

print("\nMetadata of the dataset:\n")
print(df.info())

df['SizeCategory'] = pd.cut(df['SepalLengthCm'], bins=[0, 5.0, 6.0, np.inf], labels=['Small', 'Medium', 'Large'])

label_encoder = LabelEncoder()
df['SizeCategoryEncoded'] = label_encoder.fit_transform(df['SizeCategory'])

plt.figure(figsize=(10, 6))
for species in df['Species'].unique():
    species_df = df[df['Species'] == species]
    plt.plot(species_df['SepalLengthCm'], label=species)
plt.title('Line Graph of Sepal Length for Different Species')
plt.xlabel('Index')
plt.ylabel('Sepal Length (cm)')
plt.legend(title='Species')
plt.show()


df_setosa = df[df['Species'] == 'Iris-setosa']
df_versicolor = df[df['Species'] == 'Iris-versicolor']
df_virginica = df[df['Species'] == 'Iris-virginica']


df_merged = pd.concat([df_setosa, df_versicolor])
df_merged.to_csv('merged_species.csv', index=False)

 
df_imported = pd.read_csv('merged_species.csv')
df_final = pd.concat([df_imported, df_virginica])
print("\nDescription of the final merged DataFrame:\n")
print(df_final.describe())
