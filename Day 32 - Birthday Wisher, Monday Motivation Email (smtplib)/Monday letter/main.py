import smtplib
import datetime as dt
import random

MY_EMAIL = "inda4894@gmail.com"
MY_PASSWORD = "***"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        random_quote = random.choice(all_quotes)
        print(random_quote)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_PASSWORD,
        to_addrs="v.saburov@yahoo.com",
        msg=f"Subject:Monday Motivation\n\n{random_quote}"
    )