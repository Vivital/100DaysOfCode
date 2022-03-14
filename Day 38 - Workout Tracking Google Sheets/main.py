import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 81
HEIGHT_CM = 183
AGE = 30

# USERNAME = "vivitalik"
# PASSWORD = "***"

APP_ID = "c30af3d4"
API_KEY = "63444ef60eb357a924419c68b9c2a747"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/ba447aee2a02384a1ccc74c31ce72347/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}

parameters = {
     "query":exercise_text,
     "gender":GENDER,
     "weight_kg":WEIGHT_KG,
     "height_cm":HEIGHT_CM,
     "age":AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
print(now_time)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
    "Authorization": "Bearer fgewhgoewhgohto32hto32hto32"
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)