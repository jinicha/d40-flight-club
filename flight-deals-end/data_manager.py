from pprint import pprint
import requests
import config

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/1535b87ed86e1f83ec9c3d5640e64173/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/1535b87ed86e1f83ec9c3d5640e64173/flightDeals/users"

headers = {
    "Authorization": f'Bearer {config.TOKEN}'
}


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.user_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT,
            headers=headers
        )
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)

    def get_user_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        data = response.json()
        self.user_data = data["users"]
        return self.user_data
