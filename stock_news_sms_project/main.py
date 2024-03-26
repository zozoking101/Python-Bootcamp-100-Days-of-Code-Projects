import os
import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.environ.get('AV_API_KEY')
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
ACCOUNT_SID = os.environ.get("TWILIO_SID_TWO")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN_TWO")
VIRTUAL_TWILIO_NUMBER = os.environ.get("VIRTUAL_TWILIO_NUMBER")
VERIFIED_NUMBER = os.environ.get("MY_VERIFIED_NUMBER")


stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY,
}

r = requests.get(STOCK_ENDPOINT, params=stock_parameters)
r.raise_for_status()
data = r.json()["Time Series (Daily)"]
data_list = [j for (i, j) in data.items()]

days = [i for (i, j) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

up_down = None
difference = yesterday_closing_price - day_before_yesterday_closing_price

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
percentage_difference = round(difference / day_before_yesterday_closing_price * 100)

if abs(percentage_difference) >= 1:
    news_parameters = {
        'qInTitle': COMPANY_NAME,
        # 'from': days[10-1],
        'sortBy': 'popularity',
        'apiKey': NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]

    articles = news_data[:3]


    # Create a new list of the first 3 articles headline and description using list comprehension.
    article_list = [f'{STOCK_NAME}: {up_down} {percentage_difference}% \nHeadline: {article["title"]}. '\
                    f'\nBrief: {article["description"]}' for article in articles]
    print(article_list)
    
    # Send each article as a separate message via Twilio.
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    for _ in article_list:
        
        message = client.messages \
            .create(
                body=_,
                from_=VIRTUAL_TWILIO_NUMBER,
                to=VERIFIED_NUMBER
            )
        print(message.status)
