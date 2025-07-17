import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_todo():
    response = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    assert response.status_code == 201
    assert response.json()["data"]["name"] == "Test Todo"

def test_get_todos():
    response = client.get("/api/v1/todos")
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)

def test_update_todo():
    response = client.post("/api/v1/todos", json={
        "name": "Initial Todo",
        "description": "Initial description"
    })
    todo_id = response.json()["data"]["id"]

    response = client.put(f"/api/v1/todos/{todo_id}", json={
        "name": "Updated Todo",
        "description": "Updated description"
    })

    assert response.status_code == 200
    assert response.json()["data"]["name"] == "Updated Todo"

def test_get_single_todo():
    response = client.post("/api/v1/todos", json={
        "name": "Single Todo",
        "description": "Get one"
    })
    todo_id = response.json()["data"]["id"]
    response = client.get(f"/api/v1/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == todo_id

def test_delete_todo():
    response = client.post("/api/v1/todos", json={
        "name": "Todo to delete",
        "description": "Will be deleted"
    })
    todo_id = response.json()["data"]["id"]
    response = client.delete(f"/api/v1/todos/{todo_id}")
    assert response.status_code == 200
    response = client.get(f"/api/v1/todos/{todo_id}")
    assert response.status_code == 404 or response.status_code == 200 and response.json()["data"] is None

def test_get_non_existing_todo():
    response = client.get("/api/v1/todos/-1")
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"

def test_update_non_existing_todo():
    response = client.put("/api/v1/todos/-1", json={
        "name": "Should Fail",
        "description": "No such ID"
    })
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"

def test_delete_non_existing_todo():
    response = client.delete("/api/v1/todos/-1")
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"