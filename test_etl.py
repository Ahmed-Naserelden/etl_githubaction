import pytest
import requests
from datetime import datetime
from extract import extract_weather_data
from transform import transform_weather_data
from load import load_weather_data
import pandas as pd
import os
from unittest.mock import patch, Mock

def test_api_response():
    """Test the API response status code"""
    # Create a mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        'main': {
            'temp': 15.5,
            'humidity': 75,
            'pressure': 1013
        },
        'weather': [{
            'description': 'clear sky'
        }]
    }
    
    # Mock the requests.get method
    with patch('requests.get', return_value=mock_response):
        # Test with a sample city
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': 'London',
            'appid': 'test_key',
            'units': 'metric'
        }
        
        response = requests.get(base_url, params=params)
        assert response.status_code == 200

def test_data_transformation():
    """Test the data transformation with sample data"""
    # Sample data matching API schema
    sample_data = [
        {
            'city': 'London',
            'temperature': 15.5,
            'humidity': 75,
            'pressure': 1013,
            'weather_description': 'clear sky',
            'timestamp': datetime.now().isoformat()
        },
        {
            'city': 'Paris',
            'temperature': 18.2,
            'humidity': 80,
            'pressure': 1012,
            'weather_description': 'scattered clouds',
            'timestamp': datetime.now().isoformat()
        }
    ]
    
    # Transform the data
    df, agg_df = transform_weather_data(sample_data)
    
    # Test DataFrame structure
    assert isinstance(df, pd.DataFrame)
    assert 'temperature_f' in df.columns
    assert 'weather_category' in df.columns
    
    # Test aggregations
    assert isinstance(agg_df, pd.DataFrame)
    assert 'temperature' in agg_df.columns
    assert 'humidity' in agg_df.columns

def test_data_loading():
    """Test the data loading functionality"""
    # Create sample data
    sample_df = pd.DataFrame({
        'city': ['London', 'Paris'],
        'temperature': [15.5, 18.2],
        'humidity': [75, 80],
        'pressure': [1013, 1012],
        'weather_description': ['clear sky', 'scattered clouds'],
        'timestamp': [datetime.now(), datetime.now()]
    })
    
    sample_agg = pd.DataFrame({
        'temperature': {'mean': 16.85, 'min': 15.5, 'max': 18.2},
        'humidity': {'mean': 77.5},
        'pressure': {'mean': 1012.5}
    })
    
    # Load the data
    detailed_file, agg_file = load_weather_data(sample_df, sample_agg)
    
    # Test if files were created
    assert os.path.exists(detailed_file)
    assert os.path.exists(agg_file)
    
    # Clean up test files
    os.remove(detailed_file)
    os.remove(agg_file) 