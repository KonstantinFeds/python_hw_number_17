import requests

headers_valid = {"x-api-key": "reqres-free-v1", "Content-Type": "application/json"}


def test_delete_user():
    response = requests.delete(
        url="https://reqres.in/api/users/9", headers=headers_valid, timeout=10
    )

    assert response.status_code == 204
