def test_inventory_response():
    response = client.get("/inventory")

    assert response.status_code == 200

def test_negative_stock_prevention():
    response = client.post(
        "/purchase",
        json={"quantity": 999}
    )

    assert response.status_code == 400