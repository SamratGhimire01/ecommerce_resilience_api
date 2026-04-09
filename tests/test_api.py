from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_total_numbers():
    response = client.get("/summary")
    assert response.status_code == 200
    assert "Movies" in response.json()

def test_top_countries():
    response = client.get("/countries?top=5")
    assert response.status_code == 200
    assert len(response.json()) == 5

def test_movies_trend():
    response = client.get("/trends?from_year=2000&to_year=2010")
    assert response.status_code == 200

def test_rating_distribution():
    response = client.get("/ratings")
    assert response.status_code == 200

def test_average_duration():
    response = client.get("/duration")
    assert response.status_code == 200