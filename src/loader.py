import pandas as pd
import os

netflix_cleaned = os.path.join('data','processed','netflix_cleaned.csv')


def load_data():
    with open(netflix_cleaned,'r') as file:
        df = pd.read_csv(netflix_cleaned)
        return df