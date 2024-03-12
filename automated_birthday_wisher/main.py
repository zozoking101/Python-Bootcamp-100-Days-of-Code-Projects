import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = "myemail@gmail.com"
MY_PASSWORD = "********"

today = dt.datetime.now()
month = today.month
day = today.day
today_tuple = (month, day)


data = pd.read_csv("birthdays.csv")

birthdays_dict = {(j["month"], j["day"]): j for (i, j) in data.iterrows()}

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    letter = random.choice(letters)
    with open(f"./letter_templates/{letter}") as f:
        text = f.read()
        text = text.replace("[NAME]", birthday_person["name"])

    # with smtplib.SMTP(host="smtp.gmail.com", port=465) as connection:
    #     connection.starttls()
    #     connection.login(MY_EMAIL, 
    #                      birthday_person["email"], 
    #                      f"Subject: Happy Birthday {birthday_person["name"]}!\n\n{text}")


