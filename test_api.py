from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_calculate_add():
    response = client.get(
        "/calculate", params={"num1": 10, "num2": 3, "operation": "+"}
    )
    data = response.json()
    assert response.status_code == 200
    assert data["result"] == 13


def test_calculate_subtract():
    response = client.get(
        "/calculate", params={"num1": 10, "num2": 5, "operation": "-"}
    )
    data = response.json()
    assert response.status_code == 200
    assert data["result"] == 5


def test_calculate_multiply():
    response = client.get(
        "/calculate", params={"num1": 10, "num2": 5, "operation": "*"}
    )
    data = response.json()
    assert response.status_code == 200
    assert data["result"] == 50


def test_calculate_divide():
    response = client.get(
        "/calculate", params={"num1": 10, "num2": 5, "operation": "/"}
    )
    data = response.json()
    assert response.status_code == 200
    assert data["result"] == 2
