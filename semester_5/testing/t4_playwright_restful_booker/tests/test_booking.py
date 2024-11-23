from jsonschema import validate

from api_client import RestfulBookerAPI


class TestCreateBooking:
    def setup_class(self):
        self.api = RestfulBookerAPI()

    def test_create_booking_success(self):
        payload = {
            "firstname": "John",
            "lastname": "Doe",
            "totalprice": 123,
            "depositpaid": True,
            "bookingdates": {"checkin": "2024-01-01", "checkout": "2024-01-10"},
            "additionalneeds": "Breakfast",
        }

        schema = {
            "type": "object",
            "properties": {
                "bookingid": {"type": "integer"},
                "booking": {
                    "type": "object",
                    "properties": {
                        "firstname": {"type": "string"},
                        "lastname": {"type": "string"},
                        "totalprice": {"type": "integer"},
                        "depositpaid": {"type": "boolean"},
                        "bookingdates": {
                            "type": "object",
                            "properties": {
                                "checkin": {"type": "string"},
                                "checkout": {"type": "string"},
                            },
                            "required": ["checkin", "checkout"],
                        },
                        "additionalneeds": {"type": "string"},
                    },
                    "required": [
                        "firstname",
                        "lastname",
                        "totalprice",
                        "depositpaid",
                        "bookingdates",
                        "additionalneeds",
                    ],
                },
            },
            "required": ["bookingid", "booking"],
        }

        response = self.api.create_booking(payload)

        assert (
            response.status_code == 200
        ), f"Expected status code 200, got {response.status_code}"

        response_json = response.json()
        validate(instance=response_json, schema=schema)
