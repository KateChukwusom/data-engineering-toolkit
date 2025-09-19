import pandas as pd
# Load your data
df = pd.read_csv('your_data.csv')

# Remove duplicates and drop rows with missing values
df = df.drop_duplicates().dropna()
