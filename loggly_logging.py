import logging
import socket
from logging.handlers import SysLogHandler
import os

HOST_ADDRESS = os.environ.get("HOST_ADDRESS")
HOST_PORT = int(os.environ.get("HOST_PORT"))

class ContextFilter(logging.Filter):
    hostname = socket.gethostname()

    def filter(self, record):
        record.hostname = ContextFilter.hostname
        return True


syslog = SysLogHandler(address=(HOST_ADDRESS, HOST_PORT))
syslog.addFilter(ContextFilter())
app_name = os.path.basename(os.getcwd())
format = "{asctime} | {hostname} | {filename} | {funcName} | {lineno} | {message}"

formatter = logging.Formatter(format, style="{")
syslog.setFormatter(formatter)
logger = logging.getLogger()
logger.addHandler(syslog)
logger.setLevel(logging.INFO)

logger.info(f"{app_name} started")
