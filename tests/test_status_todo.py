import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_status_todo():
    response_todo = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    todo_id = response_todo.json()["data"]["id"]
    response = client.post("/api/v1/status-todo", json={
        "status": "OK",
        "todo_id": todo_id
    })
    assert response.status_code == 201

def test_get_status_todo():
    response = client.get("/api/v1/status-todo")
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)

def test_get_status_todo_by_id():
    response_todo = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    todo_id = response_todo.json()["data"]["id"]
    response_status_todo = client.post("/api/v1/status-todo", json={
        "status": "OK",
        "todo_id": todo_id
    })
    status_todo_id = response_status_todo.json()["data"]["id"]
    response = client.get(f"/api/v1/status-todo/{status_todo_id}")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == status_todo_id

def test_update_status_todo_by_id():
    response_todo = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    todo_id = response_todo.json()["data"]["id"]
    response_status_todo = client.post("/api/v1/status-todo", json={
        "status": "OK",
        "todo_id": todo_id
    })
    status_todo_id = response_status_todo.json()["data"]["id"]
    response = client.put(f"/api/v1/status-todo/{status_todo_id}", json={
        "status": "FAILED",
        "todo_id": todo_id
    })
    assert response.status_code == 200
    assert response.json()["data"]["id"] == status_todo_id

def test_delete_status_todo_by_id():
    response_todo = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    todo_id = response_todo.json()["data"]["id"]
    response_status_todo = client.post("/api/v1/status-todo", json={
        "status": "OK",
        "todo_id": todo_id
    })
    status_todo_id = response_status_todo.json()["data"]["id"]
    response = client.delete(f"/api/v1/status-todo/{status_todo_id}")
    assert response.status_code == 200

def test_get_status_todo_not_found():
    response = client.get("/api/v1/status-todo/-1")
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"

def test_update_status_todo_not_found():
    response_todo = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    todo_id = response_todo.json()["data"]["id"]
    response = client.put("/api/v1/status-todo/-1", json={
        "status": "OK",
        "todo_id": todo_id
    })
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"

def test_delete_status_todo_not_found():
    response = client.delete("/api/v1/status-todo/-1")
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"