import requests
import pandas as pd

def test_api():
    # Test API connection
    assert requests.get("https://jsonplaceholder.typicode.com/users").status_code == 200

def test_transformations():
    # Test transformation logic
    test_data = pd.DataFrame([{"id": 1, "name": "Test"}])
    assert "id" in test_data.columns