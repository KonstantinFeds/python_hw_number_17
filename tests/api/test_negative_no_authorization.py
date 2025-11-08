import requests

headers_invalid = {"x-api-key": "reqres-free-V1", "Content-Type": "application/json"}

payload_valid = {"name": "ivan", "job": "driver"}


def test_create_user_response_no_valid_api_key():
    response = requests.post(
        url="https://reqres.in/api/users",
        json=payload_valid,
        headers=headers_invalid,
        timeout=10,
    )

    assert response.status_code == 403
    assert response.json() == {"error": "Invalid or inactive API key"}
