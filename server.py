"""
Notification server to send the email to the user using the email server
"""


from flask import Flask, request, jsonify
from email_module import send_the_email

app = Flask(__name__)

@app.route("/")
def index():
    """
    Home page of the server to check if the server is running
    """
    
    return "Hello World"


@app.route("/email", methods=["POST"])
def email():
    """
    Receive the message and receiver from the user and 
    send the email to the receiver using the email server
    """
    
    if request.headers.get("Content-Type") == "application/json":
        data = request.json
    else:
        return jsonify({"status": "failed", "message": "Wrong data type"})

    if 'message' not in data and 'receiver' not in data:
        return jsonify({"status": "failed", "message": "Required fields are missing"})
    
    result = send_the_email(data["message"], data["receiver"])
    if result:
        return jsonify({"status": "success", "message": "Email sent successfully"})
    else:
        return jsonify({"status": "failed", "message": "Email sending failed"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)