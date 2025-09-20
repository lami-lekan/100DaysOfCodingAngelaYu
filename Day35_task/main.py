import requests
import os
from twilio.rest import Client

account_sid = "ACe9cf84d86e2a895102854c20600a98cc"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

API_KEY = os.environ.get("OWM_API_KEY")
LAT = 48.956558
LONG = -54.608440
print(API_KEY)

parameters = {
    "lat": LAT,
    "lon": LONG,
    "cnt": 4,
    "appid": API_KEY

}

open_weather = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)

open_weather.raise_for_status()
weather_report = open_weather.json()
# print(weather_report)
# print(weather_report["list"][0]["weather"][0]["id"])

for weather in range(len(weather_report["list"])):
    condition_code = weather_report["list"][weather]["weather"][0]["id"]
    if condition_code < 700:
        message = client.messages.create(
            body="Bring an umbrella, it's going to rain!",
            from_= "+17083406612",
            to="+17092199211"
        )
        print(message.status)