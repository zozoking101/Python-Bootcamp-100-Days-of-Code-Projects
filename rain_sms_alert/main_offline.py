import requests
import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient


OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ.get("OWM_API_KEY_1")

account_sid = os.environ.get("TWILIO_SID_TWO")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN_TWO")

weather_parameters = {
    "lat": 29.622930,
    "lon": -95.343920,
    # "exclude": "current,minutely,daily",
    "appid": api_key,   
}

response = requests.get(OWN_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

will_rain = False

condition_code = int(weather_data["weather"][0]["id"])
if int(condition_code) < 700:
    will_rain = True

if will_rain:
    print("Bring an umbrella. ☔")
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    # client = Client(account_sid, auth_token) # http_client=proxy_client)
    
    # message = client.messages \
    #     .create(
    #         body="It's going to rain today. Remember to bring an umbrella. ☔",
    #         from_='+16502854781',
    #         to='+2347066572225'
    # )
    # print(message.status)
else:
    print("No rain today.")