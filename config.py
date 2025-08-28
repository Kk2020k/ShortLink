import os
from typing import List

API_ID = os.environ.get("API_ID", "26872474")
API_HASH = os.environ.get("API_HASH", "f8d3a289bf28a13a7159ad0b2ed114e7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

ADMIN = int(os.environ.get("ADMIN", ""))
PICS = (os.environ.get("PICS", "")).split()

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002057608700"))

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "")

IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1001590803749").split())) # Add Multiple channel ids
