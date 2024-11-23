import requests


class RestfulBookerAPI:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def get_token(self, payload):
        url = f"{self.BASE_URL}/auth"
        response = requests.post(url, json=payload)
        return response

    def create_booking(self, payload):
        url = f"{self.BASE_URL}/booking"
        response = requests.post(url, json=payload)
        return response

    def delete_booking(self, booking_number):
        url = f"{self.BASE_URL}/booking/{booking_number}"
        response = requests.delete(url)
        return response
