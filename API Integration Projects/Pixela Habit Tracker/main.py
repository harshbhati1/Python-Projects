import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from a .env file
load_dotenv()

# Retrieve token and username from environment variables
TOKEN = os.getenv('TOKEN')
USERNAME = os.getenv('USERNAME')
GRAPH = "graph1"

# Endpoint for Pixela user operations
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Create a new user on Pixela
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.json())  # Output response to verify user creation

# Endpoint for creating and managing graphs
graph_endpoint = pixela_endpoint + f"/{USERNAME}/graphs"
graph_params = {
    "id": GRAPH,
    "name": "Learning Tracker",
    "unit": "Time",
    "type": "float",
    "color": "shibafu"
}
header = {
    "X-USER-TOKEN": TOKEN
}

# Create a new graph for tracking
graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=header)
print(graph_response.json())  # Output response to verify graph creation

# Endpoint for posting data to the graph
post_endpoint = graph_endpoint + f"/{GRAPH}"
post_param = {
    "date": datetime.now().strftime("%Y%m%d"),
    "quantity": "3.0"
}
post_response = requests.post(url=post_endpoint, json=post_param, headers=header)
print(post_response.json())  # Output response to verify data posting

# Update data in the graph
put_endpoint = post_endpoint + "/20240721"
put_param = {
    "quantity": "10"
}
response_put = requests.put(url=put_endpoint, json=put_param, headers=header)
print(response_put.json())  # Output response to verify data update

# Delete data from the graph
delete_endpoint = put_endpoint
delete_response = requests.delete(url=delete_endpoint, headers=header)
print(delete_response.json())  # Output response to verify data deletion
