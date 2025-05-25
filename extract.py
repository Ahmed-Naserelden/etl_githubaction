import requests
import pandas as pd

# Get data from API
response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

# Save raw data
pd.DataFrame(data).to_csv("raw_data.csv", index=False)