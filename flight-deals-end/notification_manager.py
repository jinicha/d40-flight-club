from twilio.rest import Client
from smtplib import SMTP
import config

TWILIO_SID = config.ACCOUNT_SID
TWILIO_AUTH_TOKEN = config.AUTH_TOKEN
TWILIO_VIRTUAL_NUMBER = config.SEND_FROM
TWILIO_VERIFIED_NUMBER = config.SEND_TO
EMAIL_SENDER = config.EMAIL_SENDER
EMAIL_PW = config.EMAIL_PW


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
        print('Message sent!')

    def send_emails(self, emails, message, book_link):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL_SENDER, password=EMAIL_PW)
            for email in emails:
                connection.sendmail(
                    from_addr=EMAIL_SENDER,
                    to_addrs=email,
                    msg=f'Subject: New Low Price Flight!\n\n{message}\n\n{book_link}'
                )
                print('Email sent!')
