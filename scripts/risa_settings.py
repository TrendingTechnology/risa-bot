
import json
import os
from discord import Activity, ActivityType

def get_token(file_dir):
        with open(file_dir, 'r+') as js:
            data = json.load(js)
            return data['token']

# token
TOKEN_FILE_DIR = 'config/config.json'
TOKEN = os.environ.get('BOT_TOKEN') if os.environ.get('BOT_TOKEN') else get_token(TOKEN_FILE_DIR)

# bot
PREFIX = '!'
BOT_STATUS = Activity(type=ActivityType.listening, name=f"{PREFIX}risa")
EMOJI_BOOK = '📖'
EMOJI_BOOK_GET = '📘'
EMOJI_WASTEBASKET = '🗑️'
EMOJI_FIRST_PAGE = '⏪'
EMOJI_LAST_PAGE = '⏩'
EMOJI_NEXT_PAGE = '➡️'
EMOJI_BACK_PAGE = '⬅️'
EMOJI_RANDOM = '🔄'
EMOJI_NEXT_PAGE_ALT = '▶'
EMOJI_BACK_PAGE_ALT = '◀'
EMOJI_DOWNLOAD = '💾'

ICON_URL = "https://cdn.discordapp.com/attachments/466964106692395008/580378765419347968/icon_nhentai.png"
TOP_EMBED_TEXT = 'nHentai reader'
EMBED_DELETE_TIMER = 10800
SHORT_MSG_DELETE_TIMER = 8


# aliases
JP_LANG = ['jp']
CH_LANG = ['cn']
EN_LANG = ['en']

# nh
BANNED_TAGS = ['lolicon', 'shotacon']


INTRO_MESSAGE_EMOJIS = [
	EMOJI_BOOK,
	EMOJI_DOWNLOAD,
	EMOJI_WASTEBASKET
]

READ_MESSAGE_EMOJIS = [
	EMOJI_FIRST_PAGE,
	EMOJI_BACK_PAGE,
	EMOJI_NEXT_PAGE,
	EMOJI_LAST_PAGE,
	EMOJI_WASTEBASKET
]

PAGINATED_MESSAGE_EMOJIS = [
	EMOJI_BOOK_GET,
	EMOJI_BACK_PAGE_ALT,
	EMOJI_NEXT_PAGE_ALT,
	EMOJI_WASTEBASKET
]

