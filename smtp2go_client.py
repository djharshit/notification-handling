"""
Module to send email using SMTP2GO email server API
API documentation: https://apidoc.smtp2go.com/documentation/
"""

from os import environ
import requests

url = "https://api.smtp2go.com/v3/email/send"
headers = {"Content-Type": "application/json"}


def send_the_email(reciever: list, subject: str, message: str) -> bool:
    """Function to send the email to the user using the email server

    Keyword arguments:
    receiver -- list of email addresses of the receiver
    subject -- subject of the email
    message -- message of the email
    Return: True if email sent successfully else False
    """

    json = {"api_key": environ.get("SMTP2GO_API_KEY"), "to": reciever, "sender": "Info <info@kese.dev>", "subject": subject, "text_body": message}

    response = requests.post(url=url, json=json, headers=headers)

    print(response.status_code)
    print(response.text)

    return response.status_code == 200


if __name__ == "__main__":
    send_the_email(["info@djharshit.dev"], "Test", "This is a test email")
