import os

API_ID    = os.environ.get("API_ID", "26513107")
API_HASH  = os.environ.get("API_HASH", "f14ce4b58dc8812cfc9665588472f2d4")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
