import pandas as pd

df = pd.read_csv('cleaned_data.csv')
df['age'] = df['age'] / 100  # Simple normalization: divide by 100
df['age_doubled'] = df['age'] * 2  # Custom transformation: double the age
df.to_csv('transformed_data.csv', index=False)