import requests
import smtplib
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Retrieve latitude and longitude from environment variables
MY_LAT = float(os.getenv('MY_LAT'))  # Your latitude
MY_LONG = float(os.getenv('MY_LONG'))  # Your longitude

def iss_overhead():
    """
    Check if the ISS is currently overhead within a 5-degree range of the given latitude and longitude.
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    # Check if the ISS position is within the 5-degree range of the user's location
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False

def is_night():
    """
    Check if the current time is during the night based on sunrise and sunset times for the given location.
    """
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # Check if the current time is before sunrise or after sunset
    if time_now > sunset or time_now < sunrise:
        return True
    return False

# Main execution: Check if the ISS is overhead and it is currently night
if iss_overhead() and is_night():
    # Retrieve email credentials from environment variables
    myGmail = os.getenv('myGmail')
    password = os.getenv('password')

    # Set up the SMTP connection
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=myGmail, password=password)

    # Send an email notification
    connection.sendmail(
        from_addr=myGmail,
        to_addrs=os.getenv('to_addrs'),
        msg="Subject: ISS is overhead \n\n Hey, look for the ISS overhead. It has arrived in your area."
    )
    connection.close()
