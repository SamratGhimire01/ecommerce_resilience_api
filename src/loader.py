import pandas as pd
import os

netflix_cleaned = os.path.join('data','processed','netflix_cleaned.csv')


def load_data():
    with open(netflix_cleaned,'r') as file:
        try:
            df = pd.read_csv(netflix_cleaned)
        except Exception as e:
            raise f"Error Loading Data: {e}"
        return df