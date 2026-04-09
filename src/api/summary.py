from fastapi import APIRouter
import pandas as pd
from src.loader import load_data
from src.analysis import get_content_type_distribution,get_top_countries,get_yearly_trend,get_rating_distribution,get_duration_stats

summary_router = APIRouter()
data = load_data()
@summary_router.get('/summary',tags=["Json data"])
def total_numbers_json():
    
    result =get_content_type_distribution(data)
    return result

@summary_router.get('/countries',tags=["Json data"])
def top_countries_json(top: int = 10):
    if top <= 0:
        return {"Error":  "Must be between 0 and 10"}
        
    result = get_top_countries(data)  
    return dict(list(result.items())[:top])

@summary_router.get('/trends',tags=["Json data"])
def movies_trend_json(from_year: int = None, to_year: int = None):
    if (from_year >2021) or (from_year <1942):
        return {"Error":  "Must be between 1942 and 2021"}
    if (to_year >2021) or (to_year <1942):
        return {"Error":  "Must be between 1942 and 2021"}
    if from_year > to_year:
        return {"Error":  "From year must be less than or equal to to year"}

    result = get_yearly_trend(data) 
    filtered_trend = {
        str(year): count for year, count in result.items() 
         if int(year) >= from_year and int(year) <= to_year
    }
    return filtered_trend

@summary_router.get('/ratings',tags=["Json data"])
def rating_distribution_json():
    result = get_rating_distribution(data) 
    return result

@summary_router.get('/duration',tags=["Json data"])
def average_duration_json():
    result = get_duration_stats(data)
    return result


