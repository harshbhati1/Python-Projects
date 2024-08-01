import requests  # For making HTTP requests
import os  # For accessing environment variables
from dotenv import load_dotenv  # For loading environment variables from a .env file
from pprint import *  # For pretty-printing (unused)
from datetime import datetime  # For working with dates

load_dotenv()  # Load environment variables

class FlightSearch:
    def __init__(self):
        self.API_KEY_FLIGHT = os.getenv('API_KEY_Amadeus')  # Get API key from environment variables
        self.API_SECRET_FLIGHT = os.getenv('API_SECRET_Amadeus')  # Get API secret from environment variables
        self.acces_token = self.access_token()  # Retrieve access token
        self.headers = {
            'Authorization': f'Bearer {self.acces_token}'  # Set authorization header
        }
        
    def access_token(self):
        token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"  # Endpoint to get access token
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'  # Content type for token request
        }
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.API_KEY_FLIGHT,
            'client_secret': self.API_SECRET_FLIGHT
        }
        response = requests.post(url=token_endpoint, headers=headers, data=data)  # Request access token
        if response.status_code == 200:
            return response.json()['access_token']  # Return access token if successful
        else:
            print(f"Failed to obtain token: {response.status_code} - {response.text}")  # Print error if token request fails
            return None
    
    def fetch_iata_code(self, city_name):
        endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"  # Endpoint to fetch IATA code
        params = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=endpoint, headers=self.headers, params=params)  # Request IATA code
        if response.status_code == 200:
            data = response.json()
            if 'data' in data and len(data['data']) > 0:
                return data['data'][0]['iataCode']  # Return IATA code if found
            else:
                print(f"No IATA code found for {city_name}")  # Print message if no IATA code found
                return "TESTING"  # Return placeholder if no code found
        else:
            print(f"Failed to fetch IATA code: {response.status_code} - {response.text}")  # Print error if IATA code request fails
            return None
        
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        param = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": 10
        }
        FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"  # Endpoint to check flights
        response = requests.get(FLIGHT_ENDPOINT, headers=self.headers, params=param)  # Request flight offers
        response.raise_for_status()  # Raise error for unsuccessful request
        return response.json()  # Return flight offers data
