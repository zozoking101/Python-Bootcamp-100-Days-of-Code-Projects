import requests
import os
import datetime

NUTRITIONIX_API = os.environ.get('NUTRITIONIX_API')
NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
HOST_DOMAIN = "https://trackapi.nutritionix.com"
ENDPOINT = "/v2/natural/exercise"

GENDER = input("Male or Female: ").lower()
WEIGHT = int(input("Your weight in kg: "))
HEIGHT = float(input("Your height in cm: "))
AGE = int(input("Your age in yrs: "))

# ENTER "QUIT" TO STOP
to_continue = True

while to_continue:
    query = input("Tell me which exercises you did: ").lower()
    if query == "quit":
        to_continue = False

    headers = {
        'x-app-id': NUTRITIONIX_APP_ID,
        'x-app-key': NUTRITIONIX_API,
    }

    params = {
        'query': query,
        'gender': GENDER,
        'weight_kg': WEIGHT,
        'height_cm': HEIGHT,
        'age': AGE,
    }

    url = f'{HOST_DOMAIN}{ENDPOINT}'
    exercise_response = requests.post(url=url, json=params, headers=headers)
    exercise_response.raise_for_status()
    data = exercise_response.json()
    print(data)

    SHEETY_USERNAME = "d2be2d1ccf6bd2fb7cf15d800e160d33"  # "zozoking101"
    SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
    SHEETY_AUTHORIZATION_HEADER = os.environ.get('SHEETY_AUTHORIZATION_HEADER')
    PROJECT_NAME = "zoesWorkouts"
    SHEET_NAME = "workout"

    sheety_header = {
        "Content-Type": "application/json",
        "Authorization": SHEETY_AUTHORIZATION_HEADER,
        "username": "zozoking101",
        "password": SHEETY_TOKEN,
    }

    auth = ("zozoking101", SHEETY_TOKEN)
    now = str(datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    now = now.split()

    sheety_endpoint = f'https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}/{SHEET_NAME}'

    for i in data['exercises']:
        sheety_params = {
            f'{SHEET_NAME}': {
                "date": now[0],
                "time": now[1],
                "exercise": i["name"].title(),
                "duration": i["duration_min"],
                "calories": i["nf_calories"],
            }
        }

        post_response = requests.post(url=sheety_endpoint, json=sheety_params, auth=auth)
        post_response.raise_for_status()
        print(post_response.text)
