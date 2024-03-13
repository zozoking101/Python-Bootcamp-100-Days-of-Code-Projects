import requests
import datetime as dt
import smtplib
import time

SUNSET_URL = 'http://api.sunrise-sunset.org/json'
ISS_URL = 'http://api.open-notify.org/iss-now.json'
MY_LAT = 6.412850
MY_LONG = 4.087600
MY_EMAIL = "zoe.oladokun@gmail.com"
MY_PASSWORD = "********"


def iss_within_range():
    response_1 = requests.get(url=ISS_URL)
    response_1.raise_for_status()

    data_1 = response_1.json()
    iss_lat = float(data_1["iss_position"]["latitude"])
    iss_lng = float(data_1["iss_position"]["longitude"])

    # parameters = {
    #     "lat": MY_LAT,
    #     "lng": MY_LONG,
    # }

    return abs(iss_lat - MY_LAT) < 5 and abs(iss_lng - MY_LONG) < 5


def is_nighttime():
    formatted = 0
    sample_request = f"{SUNSET_URL}?lat={MY_LAT}&lng={MY_LONG}&formatted={formatted}"

    response_2 = requests.get(url=sample_request)
    response_2.raise_for_status()

    data_2 = response_2.json()

    sunrise = int(data_2["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_2["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now()
    hour_now = time_now.hour
    return hour_now < sunrise or hour_now >= sunset


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendemail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up 👆\n\nThe ISS is above you in the sky."
        )
while True:
    time.sleep(60*60)
    if is_nighttime() and iss_within_range():
        print("Look up!")
    else:
        print(f"ISS too far!.")
        
    print(is_nighttime())