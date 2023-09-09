"""
Module to send email using Elasticemail email server API
"""

from os import environ

import requests

# API documentation: https://elasticemail.com/developers/api-documentation/rest-api

API_KEY = environ.get("ELASTICEMAIL_API_KEY")

url = "https://api.elasticemail.com/v4/emails/transactional"

headers = {"Content-Type": "application/json", "X-ElasticEmail-ApiKey": API_KEY}


def send_the_email(receiver: list, subject: str, message: str) -> bool:
    """Function to send the email to the user using the email server

    Keyword arguments:
    receiver -- list of email addresses of the receiver
    subject -- subject of the email
    message -- message of the email
    Return: True if email sent successfully else False
    """

    json = {
        "Recipients": {"To": receiver}, 
        "Content": {
            "Body": [{"ContentType": "PlainText"}],
        }
    }

    response = requests.post(url=url, headers=headers, json=json)

    print(response.status_code)
    print(response.text)


send_the_email("hm0092374@gmail.com", "Test", "This is a test email")
