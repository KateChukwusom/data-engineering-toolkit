import pandas as pd

df = pd.read_csv('transformed_data.csv')  # Load the transformed data
print(df.head())  # Show first 5 rows
df.to_parquet('final_data.parquet', index=False)  # Save to Parquet format