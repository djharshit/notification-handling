import requests
from os import environ

url = "https://api.postmarkapp.com/email"
API_KEY = environ.get("POSTMARKAPP_API_KEY")

headers = {"Accept": "application/json", "Content-Type": "application/json", "X-Postmark-Server-Token": API_KEY}


def send_the_email(recipient, subject, message):
    json = {
        "From": "hello@djcicd.co",
        "To": recipient,
        "Subject": subject,
        "TextBody": message,
    }

    response = requests.post(url=url, headers=headers, json=json)

    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        return True
    else:
        return False


if __name__ == "__main__":
    send_the_email("hm0092374@gmail.com", "Test", "This is a test email")
