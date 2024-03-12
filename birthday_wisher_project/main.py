import smtplib
import datetime as dt
import random


MY_EMAIL = "email@outlook.com"
RECIPIENT = "zoe.oladokun@gmail.com"
CONNECTION = smtplib.SMTP("smtp.mail.outlook.com", port=587)


def send_email(message):
    with CONNECTION as connection:
        connection.starttls()
        with open("password.txt") as file:
            password = file.read()
        connection.login(user=MY_EMAIL, password=password)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT, msg=message)


# now = dt.datetime.now()
# year = now.year
# month = now.month
# week = now.weekday()
# hour = now.hour
# second = now.second
# microsecond = now.microsecond
#
# date_of_birth = dt.datetime(year=2004, month=7, day=6)
# print(date_of_birth.weekday())


def main():
    while True:
        day = dt.datetime.now()
        if day.weekday() == 0:
            with open("quotes.txt") as f:
                quotes = f.readlines()
                quote = random.choice(quotes)
                quote = f"Subject: Monday Motivation\n\n{quote}"
                send_email(quote)
                quotes.remove(quote)


if __name__ == "__main__":
    main()
