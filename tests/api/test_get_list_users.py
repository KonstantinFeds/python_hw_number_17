import json
import requests
from jsonschema import validate


headers_valid = {
  'x-api-key': 'reqres-free-v1',
  'Content-Type': 'application/json'
}

def test_get_list_users_response_schema_is_valid():
    response = requests.get(
        url='https://reqres.in/api/users',
        headers=headers_valid,
        params={"page": 1})

    assert response.status_code == 200

    with open('schemas/get_list_users.json') as file:
        schema = json.load(file)
    validate(response.json(), schema)


def test_get_users_returns_unique_users():
    response = requests.get(
        url="https://reqres.in/api/users",
        params={"page": 2, "per_page": 4},
    )
    ids = [element["id"] for element in response.json()["data"]]

    assert len(ids) == len(set(ids))





