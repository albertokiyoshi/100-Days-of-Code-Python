import requests
import datetime as dt

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_header = {
    "x-app-id": "",
    "x-app-key": "",
}

nutritionix_params = {
    "query": input("Tell me what exercises you did: "),
    "gender": "male",
    "weight_kg": ,
    "height_cm": ,
    "age": 
}

with requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_header) as response:
    response.raise_for_status()
    nutritionix_data = response.json()

today = dt.datetime.now()
time = today.time()

sheety_endpoint = ""

for exercise in nutritionix_data["exercises"]:
    sheety_params = {
        "workout": {
            "date": today.strftime("%x"),
            "time": time.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(sheety_endpoint, json=sheety_params)
    response.raise_for_status()
    print(response.text)
