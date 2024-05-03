from os import getenv


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
