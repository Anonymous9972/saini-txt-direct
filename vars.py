#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26697299"))
API_HASH = environ.get("API_HASH", "7326c7f4d7d714d782a130c77b09009c")
BOT_TOKEN = environ.get("BOT_TOKEN", "7102594775:AAGgeyiUU-0rTwbCsknLhaGFkeChn06rLp4")

OWNER = int(environ.get("OWNER", "5168669934"))
CREDIT = environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")

TOTAL_USER = os.environ.get('TOTAL_USERS', '5168669934').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '5168669934').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

