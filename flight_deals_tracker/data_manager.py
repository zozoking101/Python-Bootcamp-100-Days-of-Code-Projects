import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/d2be2d1ccf6bd2fb7cf15d800e160d33/flightDeals/price'
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/d2be2d1ccf6bd2fb7cf15d800e160d33/flightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = None

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        print(data)
        self.destination_data = data["price"]
        # Printing the data out using pprint() to see it formatted.
        pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes.
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
            
    def get_customer_emails(self):
        customers_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
