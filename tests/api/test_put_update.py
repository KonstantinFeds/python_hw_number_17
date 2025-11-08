import json
import os
from faker import Faker
import requests
from jsonschema import validate

SCHEMAS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "schemas")

fake = Faker()

headers_valid = {"x-api-key": "reqres-free-v1", "Content-Type": "application/json"}

payload_valid = {
    "name": fake.first_name() + str(fake.random_number(digits=3)),
    "job": fake.job(),
}


def test_put_update_user_response_schema_is_valid():
    response = requests.put(
        url="https://reqres.in/api/users/1",
        headers=headers_valid,
        json=payload_valid,
        timeout=10,
    )

    assert response.status_code == 200

    schema_path = os.path.join(SCHEMAS_DIR, "put_update_user.json")
    with open(schema_path, encoding="utf-8") as file:
        schema = json.load(file)
    validate(response.json(), schema)

    response_data = response.json()
    assert response_data["name"] == payload_valid["name"]
    assert response_data["job"] == payload_valid["job"]

    print(response.json())
