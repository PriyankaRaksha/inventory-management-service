from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_stock():

    response = client.get("/stock")

    assert response.status_code == 200