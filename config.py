import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
URL_APPLES = os.getenv("URL_APPLES")
URL_PEAR = os.getenv("URL_PEAR")


print(BOT_TOKEN)