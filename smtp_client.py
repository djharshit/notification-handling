import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ

EMAIL_SERVER = environ.get("EMAIL_SERVER")
EMAIL_PORT = int(environ.get("EMAIL_PORT"))
EMAIL_USERNAME = environ.get("EMAIL_USERNAME")
EMAIL_PASSWORD = environ.get("EMAIL_PASSWORD")

ssl_context = ssl.create_default_context()


def send_the_email(receiver, subject, message) -> bool:
    """
    Send the message to the receiver using the email server
    """

    try:
        with smtplib.SMTP(EMAIL_SERVER, EMAIL_PORT) as smtp_client:
            smtp_client.starttls(context=ssl_context)
            smtp_client.login("apikey", EMAIL_PASSWORD)

            msg = MIMEMultipart()
            msg["Subject"] = subject
            msg["From"] = EMAIL_USERNAME
            msg["To"] = receiver
            msg = MIMEText(message, "plain")
            msg.attach(message)

            smtp_client.sendmail(EMAIL_USERNAME, receiver, msg.as_string())

        print("SMTP email sent")
        return True

    except smtplib.SMTPException as e:
        print("SMTP email error", e)
        return False
