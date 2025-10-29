import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# ----------------------------
# Successful operation tests
# ----------------------------

def test_add_success():
    response = client.post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_subtract_success():
    response = client.post("/subtract", json={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2}

def test_multiply_success():
    response = client.post("/multiply", json={"a": 4, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 12}

def test_divide_success():
    response = client.post("/divide", json={"a": 6, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result": 2.0}

# ----------------------------
# Error handling tests
# ----------------------------

def test_divide_by_zero():
    response = client.post("/divide", json={"a": 5, "b": 0})
    assert response.status_code == 400
    assert response.json() == {"error": "Cannot divide by zero!"}

def test_invalid_input_type():
    response = client.post("/add", json={"a": "foo", "b": 2})
    assert response.status_code == 400
    # Updated assertion to match main.py error message
    assert "a: Input should be a valid number" in response.json()["error"]

def test_missing_field():
    response = client.post("/subtract", json={"a": 2})
    assert response.status_code == 400
    # Updated assertion to match main.py error message
    assert "b: Field required" in response.json()["error"]

def test_extra_field_ignored():
    response = client.post("/multiply", json={"a": 2, "b": 3, "c": 100})
    # Extra fields are ignored by default
    assert response.status_code == 200
    assert response.json() == {"result": 6}
