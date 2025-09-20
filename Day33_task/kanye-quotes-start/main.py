import requests
from datetime import datetime
from smtplib import SMTP
import time

MY_LAT = 48.956558
MY_LNG = -54.608440
MY_EMAIL = "olagbajuisrael11@gmail.com"
MY_PASSWORD = "gbgibtshgudhnpsm"

# compares user location with ISS
def is_iss_near():
    response_iss =requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_data = response_iss.json()
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if (MY_LNG - 5 <= iss_longitude <= MY_LNG + 5) and (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5):
        return True

# checks if its dark outside
def is_sunset():
    parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0
    }
    response_ss = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response_ss.raise_for_status()
    ss_data = response_ss.json()

    sunrise = ss_data["results"]["sunrise"]
    sunset = ss_data["results"]["sunset"]

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    current_datetime = datetime.now()

    current_time = current_datetime.time()
    current_hour = current_time.hour
    if current_hour >= sunset_hour and current_hour <= sunrise_hour:
        return True

# sends mail noticfication
while True:
    time.sleep(60)
    if is_iss_near() and is_sunset():
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject: ISS Above You \n\n GO outside now, if you want to see the ISS moving.")





# from tkinter import *
# import requests
# import random

# def get_quote():
#     # pass
#     kanye_quote = requests.get("https://api.kanye.rest/")
#     kanye_quote.raise_for_status()
#     quote_kanye = (kanye_quote.json()["quote"])
#     canvas.itemconfig(quote_text, text=quote_kanye)


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)

# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)

# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)



# window.mainloop()