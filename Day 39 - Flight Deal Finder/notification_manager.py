from twilio.rest import Client

TWILIO_SID = "ACa821694e010fa77f1d812fc6e3ed8fda"
TWILIO_AUTH_TOKEN = "c9e86aad1acf4c6f26a17b93e2204f56"
TWILIO_VIRTUAL_NUMBER = '+19107254410'
TWILIO_VERIFIED_NUMBER = '+79255753835'


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
        print(message.sid)
