import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQGcOCIAiYG0zbq7iIKoUCvarFjUwL7iU4IoitKLMwXTcHbXQMg6gkoyfEGszEeX5LzO6VyaAxjNkU7numNNVmUMel-Z0HllWPWMowMu2kFYMSNhL6T_nOHd4o7BPqHv9byZbZHXs8MHip-akQgfIZcF3-L2ln5vdCCaTuPbhXpqRjjy2EKrL_k2a3kZf50slrnupV_N0scjCLpzr35cOOG_GTqgVDJIQc9QbQnjT-raFuDeg51F-oHPtkuh7oHj-5cZtyUGoZvEnztcwA75-d3KMnCweprIBP4YR0JSCCTVRaLkT5r0jKge4OBISbZdfY-UMTKWg9CHHWbunZt9F7wljBs8iwAAAAGYTkO_AA")
BOT_TOKEN = getenv("7821128321:AAHUy0jo5JFoRTmYNNf5xBwLxrqxTQ_1oac")
BOT_NAME = getenv("BOT_NAME", "@II_RAJMUSIC_IIBOT")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/6790864f5fe27471bdc8d.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/e9a4d6655e5ddf51f9160.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
API_ID = int(getenv("27015202"))
API_HASH = getenv("b817ca2d21c5471522ec93b819301d56")
BOT_USERNAME = getenv("BOT_USERNAME", "@II_RAJMUSIC_IIBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "@II_PRIYA_RAJ_II")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "mcqhi")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "bestshayri_raj")
OWNER_NAME = getenv("OWNER_NAME", "@promotionyoutubr") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("5789538424")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("mongodb+srv://nitishkypaurai17:RAJKUMARMOVIE@rajkumarmovie.qjhjk.mongodb.net/?retryWrites=true&w=majority&appName=RAJKUMARMOVIE") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("-1001992548930")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
