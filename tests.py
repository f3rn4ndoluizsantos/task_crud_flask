import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

tasks = []


def test_create_task():
    new_task_data = {"title": "Nova tarefa", "description": "Descrição da nova tarefa"}
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 201
    response_json = response.json()
    # content response_json {'id': 1, 'message': 'New task created'}
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])


def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    response_json = response.json()
    assert response.status_code == 200
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        response_json = response.json()
        assert response.status_code == 200
        assert "task" in response_json
        assert task_id == response_json["task"]["id"]


def test_get_task_error():
    if tasks:
        task_id = 9999
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        response_json = response.json()
        assert response.status_code == 404
        assert "message" in response_json


def teste_update_task():
    payload = {
        "title": "New Title",
        "description": "New Description",
        "completed": True,
    }
    if tasks:
        task_id = tasks[0]
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        response_json = response.json()
        assert response.status_code == 200
        assert "message" in response_json
        assert "id" in response_json
        assert task_id == response_json["id"]

        response_2 = requests.get(f"{BASE_URL}/tasks/{task_id}")
        response_json_2 = response_2.json()
        assert response_2.status_code == 200
        assert "task" in response_json_2
        assert task_id == response_json_2["task"]["id"]
        assert payload["title"] == response_json_2["task"]["title"]
        assert payload["description"] == response_json_2["task"]["description"]
        assert payload["completed"] == response_json_2["task"]["completed"]


def teste_update_task_error():
    payload = {
        "title": "New Title",
        "description": "New Description",
        "completed": True,
    }
    if tasks:
        task_id = 9999
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        response_json = response.json()
        assert response.status_code == 404
        assert "message" in response_json


def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        data = response.json()
        assert response.status_code == 200
        assert "message" in data
        assert "id" in data
        assert task_id == data["id"]

        response_2 = requests.get(f"{BASE_URL}/tasks/{task_id}")
        response_json_2 = response_2.json()
        assert response_2.status_code == 404
        assert "message" in response_json_2


def test_delete_task_error():
    if tasks:
        task_id = 9999
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        data = response.json()
        assert response.status_code == 404
        assert "message" in data
