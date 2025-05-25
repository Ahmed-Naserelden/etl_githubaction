# Weather ETL Pipeline

This project implements a daily ETL (Extract, Transform, Load) pipeline for weather data using GitHub Actions. The pipeline fetches weather data from OpenWeatherMap API, processes it, and stores the results in CSV files.

## Features

- Daily automated data collection from OpenWeatherMap API
- Data transformation and aggregation
- Data validation tests
- Comprehensive logging
- Automated workflow using GitHub Actions

## Setup

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your OpenWeatherMap API key:
   - Get an API key from [OpenWeatherMap](https://openweathermap.org/api)
   - Add it as a GitHub secret named `OPENWEATHER_API_KEY`

## Project Structure

- `extract.py`: Fetches weather data from OpenWeatherMap API
- `transform.py`: Processes and transforms the weather data
- `load.py`: Saves the processed data to CSV files
- `test_etl.py`: Contains data validation tests
- `.github/workflows/etl_pipeline.yml`: GitHub Actions workflow configuration

## Running the Pipeline

The pipeline runs automatically every day at midnight (UTC). You can also trigger it manually through the GitHub Actions interface.

## Output

The pipeline generates two types of CSV files in the `output` directory:
1. Detailed weather data for each city
2. Aggregated weather statistics by weather category

## Testing

Run the tests using:
```bash
pytest test_etl.py -v
```

## Logging

The pipeline includes comprehensive logging. Logs are available in the GitHub Actions workflow run details. 