import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

query = input("Enter what you did in gym today? ")

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')

NaturalLanguageForExerciseEndPoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": query
}

response = requests.post(url=NaturalLanguageForExerciseEndPoint, json=parameters, headers=header)
response.raise_for_status()
data = response.json()["exercises"]


# shitty


# Updated Sheety API endpoint
post_url = "https://api.sheety.co/bf181a770f8f8bab0b3cdf589b963ad2/projectWorkout/workouts"
MYTOKEN = os.getenv('MYTOKEN')
header1 = {
    "Authorization": f"Bearer {MYTOKEN}"
}

# Data to be posted
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")
for entry in data:
    duration_minutes = round(entry["duration_min"])  # Round the duration to the nearest minute
    duration_formatted = f"{duration_minutes:02d}min"
    data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": entry["user_input"].title(),
            "duration": duration_formatted,
            "calories": entry["nf_calories"]
        }
    }
    post_response = requests.post(url=post_url, json=data, headers= header1)
    print(f"POST Status Code: {post_response.status_code}")
    print("POST Response Content:", post_response.json())

