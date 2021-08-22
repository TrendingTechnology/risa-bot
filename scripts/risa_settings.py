
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
EMOJI_NEXT_PAGE_10 = '⏭️'
EMOJI_BACK_PAGE_10 = '⏮️'
EMOJI_DOWNLOAD = '💾'

RISA_THUMB_URL = "https://camo.githubusercontent.com/4e77178220f9ca7124b09d9407d786a5e905ecf609f9ee5f45c786f3cf713144/68747470733a2f2f692e6962622e636f2f4a6e6b5668304c2f31382d63726f707065642e6a7067"
ICON_URL = "https://cdn.discordapp.com/attachments/466964106692395008/580378765419347968/icon_nhentai.png"
LOAD_GIF_URL = "https://c.tenor.com/p3XgH1GgXoUAAAAd/shy-anime.gif"
NO_RESULT_GIF_URL = "https://c.tenor.com/cZAW8f5L1O0AAAAd/sad-anime.gif"
TOP_EMBED_TEXT = 'nHentai reader'
EMBED_DELETE_TIMER = 10800
SHORT_MSG_DELETE_TIMER = 8

BANNED_TAG_MSG = "Sorry, I cannot let you show a doujin that contains a banned tag."
NOT_EXIST_MSG = "Doujin doesn't exist!"
LOAD_MSG = "Searching..."
NO_RESULT_MSG = "Nothing found!"
# Owner
GITHUB_LINK = "https://github.com/arkhon7"
GITHUB_README_LINK = "https://github.com/arkhon7/risa-bot#risa"
SOURCE_CODE = "https://github.com/arkhon7/risa-bot.git"
GMAIL = 'https://mail.google.com/mail/u/0/?fs=1&to=reviuy9@gmail.com&tf=cm'


# aliases
JP_LANG = ['jp']
CH_LANG = ['cn']
EN_LANG = ['en']

# nh
BANNED_TAGS = ['loli', 'shota', 'furry']


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
	EMOJI_BACK_PAGE_10,
	EMOJI_BACK_PAGE_ALT,
	EMOJI_NEXT_PAGE_ALT,
	EMOJI_NEXT_PAGE_10,
	EMOJI_WASTEBASKET
]

