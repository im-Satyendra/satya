import os

class Config(object):
    TG_BOT_TOKEN = "5217702275:AAH0KwikoXAzjEc7qO8V9XiH1-gnTAVnFF4"
    APP_ID = 2171111
    API_HASH = "fd7acd07303760c52dcc0ed8b2f73086"
    AUTH_USERS = 1089528685
    OWNER_ID = 1089528685
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 3600
    DEF_WATER_MARK_FILE = ""
    DB = "mongodb+srv://satya:s4tya@cluster0.rrqhs.mongodb.net/utyfky?retryWrites=true&w=majority"
    CHAT_ID = -1001724430366
    LOG_CHANNEL = -1001753919095
