import requests
import datetime as dt

API_KEY = ""


class FlightSearch:
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com"
        self.today = dt.datetime.now()
        self.six_months_date = self.today + dt.timedelta(days=180)
        self.from_location = "SAO"
        self.header = {
            "apikey": API_KEY,
        }
        self.flights_data = None

    def get_iata(self, city):
        iata_params = {
            "term": city,
            "location_types": "city",
        }
        with requests.get(self.endpoint + "/locations/query", params=iata_params, headers=self.header) as response:
            response.raise_for_status()
            self.flights_data = response.json()
        return self.flights_data

    def get_flight_info(self, city_iata_code):
        price_params = {
            "fly_from": self.from_location,
            "fly_to": city_iata_code,
            "date_from": self.today.strftime("%d/%m/%Y"),
            "date_to": self.six_months_date.strftime("%d/%m/%Y"),
            "curr": "GBP",
        }
        with requests.get(self.endpoint + "/search", params=price_params, headers=self.header) as response:
            response.raise_for_status()
            flight_price_data = response.json()
            return flight_price_data
