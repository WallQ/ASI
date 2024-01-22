import os
import smtplib
import ssl

from dotenv import load_dotenv

load_dotenv()


def send_email():
    smtp_server = "smtp-mail.outlook.com"
    port = 587

    email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(email, password)
        server.sendmail(email, email, "Hello, World!")
