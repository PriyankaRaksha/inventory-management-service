from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_product():

    response = client.post("/products")

    assert response.status_code == 200