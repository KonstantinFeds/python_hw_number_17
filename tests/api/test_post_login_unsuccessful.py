import json
import os

import requests
from jsonschema import validate

SCHEMAS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "schemas")

headers_valid = {"x-api-key": "reqres-free-v1", "Content-Type": "application/json"}

payload_valid = {
    "email": "767ivan999@test.com",
}


def test_login_unsuccessful():
    response = requests.post(
        url="https://reqres.in/api/login",
        json=payload_valid,
        headers=headers_valid,
        timeout=10,
    )

    assert response.status_code == 400

    schema_path = os.path.join(SCHEMAS_DIR, "post_unsuccessful.json")
    with open(schema_path, encoding="utf-8") as file:
        schema = json.load(file)
    validate(response.json(), schema)
