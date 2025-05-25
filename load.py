import pandas as pd
import logging
from datetime import datetime
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_weather_data(df, agg_df):
    """
    Load the transformed weather data into CSV files
    """
    try:
        logger.info("Starting data loading process")
        
        # Create output directory if it doesn't exist
        output_dir = 'output'
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate timestamp for file names
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Save detailed data
        detailed_file = f'{output_dir}/weather_data_{timestamp}.csv'
        df.to_csv(detailed_file, index=False)
        logger.info(f"Detailed weather data saved to {detailed_file}")
        
        # Save aggregated data
        agg_file = f'{output_dir}/weather_aggregations_{timestamp}.csv'
        agg_df.to_csv(agg_file)
        logger.info(f"Aggregated weather data saved to {agg_file}")
        
        return detailed_file, agg_file
        
    except Exception as e:
        logger.error(f"Error during data loading: {str(e)}")
        raise

if __name__ == "__main__":
    # This is just for testing
    sample_df = pd.DataFrame({
        'city': ['London'],
        'temperature': [15],
        'humidity': [75],
        'pressure': [1013],
        'weather_description': ['clear sky'],
        'timestamp': [datetime.now()]
    })
    sample_agg = pd.DataFrame({
        'temperature': {'mean': 15, 'min': 15, 'max': 15},
        'humidity': {'mean': 75},
        'pressure': {'mean': 1013}
    })
    load_weather_data(sample_df, sample_agg) 