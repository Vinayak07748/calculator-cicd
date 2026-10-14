from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "calculator API is running"
    }


def test_multiply():
    response = client.get("/multiply?a=5&b=4")
    assert response.status_code == 200
    assert response.json()["result"] == 20