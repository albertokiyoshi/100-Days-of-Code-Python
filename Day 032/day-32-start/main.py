import smtplib
import datetime as dt
from random import choice

with open("quotes.txt", "r+") as data:
    quotes_list = data.readlines()

user_email = "example@example.com"
user_password = "example"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    quote = choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=user_email, password=user_password)
        connection.sendmail(
                                from_addr=user_email,
                                to_addrs="example@example.com",
                                msg=f"Subject:Motivational Quote\n\n{quote}"
                            )
