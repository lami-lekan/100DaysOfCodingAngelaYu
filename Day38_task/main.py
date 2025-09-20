import requests

APP_ID = "ad2a4664"
API_KEY = "fba0f4cb898a4389494c1cf10c08441a"

HOST_DOMAIN = "https://trackapi.nutritionix.com"
nutrient_endpoint = "/v2/natural/nutrients"
excercise_endpoint = "/v2/natural/exercise"

sheety_url = "https://api.sheety.co/izzy/myWorkouts/workouts"
sheety_header = {
    "Authorization": "Basic aXp6eTpPbGFnYmFqdQ=="
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

excercise ={
    "query": f"{input('Tell me which excercise you did: ')}"
}
nutritionix = requests.post(url=f"{HOST_DOMAIN}{excercise_endpoint}", headers=headers, json=excercise)
print(nutritionix.text)

sheety_data = requests.get(url=sheety_url, headers=sheety_header)

print(sheety_data.text)
