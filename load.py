import pandas as pd

# Load transformed data
df = pd.read_csv("transformed_data.csv")

# Save final output
df.to_csv("final_data.csv", index=False)