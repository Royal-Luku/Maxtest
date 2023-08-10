import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "22501624"))
    API_HASH = os.environ.get("API_HASH", "5181e32c508753a0fdf347d6d3a0478c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6684062044:AAFO01ts83KQ_qUR8WiBoGklqPTFOmShsoM")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MaxxBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQFXWPgAArE2p8vlzS9lkkAih-5wR1A7EWDh_F3J5fG22d7h7dB04Ii5-M8My39-X-dhQI3J7EWAxae_xyufvu86m-NeMVIiFM0T49lvW13p64l9KKM5SZpSdh9onwBK95GYm-afdhCKeKMQ_axyBfbMSqfLAT1gQUIQa9TpqbJL80KA-aQPBJbc2j2kQcAyOAitnYdCnl9yeryWSy0jJzJRI9HLS6pwHg_OvqzFYNn76wpvFRVuGBF76YhGErE6Q3r_JqMzefgIYxuF-imtOBbMxTaymY0Iv3IvNvlZbqDtoSNfpZ6BV91QPdIEWxtOtIEaucFOifAAr5-x0nDfhJg_Kqn7PwAAAAByEI8cAA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001980021513"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Maxx_beta_version_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "1913687836"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://RoyalTelegram:RoyalTelegram@cluster0.ixfndqo.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://youtube.com/@GreyMattersBot'>Link Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @GreyMatter_Bots</a></b>
"""

