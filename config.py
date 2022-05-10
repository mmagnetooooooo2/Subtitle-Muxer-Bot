
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    APP_ID = os.environ.get('APP_ID', None)
    API_HASH = os.environ.get('API_HASH', None)
    HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME', None)
    HEROKU_API_KEY = os.environ.get('HEROKU_API_KEY', None)
    

    #comma seperated user id of users who are allowed to use

    DOWNLOAD_DIR = 'downloads'
    OWNER_ID = int(os.environ.get("OWNER_ID", 1316963576))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)  
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", ""))
    # database session name, example: xurluploader
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    SEND_LOGS_WHEN_DYING = str(os.environ.get("SEND_LOGS_WHEN_DYING", "True")).lower() == 'true' 
