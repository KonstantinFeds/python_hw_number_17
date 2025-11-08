import json
import os
import requests
from jsonschema import validate

SCHEMAS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "schemas")

headers_valid = {"x-api-key": "reqres-free-v1", "Content-Type": "application/json"}


def test_get_list_users_response_schema_is_valid():
    response = requests.get(
        url="https://reqres.in/api/users",
        headers=headers_valid,
        params={"page": 1},
        timeout=10,
    )

    assert response.status_code == 200

    schema_path = os.path.join(SCHEMAS_DIR, "get_list_users.json")
    with open(schema_path, encoding="utf-8") as file:
        schema = json.load(file)
    validate(response.json(), schema)
