import pandas as pd
import datetime as dt
import smtplib
from random import randint

user_email = "example@example.com"
user_password = "example"
today = dt.datetime.now()

birthdays = pd.read_csv("birthdays.csv")

for index, row in birthdays.iterrows():
    if row.month == today.month and row.day == today.day:
        name = row["name"]
        email = row.email
        file_path = f"letter_templates/letter_{randint(1, 3)}.txt"
        with open(file_path) as letter_file:
            letter = letter_file.read().replace("[NAME]", name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=user_email, password=user_password)
            connection.sendmail(
                from_addr=user_email,
                to_addrs=email,
                msg=f"Subject:Happy Birthday!\n\n{letter}"
            )
