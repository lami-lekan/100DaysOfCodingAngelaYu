# import smtplib

# my_email = "olagbajuisrael11@gmail.com"
# my_password = "gbgibtshgudhnpsm"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=my_password)
#     connection.sendmail(from_addr=my_email, to_addrs="olalekan.olagbaju@yahoo.com", msg="Subject:Hello!\n\nHow're you doing?")

# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# weekday = now.weekday()

# date_of_birth = dt.datetime(year=1997, month=11, day=26)
# print(date_of_birth)

import pandas as pd
import datetime as dt
import smtplib as smtp
import random

with open(file="quotes.txt") as quotes:
    all_quotes = quotes.readlines()
    message=random.choice(all_quotes)

my_email = "olagbajuisrael11@gmail.com"
my_password = "gbgibtshgudhnpsm"
days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day_otw = dt.datetime.now().weekday()


if day_otw < 6:
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=(my_email, "olalekan.olagbaju@yahoo.com"), msg=f"Subject:{days_list[day_otw]} Motivation\n\n{message}")
