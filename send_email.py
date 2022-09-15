from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv
load_dotenv()

import os

sender_email = input("Enter Sender Gmail: ")
receiver_email = input("Enter Receiver Email: ")

# the app password generated from gmail
password = os.environ.get("MY_PASSWORD")
subject = input("Subject of Mail: ")
body = input("Write your message here: ")

em = EmailMessage()
em["From"] = receiver_email
em["To"] = sender_email
em["subject"] = subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as connection:
    connection.login(sender_email, password)
    connection.sendmail(sender_email, receiver_email, em.as_string())
