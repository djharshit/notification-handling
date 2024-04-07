"""
Module to send email using Sendgrid email server API
API documentation: https://apidoc.smtp2go.com/documentation/
"""

from os import environ

import requests

url = "https://api.sendgrid.com/v3/mail/send"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {environ.get("SENDGRID_API_KEY")}",
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
        "personalizations": [{"to": []}],
        "from": {"email": "info@kese.dev", "name": "Info"},
        "subject": subject,
        "content": [{"type": "text/plain", "value": message}],
    }

    for i in receiver:
        json["personalizations"][0]["to"].append({"email": i})

    response = requests.post(url=url, json=json, headers=headers)

    print(response.status_code)
    print(response.text)

    return response.status_code == 202


if __name__ == "__main__":
    send_the_email(["info@djharshit.dev"], "Test", "This is a test email")
