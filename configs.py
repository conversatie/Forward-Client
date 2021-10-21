# (c) @AbirHasan2005

import os
import heroku3


class Config(object):
    # Get This From @TeleORG_Bot
    API_ID = int(os.environ.get("API_ID", "6667465"))
    API_HASH = os.environ.get("API_HASH", "b3dcf78a9d2988aa4532139f50dd0e68")
    # Get This From @StringSessionGen_Bot
    STRING_SESSION = os.environ.get("STRING_SESSION", "BACdYvwjPp1LNXjlOV2nZStxrzZkbx3HfqxM4y-stGrrQbNUuqyHRrQjNSc0BFwiSCcl7X4AVUCZ5ZRTcStTIhtp4zg6Z9S_f4TgzAs835TsYFR_-3wULWQ8SSkIs5xrwKCI5HY3isYP2187tuGNWH1gXR6UDZ5HN3I_mE1qmp6JFtAS0HkptD_E3eNcXD4o9UYxUFxwxk7aaH205BMVdd7Xlg3oHDDtFrMKXSG8H5eQKMjqn3BG7j74P5eDRoPQMnm2rT1g1jy9kcUM3qpalBadROLqjZ5y9MjlZ5iasFhXIg9qhtjFnbNQi1amUiiN5XhErFW60ic_xAS1qTdRF7GdR-blRAA")
    # Forward From Chat ID
    FORWARD_FROM_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_FROM_CHAT_ID", "-1001006935927").split()))
    # Forward To Chat ID
    FORWARD_TO_CHAT_ID = list(set(int(x) for x in os.environ.get("FORWARD_TO_CHAT_ID", "-1001515924882").split()))
    # Filters for Forwards
    DEFAULT_FILTERS = "video document photo audio text gif forwarded poll sticker"
    FORWARD_FILTERS = list(set(x for x in os.environ.get("FORWARD_FILTERS", DEFAULT_FILTERS).split()))
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", "").split()))
    MINIMUM_FILE_SIZE = os.environ.get("MINIMUM_FILE_SIZE", None)
    BLOCK_FILES_WITHOUT_EXTENSIONS = bool(os.environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", False))
    # Forward as Copy. Value Should be True or False
    FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
    # Sleep Time while Kang
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 10))
    # Heroku Management
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY")
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    HEROKU_APP = heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME] if HEROKU_API_KEY and HEROKU_APP_NAME else None
    # Message Texts
    HELP_TEXT = """
This UserBot can forward messages from any Chat to any other Chat also you can kang all messages from one Chat to another Chat.

👨🏻‍💻 **Commands:**
• `!start` - Check UserBot Alive or Not.
• `!help` - Get this Message.
• `!kang` - Start All Messages Kanger.
• `!restart` - Restart Heroku App Dyno Workers.
• `!stop` - Stop Kanger & Restart Service.

©️ **Developer:** @AbirHasan2005
👥 **Support Group:** [【★ʟя★】](https://t.me/JoinOT)"""
