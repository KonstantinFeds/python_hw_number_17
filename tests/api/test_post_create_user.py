import json
import requests
from jsonschema import validate

payload_valid = {
  "name": "ivan",
  "job": "driver"
}
headers_valid = {
  'x-api-key': 'reqres-free-v1',
  'Content-Type': 'application/json'
}

headers_invalid = {
  'x-api-key': 'reqres-free-V1',
  'Content-Type': 'application/json'
}


def test_create_user_response_schema_is_valid():
    response = requests.post(
        url='https://reqres.in/api/users',
        json=payload_valid,
        headers=headers_valid)

    assert response.status_code == 201

    with open('schemas/post_create_user.json') as file:
        schema = json.load(file)
    validate(response.json(), schema)


def test_create_user_response_no_valid_api_key():
    response = requests.post(
        url='https://reqres.in/api/users',
        json=payload_valid,
        headers=headers_invalid)

    assert response.status_code == 403
    assert response.json() == {"error": "Invalid or inactive API key"}









