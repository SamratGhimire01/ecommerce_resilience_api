from fastapi import FastAPI
from src.api.endpoints import router
from src.api.summary import summary_router

app = FastAPI()

@app.get('/')
def home():
    return {'msg':'Wel-come to Netflix Data Analysis Api.'}

app.include_router(router)
app.include_router(summary_router)