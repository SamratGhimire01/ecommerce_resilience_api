import pandas as pd
import numpy as np
from loader import load_data


data = load_data()
print(data.head())
total_movies = (data.type == "Movie").sum()
total_series =(data.type == "TV Show").sum()
print(total_movies,total_series)


print((data.country.value_counts().head(10)))


print((data.release_year.value_counts().sort_index()))

print((data.rating.value_counts().head(10)))

print(np.ceil(data[data['Total_minutes']>0]['Total_minutes'].mean()))
print(np.ceil(data[data['Total_seasons']>0]['Total_seasons'].mean()))