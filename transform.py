import pandas as pd
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def transform_weather_data(weather_data):
    """
    Transform the extracted weather data
    """
    try:
        logger.info("Starting data transformation")
        
        # Convert to DataFrame
        df = pd.DataFrame(weather_data)
        
        # Convert timestamp to datetime
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        # Add derived columns
        df['temperature_f'] = (df['temperature'] * 9/5) + 32  # Convert to Fahrenheit
        df['pressure_hpa'] = df['pressure']  # Pressure in hPa
        df['humidity_percentage'] = df['humidity']  # Humidity as percentage
        
        # Create weather condition categories
        df['weather_category'] = df['weather_description'].apply(
            lambda x: 'Clear' if 'clear' in x.lower() 
            else 'Cloudy' if 'cloud' in x.lower()
            else 'Rainy' if 'rain' in x.lower()
            else 'Other'
        )
        
        # Calculate some aggregations
        aggregations = {
            'temperature': ['mean', 'min', 'max'],
            'humidity': ['mean'],
            'pressure': ['mean']
        }
        
        agg_df = df.groupby('weather_category').agg(aggregations)
        logger.info("Data transformation completed successfully")
        
        return df, agg_df
        
    except Exception as e:
        logger.error(f"Error during data transformation: {str(e)}")
        raise

if __name__ == "__main__":
    # This is just for testing
    sample_data = [
        {
            'city': 'London',
            'temperature': 15,
            'humidity': 75,
            'pressure': 1013,
            'weather_description': 'clear sky',
            'timestamp': datetime.now().isoformat()
        }
    ]
    transform_weather_data(sample_data) 