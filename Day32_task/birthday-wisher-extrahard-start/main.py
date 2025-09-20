##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import smtplib as smtp
import random

my_email = "olagbajuisrael11@gmail.com"
my_password = "gbgibtshgudhnpsm"
birthday_csv = pd.read_csv("birthdays.csv")
birthday_dict = birthday_csv.to_dict()
saved_day = birthday_dict["day"]


today = dt.datetime.now()
today_date = (today.day, today.month, today.year)

for index, day in saved_day.items():
    if day == today_date[0]:
        with open("letter_templates/letter_1.txt") as letter_1,\
        open("letter_templates/letter_2.txt") as letter_2, \
        open("letter_templates/letter_3.txt") as letter_3:
            celebrant_email = birthday_dict["email"][index]
            name = birthday_dict["name"][index]
            letter_to_send = (random.choice([letter_1, letter_2, letter_3])).read()
        modified_letter = letter_to_send.replace("[NAME]", name)
        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs=celebrant_email, msg=f"Subject:Happy Birthday {name}!!!\n\n{modified_letter}")