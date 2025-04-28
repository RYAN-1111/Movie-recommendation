from fastapi.testclient import TestClient

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from backend.main import app  # replace this!
from fastapi.testclient import TestClient
from backend.main import app  # make sure the path is correct

from fastapi.testclient import TestClient
from backend.main import app  # make sure the path is correct

client = TestClient(app)

def test_recommend_success_valid_movie():
    response = client.get("/recommend", params={"movie": "Inception"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "recommended_movies" in data
    assert isinstance(data["recommended_movies"], list)
    assert len(data["recommended_movies"]) > 0  # should return at least one recommendation

def test_recommend_success_another_movie():
    response = client.get("/recommend", params={"movie": "Titanic"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "recommended_movies" in data
    assert isinstance(data["recommended_movies"], list)

def test_recommend_failure_missing_movie():
    response = client.get("/recommend")
    assert response.status_code == 422  # missing required 'movie' param

def test_recommend_failure_invalid_movie():
    response = client.get("/recommend", params={"movie": "asldkfjalskdjf"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "recommended_movies" in data
    assert isinstance(data["recommended_movies"], list)

def test_recommend_failure_numeric_input():
    response = client.get("/recommend", params={"movie": 12345})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "recommended_movies" in data
    assert isinstance(data["recommended_movies"], list)
