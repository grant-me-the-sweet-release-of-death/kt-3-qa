import pytest
from base_request import BaseRequest
BASE_URL = "https://petstore.swagger.io/v2"
@pytest.fixture
def api():
    return BaseRequest(BASE_URL)
def test_create_user(api):
    data = {
        "id": 12345,
        "username": "test_user",
        "firstName": "Test",
        "lastName": "User",
        "email": "testuser@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1
    }
    response = api.post("/user", data=data)
    assert response.status_code == 200
def test_get_user(api):
    response = api.get("/user/test_user")
    assert response.status_code == 200
    assert response.json()["username"] == "test_user"
def test_update_user(api):
    updated_data = {"firstName": "UpdatedTest", "lastName": "UpdatedUser"}
    response = api.put("/user/test_user", data=updated_data)
    assert response.status_code == 200
def test_delete_user(api):
    response = api.delete("/user/test_user")
    assert response.status_code == 200