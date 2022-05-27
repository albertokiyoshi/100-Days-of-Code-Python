import requests
from twilio.rest import Client
import os

# Needs to add the environment variable on system
API_KEY = os.getenv("OWM_API_KEY")

account_sid = "" # SID from Twilio
# Needs to add the environment variable on system
auth_token = os.getenv("AUTH_TOKEN") # Authentication Token from Twilio

parameters = {
    "lat": -27.594870,
    "lon": -48.548222,
    "exclude": "current,minutely,daily",
    "appid": API_KEY,
}

print(API_KEY)
print(auth_token)

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

for hour_weather in weather_data["hourly"][:12]:
    weather_id = hour_weather["weather"][0]["id"]
    if weather_id < 700:
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body="It's going to rain today. Remember to bring an umbrella.",
                from_="", # Source phone number (from Twilio)
                to="", # Destination phone number
                    )
        print(message.status)
        break
