from fastapi import FastAPI
import os
from fastapi.responses import FileResponse
from src.analysis import data
from src.viz import plot_average_duration,plot_content_distribution,plot_yearly_trend,plot_top_countries,plot_rating_distribution
from src.reporter import duration_report,report_content_distribution,report_yearly_trend,report_top_countries,report_rating_distribution

app = FastAPI()

@app.get('/average-duration',tags=["Visualizations"])
def get_average_duration():
    image_path = './images/average_duration.png'
    
   
    if not os.path.exists(image_path):
        plot_average_duration(data) 
    
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type='image/png')
    
    return {"Error": "Cannot Access Image."}

@app.get('/duration-report',tags=["Reports"])
def get_duration_reports():
    duration_report('./images/average_duration.png')
    
    pdf_path = 'Duration_Report.pdf'
    
    if os.path.exists(pdf_path):
        return FileResponse(path=pdf_path, media_type='application/pdf', filename=pdf_path)
    
    return {"Error":"Report Not Found."}

@app.get('/content_distribution',tags=["Visualizations"])
def get_content_distribution():
    image_path = './images/content_distribution.png'
    
   
    if not os.path.exists(image_path):
        plot_content_distribution(data)
    
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type='image/png')
    
    return {"Error": "Cannot Access Image."}

@app.get('/report_content_distribution',tags=["Reports"])
def get_report_content_distribution():
    report_content_distribution('./images/content_distribution.png')
    
    pdf_path = 'Content_Distribution.pdf'
    
    if os.path.exists(pdf_path):
        return FileResponse(path=pdf_path, media_type='application/pdf', filename=pdf_path)
    
    return {"Error":"Report Not Found."}

@app.get('/yearly_trend',tags=["Visualizations"])
def get_yearly_trend():
    image_path = './images/yearly_trend.png'
    
   
    if not os.path.exists(image_path):
        plot_yearly_trend(data)
    
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type='image/png')
    
    return {"Error": "Cannot Access Image."}

@app.get('/report_yearly_trend',tags=["Reports"])
def get_report_yearly_trend():
    report_yearly_trend('./images/yearly_trend.png')
    
    pdf_path = 'Yearly_Trends.pdf'
    
    if os.path.exists(pdf_path):
        return FileResponse(path=pdf_path, media_type='application/pdf', filename=pdf_path)
    
    return {"Error":"Report Not Found."}

@app.get('/top_countries',tags=["Visualizations"])
def get_top_countries():
    image_path = './images/top_countries.png'
    
   
    if not os.path.exists(image_path):
        plot_top_countries(data)
    
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type='image/png')
    
    return {"Error": "Cannot Access Image."}

@app.get('/report_top_countries',tags=["Reports"])
def get_report_top_countries():
    report_top_countries('./images/top_countries.png')
    
    pdf_path = 'top_countries.pdf'
    
    if os.path.exists(pdf_path):
        return FileResponse(path=pdf_path, media_type='application/pdf', filename=pdf_path)
    
    return {"Error":"Report Not Found."}

@app.get('/rating_distribution',tags=["Visualizations"])
def get_rating_distribution():
    image_path = './images/rating_distribution.png'
    
   
    if not os.path.exists(image_path):
        plot_rating_distribution(data)
    
    if os.path.exists(image_path):
        return FileResponse(image_path, media_type='image/png')
    
    return {"Error": "Cannot Access Image."}

@app.get('/report_rating_distribution',tags=["Reports"])
def get_report_rating_distribution():
    report_rating_distribution('./images/rating_distribution.png')
    
    pdf_path = 'rating_distribution.pdf'
    
    if os.path.exists(pdf_path):
        return FileResponse(path=pdf_path, media_type='application/pdf', filename=pdf_path)
    
    return {"Error":"Report Not Found."}