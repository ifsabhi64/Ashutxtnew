#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20567114"))
API_HASH = environ.get("API_HASH", "8a5b92106e45fc6637a65a67df060a65")
BOT_TOKEN = environ.get("BOT_TOKEN", "7921161374:AAEn1Id1RMGuBoj7oxPduBcEdBTh-XFGDSg")

OWNER = int(environ.get("OWNER", "8036182138"))
CREDIT = environ.get("CREDIT", "**[༄ᶦᶰᵈआशु࿐❥◉🇮🇳™](https://t.me/IFSAshuAbhiBot)**")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8036182138').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8036182138').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

