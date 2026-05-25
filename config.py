import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

BOT_NAME = "HMB Support AI"
CREATOR = "Le Roy HMB"

ORANGE_MONEY = "692274053"
MTN_MOMO = "651388771"
