import requests
import logging
import os
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def extract_weather_data():
    """
    Extract weather data from OpenWeatherMap API for major cities
    """
    try:
        # Get API key from environment variable
        api_key = os.getenv('OPENWEATHER_API_KEY')
        logger.info("Checking for OpenWeather API key...")
        
        if not api_key:
            logger.error("OpenWeather API key not found in environment variables")
            raise ValueError("OpenWeather API key not found in environment variables. Please set the OPENWEATHER_API_KEY environment variable.")
        
        logger.info("API key found, proceeding with data extraction")

        # List of major cities
        cities = ['London', 'New York', 'Tokyo', 'Paris', 'Sydney']
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        weather_data = []
        
        for city in cities:
            logger.info(f"Fetching weather data for {city}")
            params = {
                'q': city,
                'appid': api_key,
                'units': 'metric'  # For Celsius
            }
            
            response = requests.get(base_url, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes
            
            data = response.json()
            weather_data.append({
                'city': city,
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'weather_description': data['weather'][0]['description'],
                'timestamp': datetime.now().isoformat()
            })
            
        logger.info(f"Successfully extracted weather data for {len(cities)} cities")
        return weather_data
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data from API: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during data extraction: {str(e)}")
        raise

if __name__ == "__main__":
    extract_weather_data() 