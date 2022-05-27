import requests


class DataManager:
    def __init__(self):
        self.endpoint = ""
        self.sheet_data = None
        self.update_params = None

    def get_data(self):
        with requests.get(self.endpoint) as response:
            response.raise_for_status()
            self.sheet_data = response.json()
        return self.sheet_data["prices"]

    def update_data(self, object_id, key, value):
        self.update_params = {
            "price": {
                key: value,
            }
        }
        response = requests.put(self.endpoint + object_id, json=self.update_params)
        response.raise_for_status()