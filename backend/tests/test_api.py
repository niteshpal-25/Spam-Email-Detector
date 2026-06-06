from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health_check():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"


def test_model_info():

    response = client.get("/model-info")

    assert response.status_code == 200

    data = response.json()

    assert "model" in data
    assert "accuracy" in data


def test_predict_spam():

    payload = {
        "message":
        "Congratulations! You won a free iPhone."
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data
    assert "confidence" in data


def test_predict_normal_message():

    payload = {
        "message":
        "Hi Vishal, let's meet tomorrow."
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data