# (c) @AM_ROBOTS

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
π€ My Name: <a href='https://t.me/nvslinkbot'>Lin Search Bot</a>

π Language : <a href='https://www.python.org'> Python V3</a>

π Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

π‘ Server: <a href='koyeb.com'>Koyeb</a>

π¨βπ» Created By: <a href='https://t.me/tgnvs'>TGNVS</a></b>
"""

    ABOUT_HELP_TEXT = """<b>Donation</b>
<b>Thanks for showing interest in donation
Donate Us To Keep Alive
Continously Alive

You Can Send Any Amount
Donate Only One Rupee
Of 10βΉ,20βΉ,30βΉ,50βΉ,100βΉ π

πΈPayment Methods:
Only UPI
UPI:-</b> tgnvs@airtel
-<b> <a href=https://upier.vercel.app/pay/tgnvs@airtel?am=15>Donation Link</a></b>
"""

    HOME_TEXT = """
<b>Hey! {}π,

I'm Link Search Bot.π€</a>

I Can Search π What You Wantβ

<a>Made With β€ By @tgnvs</a></b>
"""


    START_MSG = """
<b>Hey! {}π,

I'm Link Search Bot.π€</a>

I Can Search π What You Wantβ

<a>Made With β€ By @tgnvs</a></b>
"""

