"""
Notification server to send the email to the user using the email server
"""


from os import environ

from flask import Flask, jsonify, request

from postmarkapp_client import send_the_email

app = Flask(__name__)

AUTH_TOKEN = environ.get("AUTH_TOKEN")

@app.get("/")
def index():
    """
    Home page of the server to check if the server is running
    """
    
    return "Hello World"


@app.post("/email")
def email():
    """
    Receive the message and receiver from the user and 
    send the email to the receiver using the email server
    """

    auth_header = request.headers.get("Authorization")

    if not auth_header:
        msg = {"status": "failure", "message": "No Authorization header found"}
        return jsonify(msg), 401
    
    __token = auth_header.split(" ")[1]

    if __token != AUTH_TOKEN:
        msg = {"status": "failure", "message": "Invalid token"}
        return jsonify(msg), 401
    
    data = request.get_json()
    print(data)

    if send_the_email(data["receiver"], data["subject"], data["message"]):
        return jsonify({"status": "success", "message": "Email sent successfully"}), 200
    else:
        return jsonify({"status": "failed", "message": "Email sending failed"}), 400

@app.post("/sms")
def sms():
    msg = {"status": "failure", "message": "Not implemented yet"}
    return jsonify(msg), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)