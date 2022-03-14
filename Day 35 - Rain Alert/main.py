import requests
from twilio.rest import Client

api_key = "7bd19285a60a012dbc25c78f4b5399d2"
account_sid = "ACa821694e010fa77f1d812fc6e3ed8fda"
auth_token = "c9e86aad1acf4c6f26a17b93e2204f56"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_LATITUDE = 55.897550
MY_LONGITUDE = 38.137507

weather_params = {
    "lat":MY_LATITUDE,
    "lon":MY_LONGITUDE,
    "appid":api_key,
    "exclude":"current,minutely,daily",
}

response = requests.get(url=OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for i in range(0, 12):
    condition_code = (weather_slice[i]["weather"][0]["id"])
    if condition_code > 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's not going to rain! Don't worry.",
        from_='+19107254410',
        to='+79255753835'
    )
    print(message.status)
