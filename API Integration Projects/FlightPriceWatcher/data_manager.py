import os  # For accessing environment variables
from dotenv import load_dotenv  # For loading environment variables from a .env file
import requests  # For making HTTP requests

load_dotenv()  # Load environment variables

class DataManager:
    
    def __init__(self):
        bearer_token = os.getenv('bearer_token_Sheety')  # Retrieve Sheety API token
        self.header = {
            "Authorization": f"Bearer {bearer_token}"  # Set authorization header for API requests
        }
        
    def get_data(self):
        get_endpoint = os.getenv('get_endpoint_Sheety')  # Endpoint to get data from Sheety
        response = requests.get(get_endpoint, headers=self.header)  # Make GET request
        response.raise_for_status()  # Raise error for unsuccessful request
        sheet_data = response.json()["prices"]  # Extract data from response
        return sheet_data  # Return data
    
    def put_data(self, data, id):
        put_endpoint = f"{os.getenv('put_endpoint_Sheety')}/{id}"  # Construct PUT request URL
        response = requests.put(put_endpoint, headers=self.header, json=data)  # Make PUT request
        if response.status_code == 200:
            print(f"worked")  # Print success message
        else:
            print(f"failed")  # Print failure message
    
    def get_customer_emails(self):
        response = requests.get(url=os.getenv('get_endpoint_User'), headers=self.header)  # GET request to retrieve customer emails
        data = response.json()  # Parse JSON response
        self.customer_data = data["users"]  # Extract customer data
        return self.customer_data  # Return customer data
