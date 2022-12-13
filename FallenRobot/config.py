import json
import os


def get_user_list(config, key):
    with open("{}/FallenRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    API_ID = "6435225"
    API_HASH = "4e984ea35f854762dcde906dce426c2d"
    TOKEN = "5744245230:AAFuipcdKfCHL5xyo0agw1BDO1JCdC2WQEQ"
    OWNER_ID = "1442684727"
    SUPPORT_CHAT = "tpxsupport404"
    JOIN_LOGGER = ("-1001585369050")
    EVENT_LOGS = ("-1001585369050")
    OWNER_USERNAME = "Ath2023"

    SQLALCHEMY_DATABASE_URI = "postgres://qgkukhqc:LhgZ-tfaJFFJjoD8lo5usFNZdvz-aSx0@heffalump.db.elephantsql.com/qgkukhqc"
    MONGO_DB_URI = "mongodb+srv://sasuke:sas@cluster0.rm3gpq8.mongodb.net/?retryWrites=true&w=majority"
    LOAD = []
    NO_LOAD = ["rss"]
    WEBHOOK = False
    INFOPIC = True
    URL = None

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")

    DONATION_LINK = ""
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = (
        "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE"
    )
    ALLOW_EXCL = True
    CASH_API_KEY = "NV34OEUX0YAFLUB6"
    TIME_API_KEY = "RTHI3DLW56HY"
    BL_CHATS = []
    SPAMMERS = None
    ALLOW_CHATS = True
    START_IMG = "https://telegra.ph/file/5488f5f7cbef38d2e81f7.jpg"
    HEROKU_API_KEY = None
    HEROKU_APP_NAME = None
    TEMP_DOWNLOAD_DIRECTORY = "./"
    ARQ_API_KEY = "LJMETG-DPHBCX-DGHJCD-TMFIGB-ARQ"
    ARQ_API_URL = "https://arq.hamker.in"
    ALLOW_EXCL = True
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
