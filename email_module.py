import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ

from dotenv import find_dotenv, load_dotenv

if find_dotenv():
    load_dotenv()

EMAIL_SERVER = environ.get("EMAIL_SERVER")
EMAIL_PORT = int(environ.get("EMAIL_PORT"))
EMAIL_USERNAME = environ.get("EMAIL_USERNAME")
EMAIL_PASSWORD = environ.get("EMAIL_PASSWORD")

ssl_context = ssl.create_default_context()


def send_the_email(msg: str, receiver: str) -> bool:
    """
    Send the message to the receiver using the email server
    """

    try:
        with smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT) as smtp_client:
            smtp_client.starttls(context=ssl_context)
            smtp_client.login("apikey", EMAIL_PASSWORD)

            message = MIMEMultipart()
            message["Subject"] = "User Submit Form"
            message["From"] = EMAIL_USERNAME
            message["To"] = receiver
            msg = MIMEText(msg, "plain")
            message.attach(msg)

            smtp_client.sendmail(EMAIL_USERNAME, receiver, message.as_string())

        print("[+] Email sent successfully")
        return True

    except smtplib.SMTPException as e:
        print("[+] The error occurred", e)
        return False
