import requests
from twilio.rest import Client
import os 
from dotenv import load_dotenv


load_dotenv()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')



parameters = {
    "lat": os.getenv('lat'),
    "lon": os.getenv('lon'),
    "cnt": os.getenv('cnt'),
    "appid": os.getenv('appid')
}
OWEendpoint = os.getenv('OWEendpoint')
response = requests.get(OWEendpoint, params=parameters)
response.raise_for_status()
data = response.json()

actualData = [point["weather"][0]["id"] for point in data["list"] if point["weather"][0]["id"] < 700]

if len(actualData) > 0:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=f"whatsapp:{os.getenv('number')}",
        body="Bro bring your umbrella! There'll be rain today",
        to=f"whatsapp:{os.getenv('number1')}"
    )
    print(f"Message SID: {message.sid}")
    print(f"Message Status: {message.status}")
else:
    print("No weather conditions met the criteria.")

print(f"Weather Data: {actualData}")
