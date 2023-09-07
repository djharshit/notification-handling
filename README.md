# Notification Server

## Description
This is a simple notification server that can be used to send notifications to an email. It is intended to be used with the TA-Automation app, but can be used for other purposes as well.

## Installation
```bash
docker pull djharshit/notification-server
docker run -d -p 5000:5000 djharshit/notification-server
```

## Usage
```python
import requests

requests.post('http://localhost:5000/email', json={
    'to': 'sender-email',
    'subject': 'subject',
    'message': 'message'}
)
```

### Source
[Dockerhub](https://hub.docker.com/r/djharshit/notification-server)  
[GitHub](https://github.com/djharshit/notification-server)