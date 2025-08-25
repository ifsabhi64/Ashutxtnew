#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "25109542"))
API_HASH = environ.get("API_HASH", "3e1c35da0a6264d3a08d89763de2c809")
BOT_TOKEN = environ.get("BOT_TOKEN", "8327472832:AAHKLVW2ZU0gD3hgl-3guZ4Lg7ilH8DiDeE")

OWNER = int(environ.get("OWNER", ""))
CREDIT = environ.get("CREDIT", "**[༄ᶦᶰᵈआशु࿐❥◉🇮🇳™](https://t.me/IFSAshuAbhiBot)**")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8051613732').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8036182138,8051613732').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set



