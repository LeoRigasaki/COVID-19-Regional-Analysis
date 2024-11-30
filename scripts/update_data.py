# scripts/update_data.py

import requests
import pandas as pd
from datetime import datetime, timezone

# URL of the OWID COVID-19 dataset
DATA_URL = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

# Path to save the dataset
DATA_PATH = 'data/owid-covid-data.csv'

def fetch_data(url, path):
    response = requests.get(url)
    response.raise_for_status()  # Ensure we could be able to fetch data or notice bad responses
    with open(path, 'wb') as f:
        f.write(response.content)

def show_data_preview(path):
    # Read the dataset into a Pandas DataFrame
    df = pd.read_csv(path)
    # Print the first few rows
    print("\nData Preview:\n")
    print(df.head().to_string())  # Use to_string() for better log readability

def main():
    # Fetch the latest data
    fetch_data(DATA_URL, DATA_PATH)
    # Log the update time with timezone-aware datetime
    print(f'Data updated at {datetime.now(timezone.utc).isoformat()}')
    # Display data preview
    show_data_preview(DATA_PATH)

if __name__ == '__main__':
    main()
