#Отслеживаем цену на конкретный товар по ссылке с Амазона.
#Если цена ниже целевой, отправляем об этом уведомление на почту.

import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

MY_EMAIL = "inda4894@gmail.com"
MY_PASSWORD = "pointer3"

TARGET_PRICE = 110.0

AMAZON_URL = "https://www.amazon.com/Instant-Pot-Plus-Programmable-Sterilizer/dp/B075CWJ3T8/ref=dp_prsubs_2?pd_rd_i=B075CWJ3T8&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6",
}

response = requests.get(AMAZON_URL, headers=headers)
website = response.content

soup = BeautifulSoup(website, "lxml")

price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
product = soup.find(name="span", id="productTitle").getText().strip()

message = f"{product} is now ${price}".encode("utf-8")
print(message)

if price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="v.saburov@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{AMAZON_URL}"
        )
