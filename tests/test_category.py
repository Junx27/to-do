import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_category():
    response = client.post("/api/v1/category", json={
        "name": "Database"
    })
    assert response.status_code == 201
    assert response.json()["data"]["name"] == "Database"

def test_get_categories():
    response = client.get("/api/v1/category")
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)

def test_update_category():
    response = client.post("/api/v1/category", json={
        "name": "First"
    })

    category_id = response.json()["data"]["id"]
    response = client.put(f"/api/v1/category/{category_id}", json={
        "name": "Second"
    })

    assert response.status_code == 200
    assert response.json()["data"]["name"] == "Second"

def test_get_category_by_id():
    response = client.post("/api/v1/category", json={
        "name": "Go"
    })
    category_id = response.json()["data"]["id"]
    response = client.get(f"/api/v1/category/{category_id}")
    assert response.status_code == 200

def test_delete_category():
    response = client.post("/api/v1/category", json={
        "name": "Python"
    })
    category_id = response.json()["data"]["id"]
    response = client.delete(f"/api/v1/category/{category_id}")
    assert response.status_code == 200

def test_update_non_exist():
    response = client.put("/api/v1/category/-1", json={
        "name": "Not found"
    })
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"

def test_get_non_exist():
    response = client.get("/api/v1/category/-1")
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"

def test_delete_non_exist():
    response = client.get("/api/v1/category/-1")
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"