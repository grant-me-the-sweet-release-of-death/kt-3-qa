import pytest
from base_request import BaseRequest
BASE_URL = "https://petstore.swagger.io/v2"
@pytest.fixture
def api():
    return BaseRequest(BASE_URL)
def test_create_order(api):
    data = {
        "id": 123,
        "petId": 56789,
        "quantity": 1,
        "shipDate": "2024-10-25T12:45:30.000Z",
        "status": "placed",
        "complete": True
    }
    response = api.post("/store/order", data=data)
    assert response.status_code == 200
def test_get_order(api):
    response = api.get("/store/order/123")
    assert response.status_code == 200
    assert response.json()["id"] == 123
def test_delete_order(api):
    response = api.delete("/store/order/123")
    assert response.status_code == 200
def test_inventory(api):
    response = api.get("/store/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)