import requests
import os


def customer_acquisition():
    SHEETY_USERS_ENDPOINT = "https://api.sheety.co/d2be2d1ccf6bd2fb7cf15d800e160d33/flightDeals/users"
    SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')
    
    to_continue = True
    while to_continue:
        FIRST_NAME = input("What is your first name? ")
        if FIRST_NAME.lower() == 'quit' or '':
            return
        LAST_NAME = input("What is your last name? ")
        if LAST_NAME.lower() == 'quit' or '':
            return
        EMAIL = input("What is your email? ")
        if EMAIL.lower() == 'quit' or '':
            return
        EMAIL_2 = input("Type your email again. ")
        if EMAIL_2.lower() == 'quit' or '':
            return
        if EMAIL != EMAIL_2:
            print("Error: Emails are not the same.")
            customer_acquisition()
        
        body = {
            "users": {
                'firstName': FIRST_NAME,
                'lastName': LAST_NAME,
                'email': EMAIL
            }

        }
        
        response = requests.post(url=SHEETY_USERS_ENDPOINT, json=body)  # auth=("zozoking101", SHEETY_TOKEN)
        if response.status_code == "200":
            print("You're in the club!")
        else:
            print(response.text)
