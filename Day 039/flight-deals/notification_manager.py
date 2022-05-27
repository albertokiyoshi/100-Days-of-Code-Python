from twilio.rest import Client

ACCOUNT_SID = ""
AUTH_TOKEN = ""


class NotificationManager:
    def __init__(self):
        self.account_sid = ACCOUNT_SID
        self.auth_token = AUTH_TOKEN

    def send_message(self, flight_info):
        price = flight_info.price
        city_from = flight_info.city_from
        iata_from = flight_info.iata_from
        city_to = flight_info.city_to
        iata_to = flight_info.iata_to
        outbound = flight_info.outbound
        inbound = flight_info.inbound
        message_text = f"Low price alert! Only ${price} to fly from {city_from}-{iata_from} to " \
                       f"{city_to}-{iata_to}, from {outbound} to {inbound}."
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
                body=message_text,
                from_="",
                to="",
            )

        print(message.sid)
