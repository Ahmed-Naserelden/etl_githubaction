import pandas as pd

# Load raw data
df = pd.read_csv("raw_data.csv")

# Simple transformations
df = df[['id', 'name', 'email', 'address']]
df['processed_at'] = pd.Timestamp.now()

# Save transformed data
df.to_csv("transformed_data.csv", index=False)