from twilio.rest import Client
import os
import smtplib

TWILIO_SID = os.environ.get("TWILIO_SID_TWO")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN_TWO")
TWILIO_VIRTUAL_NUMBER = os.environ.get("VIRTUAL_TWILIO_NUMBER")
TWILIO_VERIFIED_NUMBER = os.environ.get("MY_VERIFIED_NUMBER")

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.mail.yahoo.com"
MY_EMAIL = "MY EMAIL"
MY_PASSWORD = "MY PASSWORD"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.status)
        
    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
