from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "31cb00c1cbe580394778b43105864bca")
      API_ID = int(getenv("API_ID", "23031620"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7132554545:AAGbEIvcyLgAswB6CaqYNNULrRG06kl9vh0")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002036982984:-1002080964342").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
