import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"

tasks = []


def test_create_task():
    new_task_data = {"title": "Nova tarefa", "description": "Descrição da nova tarefa"}
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 201
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json["id"])


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        response_json = response.json()
        print(response_json)
        assert response.status_code == 200
        assert "task" in response_json
        assert task_id == response_json["task"]["id"]


if __name__ == "__main__":
    test_create_task()
    print(tasks)
    test_get_task()
