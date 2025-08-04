import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_report_todo():
    response_todo = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    todo_id = response_todo.json()["data"]["id"]
    response = client.post("/api/v1/report-todo", json={
        "percentage": 100,
        "todo_id": todo_id
    })
    assert response.status_code == 201

def test_get_report_todo():
    response = client.get("/api/v1/report-todo")
    assert response.status_code == 200
    assert isinstance(response.json()["data"], list)

def test_get_report_todo_by_id():
    response_todo = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    todo_id = response_todo.json()["data"]["id"]
    response_status_todo = client.post("/api/v1/report-todo", json={
        "percentage": 100,
        "todo_id": todo_id
    })
    report_todo_id = response_status_todo.json()["data"]["id"]
    response = client.get(f"/api/v1/report-todo/{report_todo_id}")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == report_todo_id

def test_update_report_todo_by_id():
    response_todo = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    todo_id = response_todo.json()["data"]["id"]
    response_report_todo = client.post("/api/v1/report-todo", json={
        "percentage": 100,
        "todo_id": todo_id
    })
    report_todo_id = response_report_todo.json()["data"]["id"]
    response = client.put(f"/api/v1/report-todo/{report_todo_id}", json={
        "percentage": 100,
        "todo_id": todo_id
    })
    assert response.status_code == 200
    assert response.json()["data"]["id"] == report_todo_id

def test_delete_report_todo_by_id():
    response_todo = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    todo_id = response_todo.json()["data"]["id"]
    response_report_todo = client.post("/api/v1/report-todo", json={
        "percentage": 100,
        "todo_id": todo_id
    })
    report_todo_id = response_report_todo.json()["data"]["id"]
    response = client.delete(f"/api/v1/report-todo/{report_todo_id}")
    assert response.status_code == 200

def test_get_report_todo_not_found():
    response = client.get("/api/v1/report-todo/-1")
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"

def test_update_report_todo_not_found():
    response_todo = client.post("/api/v1/todos", json={
        "name": "Test Todo",
        "description": "Testing purpose"
    })
    todo_id = response_todo.json()["data"]["id"]
    response = client.put("/api/v1/report-todo/-1", json={
        "status": "OK",
        "todo_id": todo_id
    })
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"

def test_delete_report_todo_not_found():
    response = client.delete("/api/v1/report-todo/-1")
    assert response.status_code == 404
    assert response.json()["message"] == "Not found"