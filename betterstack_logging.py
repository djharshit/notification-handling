from logtail import LogtailHandler
import logging
from os import environ

SOURCE_TOKEN = environ.get("BETTERSTACK_SOURCE_TOKEN")

handler = LogtailHandler(source_token=SOURCE_TOKEN)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)