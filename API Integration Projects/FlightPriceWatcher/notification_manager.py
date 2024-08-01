import os
import smtplib
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class NotificationManager:

    def __init__(self):
        # Initialize Twilio client and email connection
        self.client = Client(os.environ['TWILIO_SID'], os.environ["TWILIO_AUTH_TOKEN"])
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.connection = smtplib.SMTP("smtp.gmail.com", 587)

    def send_whatsapp(self, message_body):
        # Send a WhatsApp message using Twilio
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER1"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.sid)
    
    def send_emails(self, email_list, email_body):
        # Send an email to a list of recipients
        with self.connection:
            self.connection.starttls()  # Secure the connection
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8')
                )
