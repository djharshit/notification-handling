"""
Module to send email using Postmarkapp email server API
"""

from os import environ

import requests

# API documentation: https://postmarkapp.com/developer/api/email-api

API_KEY = environ.get("POSTMARKAPP_API_KEY")

url = "https://api.postmarkapp.com/email"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-Postmark-Server-Token": API_KEY,
}


def send_the_email(receiver: list, subject: str, message: str) -> bool:
    """Function to send the email to the user using the email server

    Keyword arguments:
    receiver -- list of email addresses of the receiver
    subject -- subject of the email
    message -- message of the email
    Return: True if email sent successfully else False
    """

    json = {
        "From": "info@djcicd.co",
        "To": ", ".join(receiver),
        "Subject": subject,
        "TextBody": message,
    }

    response = requests.post(url=url, headers=headers, json=json)

    print(response.status_code)
    print(response.text)

    return response.status_code == 200


if __name__ == "__main__":
    send_the_email("hm0092374@gmail.com", "Test", "This is a test email")
