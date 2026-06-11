
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

sample = {
    "gross_amount":1000.0,
    "quantity":2,
    "returned":0.0,
    "rating":4.5,
    "discount_pct":0.2,
    "delivery_days":3,
    "city_tier":0,
    "age_group":1,
    "acquisition_channel":2,
    "loyalty_tier":3,
    "preferred_category":3,
    "skin_type":0,
    "marketing_consent":1
}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_predict():
    response = client.post("/predict", json=sample)
    assert response.status_code == 200

def test_batch_predict():
    response = client.post("/batch_predict", json=[sample])
    assert response.status_code == 200
