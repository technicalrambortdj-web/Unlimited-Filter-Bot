import os
import pyrogram

import nntplib
import time

# Sync time tolerance offset
from pyrogram.session import session
session.Session.MAX_TIME_DIFF = 86400


if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config



if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "filter bot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300
    )
    Config.AUTH_USERS.add(str(680815375))
    app.run()
