import smtplib
from twilio.rest import Client

TWILIO_SID = "ACa821694e010fa77f1d812fc6e3ed8fda"
TWILIO_AUTH_TOKEN = "c9e86aad1acf4c6f26a17b93e2204f56"
TWILIO_VIRTUAL_NUMBER = '+19107254410'
TWILIO_VERIFIED_NUMBER = '+79255753835'
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "inda4894@gmail.com"
MY_PASSWORD = "pointer3"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )