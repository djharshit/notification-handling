from os import environ
import requests

# API documentation: https://apidoc.smtp2go.com/documentation/

API_KEY = environ.get("SMTP2GO_API_KEY")

url = "https://api.smtp2go.com/v3/email/send"

headers = {"Content-Type": "application/json"}


def send_the_email(recipient, subject, message):
    json = {"api_key": API_KEY, "to": [recipient], "sender": "Info <info@djcicd.co>", "subject": subject, "text_body": message}

    response = requests.post(url=url, json=json, headers=headers)

    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        return True
    else:
        return False

if __name__ == "__main__":
    send_the_email("hm0092374@gmail.com", "Test", "This is a test email")
