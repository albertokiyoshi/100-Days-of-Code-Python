import requests
from datetime import datetime
import smtplib
import time

user_email = "example@example.com"
user_password = "example"


USER_LAT = 
USER_LONG = 


def compare_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if USER_LAT - 5 < iss_latitude < USER_LAT + 5 and USER_LONG - 5 < iss_longitude < USER_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": USER_LAT,
        "lng": USER_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if compare_position() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=user_email, password=user_password)
            connection.sendmail(
                from_addr=user_email,
                to_addrs="example@example.com",
                msg="Subject:Look up!\n\nThe ISS is above in the sky."
            )
