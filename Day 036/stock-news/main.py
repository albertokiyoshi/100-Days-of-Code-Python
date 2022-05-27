import requests
import pandas as pd
from twilio.rest import Client

STOCK = "AMZN"
STOCK_API_KEY = ""
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

COMPANY_NAME = "Amazon"
NEWS_API_KEY = ""
NEWS_ENDPOINT = "https://newsapi.org/v2/top-headlines"

account_sid = "" # SID from Twilio
auth_token = "" # Authentication Token from Twilio

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

with requests.get(STOCK_ENDPOINT, stock_parameters) as response:
    response.raise_for_status()
    data = response.json()
    stock_data = pd.DataFrame(data["Time Series (Daily)"]).transpose()

price_yesterday = float(stock_data.iloc[2]["4. close"])
price_day_before_yesterday = float(stock_data.iloc[3]["4. close"])

price_variation = ((price_yesterday / price_day_before_yesterday) - 1) * 100

if price_variation >= 3 or price_variation <= -3:

    with requests.get(NEWS_ENDPOINT, params=news_parameters) as response:
        response.raise_for_status()
        data = response.json()
        news_data = data["articles"]

    for article in news_data[:3]:
        headline = article["title"]
        brief = article["description"]

        if price_variation >= 3:
            percentage_variation = f"🔺{round(abs(price_variation))}%"
        else:
            percentage_variation = f"🔻{round(abs(price_variation))}%"

        message_text = f"{STOCK}: {percentage_variation}\nHeadline: {headline}\nBrief: {brief}"
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
                body=message_text,
                from_="", # Source phone number (from Twilio)
                to="", # Destination phone number
            )

        print(message.sid)
