def test_inventory_response():
    response = client.get("/inventory")

    assert response.status_code == 200