import requests
import time

t = time.localtime()
today_date = time.strftime("%Y%m%d", t)

USERNAME = "izzylekan"
TOKEN = "jagkjlhsfhdgiuhndfjnk"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config ={
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Day",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config = {
    "date": today_date,
    "quantity": "1"
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)