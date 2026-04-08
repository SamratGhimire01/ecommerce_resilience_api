import pandas as pd
import numpy as np
from loader import load_data


data = load_data()

def get_content_type_distribution(data):
    total_movies = (data.type == "Movie").sum()
    total_series =(data.type == "TV Show").sum()
    return {
        'Movies': int((total_movies)),
        'TV Shows': int((total_series))
    }

def get_top_countries(data):
    return data.country.value_counts().head(10).to_dict()

def get_yearly_trend(data):
    return data.release_year.value_counts().sort_index().to_dict()

def get_rating_distribution(data):
    return data.rating.value_counts().head(10).to_dict()

def get_duration_stats(data):
    return{
        'average_duration_minutes': int(np.ceil(data[data['Total_minutes']>0]['Total_minutes'].mean())),
        'average_seasons': int(np.ceil(data[data['Total_seasons']>0]['Total_seasons'].mean())) 
    }

# print(get_content_type_distribution(data),
# get_top_countries(data),
# get_yearly_trend(data),
# get_rating_distribution(data),
# get_duration_stats(data))