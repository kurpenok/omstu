from jsonschema import validate

from api_client import RestfulBookerAPI


class TestAuthToken:
    def setup_class(self):
        self.api = RestfulBookerAPI()

    def test_get_token_success(self):
        payload = {"username": "admin", "password": "password123"}

        schema = {
            "type": "object",
            "properties": {"token": {"type": "string"}},
            "required": ["token"],
        }

        response = self.api.get_token(payload)

        assert (
            response.status_code == 200
        ), f"Expected status code 200, got {response.status_code}"

        response_json = response.json()
        validate(instance=response_json, schema=schema)
