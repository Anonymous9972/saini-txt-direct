#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26697299"))
API_HASH = environ.get("API_HASH", "7326c7f4d7d714d782a130c77b09009c")
BOT_TOKEN = environ.get("BOT_TOKEN", "8178994593:AAFVDrUmrmJOnoo3Z8JQHU6IPz1xKFeOvPY")
OWNER = int(environ.get("OWNER", "5168669934"))
CREDIT = "ᗩᑎOᑎYᗰOᑌՏ"
AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
