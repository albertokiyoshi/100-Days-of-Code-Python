import requests
from datetime import datetime

USERNAME = "" # Pixe username
TOKEN = "" # Pixe token
GRAPH_ID = "" # Pixe graph ID

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

day = datetime(year=2022, month=5, day=2).strftime("%Y%m%d")

pixel_config = {
    "date": day,
    "quantity": "6.01",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_update_endpoint = f"{pixel_creation_endpoint}/{day}"

pixel_put_config = {
    "quantity": "6.01"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_put_config, headers=headers)
# print(response.text)

response = requests.delete(url=pixel_update_endpoint, headers=headers)

