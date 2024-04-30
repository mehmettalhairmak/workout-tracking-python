import datetime
import requests

NUTRITIONIX_API_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUTRITIONIX_APP_ID = "********"
NUTRITIONIX_APP_KEY = "********"

SHEETY_API_URL = "https://api.sheety.co/7ad1e5cd020ce5ce517941f8b69283f9/workoutTracking/workouts"

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY
}

nutritionix_body = {
    "query": input("Tell me which exercises you did: ".title())
}

nutritionix_response = requests.post(NUTRITIONIX_API_URL, headers=nutritionix_headers, json=nutritionix_body)
nutritionix_data = nutritionix_response.json()

exercises = nutritionix_data["exercises"]

current_date = datetime.datetime.now()
date = current_date.strftime("%d/%m/%Y")
time = current_date.strftime("%X")

sheety_header = {
    "Authorization": "********"
}

for exercise in exercises:
    sheety_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    requests.post(SHEETY_API_URL, headers=sheety_header, json=sheety_body)