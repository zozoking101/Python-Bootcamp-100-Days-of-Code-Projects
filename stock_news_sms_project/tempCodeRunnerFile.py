# data = r.json()["Time Series (Daily)"]
# data_list = [j for (i, j) in data.items()]
# days = [i for (i, j) in data.items()]
# yesterday_data = data_list[0]
# yesterday_closing_price = float(yesterday_data["4. close"])
# print(yesterday_closing_price)

# day_before_yesterday_data = data_list[1]
# day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

# up_down = None
# difference = yesterday_closing_price - day_before_yesterday_closing_price

# if difference > 0:
#     up_down = "🔺"
# else:
#     up_down = "🔻"
# percentage_difference = round(difference / day_before_yesterday_closing_price * 100)

# if abs(percentage_difference) > 1:
#     news_parameters = {
#         'qInTitle': COMPANY_NAME,
#         'from': days[10-1],
#         'sortBy': 'popularity',
#         'apiKey': NEWS_API_KEY,
#     }
#     news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
#     news_response.raise_for_status()
#     news_data = news_response.json()["articles"]

#     articles = news_data[:3]
#     print(articles)

#     # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
#     article_list = [f'{STOCK_NAME}: {up_down}{percentage_difference}% \nHeadline: {article["title"]}. '\
#                     f'\nBrief: {article["description"]}' for article in articles]

#     for _ in article_list:
#         # send_article(_)
#         print(_)
