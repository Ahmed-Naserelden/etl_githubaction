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
    Extract weather data from Open-Meteo API for major cities
    """
    try:
        logger.info("Starting data extraction from Open-Meteo API")
        
        # List of major cities with their coordinates
        cities = {
            'London': {'lat': 51.5074, 'lon': -0.1278},
            'New York': {'lat': 40.7128, 'lon': -74.0060},
            'Tokyo': {'lat': 35.6762, 'lon': 139.6503},
            'Paris': {'lat': 48.8566, 'lon': 2.3522},
            'Sydney': {'lat': -33.8688, 'lon': 151.2093}
        }
        
        base_url = "https://api.open-meteo.com/v1/forecast"
        weather_data = []
        
        for city, coords in cities.items():
            logger.info(f"Fetching weather data for {city}")
            params = {
                'latitude': coords['lat'],
                'longitude': coords['lon'],
                'current': 'temperature_2m,relative_humidity_2m,pressure_msl,weather_code',
                'timezone': 'auto'
            }
            
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
            current = data['current']
            
            # Map weather codes to descriptions
            weather_codes = {
                0: 'Clear sky',
                1: 'Mainly clear',
                2: 'Partly cloudy',
                3: 'Overcast',
                45: 'Foggy',
                48: 'Depositing rime fog',
                51: 'Light drizzle',
                53: 'Moderate drizzle',
                55: 'Dense drizzle',
                61: 'Slight rain',
                63: 'Moderate rain',
                65: 'Heavy rain',
                71: 'Slight snow',
                73: 'Moderate snow',
                75: 'Heavy snow',
                77: 'Snow grains',
                80: 'Slight rain showers',
                81: 'Moderate rain showers',
                82: 'Violent rain showers',
                85: 'Slight snow showers',
                86: 'Heavy snow showers',
                95: 'Thunderstorm',
                96: 'Thunderstorm with slight hail',
                99: 'Thunderstorm with heavy hail'
            }
            
            weather_description = weather_codes.get(current['weather_code'], 'Unknown')
            
            weather_data.append({
                'city': city,
                'temperature': current['temperature_2m'],
                'humidity': current['relative_humidity_2m'],
                'pressure': current['pressure_msl'],
                'weather_description': weather_description,
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