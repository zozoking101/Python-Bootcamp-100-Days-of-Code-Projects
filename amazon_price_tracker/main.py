import smtplib, ssl
import os
import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.co.uk/Roxenda-Speed-Cube-Profession-3x3x3/dp/B07FMVFQS8/" \
      "ref=sr_1_7?dib=eyJ2IjoiMSJ9.UzlpqFZrNuouC8IFt75X7L3rf5GvqurrM30hqGaAtwxw-" \
      "OIvP6UCHgH36ToT3vVl_1gPrl9alCI5M9f0X-DB2xlJjSDNq30ntynJXuBW-YwyTlvpuRdJv_momhfxNFQSqgg6TaLDpzD9rUsj7_" \
      "GFSYiR58dJNka59THzLfusIXjG0nbuuv_V5JL-gRfgYp_" \
      "CWzQEJT7YjlEvalyZFwjBLlRGfG2D0f1rBZ7G7NKRETmGaeORHv27Ig2etr3DTPjh7BHIzAOib8SFYykQtMrNhJQM5icLAlL919FFrO1xUng." \
      "8rUcpB1wdFwNTmFVqnaVI5qR3IWnbaE9RiUjkIcke-4&dib_tag=se&keywords=rubik%27s+cube&qid=1712232152&sr=8-7"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US;q=0.9"
}

response = requests.get(url, headers=header)
# with open("response.txt", mode="w", encoding="utf-8") as f:
#     f.write(response.text)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

title = soup.select("#titleSection")[0].get_text().strip()
# print(title)

price = soup.select("#style_name_1_price .a-size-mini")[0].get_text().strip()
price_without_currency = price.split("£")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

BUY_PRICE = 5.60

if price_as_float < BUY_PRICE:
    smptp_server = "smtp.office365.com"
    sender = os.environ.get("MY_EMAIL")
    receivers = [os.environ.get("RECEPIENT_EMAIL")] 
    for receiver in receivers:
        message = f"""
        From: {sender}
        To: {receiver}
        Subject: Rubik's cube price drop.
        
        Alert 🔔: {title} is now £{price_as_float}.
        """
        context = ssl.create_default_context()
        with smtplib.SMTP(smptp_server, 587) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender, "********")
            server.sendmail(sender, receivers, message.encode('utf-8'))
            print('Email sent successfully.')
