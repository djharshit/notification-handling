from math import e
import requests
from os import environ

# API documentation: https://apidoc.smtp2go.com/documentation/

API_KEY = environ.get("SENDGRID_API_KEY")

url = "https://api.sendgrid.com/v3/mail/send"

headers = {"Content-Type": "application/json", "Authorization": "Bearer " + API_KEY}


def send_the_email(recipient, subject, message):
    json = {
        "personalizations": [{"to": [{"email": recipient}]}],
        "from": {"email": "email@harshitm.tv", "name": "Harshit Email"},
        "subject": subject,
        "content": [{"type": "text/plain", "value": message}],
    }

    response = requests.post(url=url, json=json, headers=headers)

    print(response.status_code)
    print(response.text)

    if response.status_code == 202:
        return True
    else:
        return False


if __name__ == "__main__":
    send_the_email("hm0092374@gmail.com", "Test", "This is a test email")
