import requests
from datetime import datetime
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

# constant
USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
PIXELA_ENDPOINT ="https://pixe.la/v1/users"




# create user account
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)



# create a graph definition
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config ={
    "id": "graph1",
    "name": "codingTracker",
    "unit": "commit",
    "type": "int",
    "color": "ajisai"

}

headers = {"X-USER-TOKEN": TOKEN}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# post value to the graph
habit_record = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
today = datetime.now()
habit_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "2",

}
response = requests.post(url=habit_record, json=habit_params, headers=headers)
print(response.text)


# update graph
graph_changes = {
    "unit": "km"
}

response = requests.put(url=habit_record, json=graph_changes, headers=headers)
print(response.text)
