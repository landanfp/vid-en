
import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5088657122:AAGByZ5PLpv205PaXhxDEZ_JixPIn1OaVnk")
    API_ID = int(os.environ.get("API_ID", "3335796"))
    APP_HASH = os.environ.get("APP_HASH","138b992a0e672e8346d8439c3f42ea78")
    SESSION_NAME = os.environ.get("SESSION_NAME", "VIDEO-EN")
    OWNER_ID = int(os.environ.get("OWNER_ID", "763990585")
    SUDO_USERS = os.environ.get("SUDO_USERS","")
    MONGO_DB = os.environ.get("MONGO_DB", "mongodb+srv://abirhasan2005:abirhasan@cluster0.i6qzp.mongodb.net/cluster0?retryWrites=true&w=majority")
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL, "-1001792962793")
     = os.environ.get(", "")                             
