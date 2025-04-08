import pandas as pd

data = {
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6],
    'Column3': [7, 8, 9]
}

df = pd.DataFrame(data)

df = pd.read_csv('file_path.csv')
df.head(3)
df.info()
df['Column1']
df[['Column1', 'Column2']]
df.iloc[0]

df.loc[0]
filtered_df = df[df['Column1'] > 1]
df['NewColumn'] = [10, 11, 12]
df = df.drop(columns=['Column1'])
df = df.dropna()
df = df.sort_values(by='Column2')
df = df.sort_values(by=['Column1', 'Column2'])
df.sum()


df.mean()
df.to_csv('output_file.csv', index=False)
