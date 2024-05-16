from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", "28167530")  # api id
API_HASH = environ.get("API_HASH", "202a9e8b13b7663417ddacc671420ad9")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "6785693620:AAGeHHcw12M5qijCaTbEGV-Sge9gwdcrQwM")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "redis-19981.c15.us-east-1-2.ec2.redns.redis-cloud.com")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", "19981")  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "mHppSlUdGQYXEnwmAgzaAgSoYcQQdIZl"
)  # redis password


ADMINS = [6440245883,5015968435]
OWNER_ID = 6440245883  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002021142183  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1001160455229
DUMP_CHANNEL = -1001160455229


# Config
COOKIE = environ.get("COOKIE", "csrfToken=tjtoLdkesqHiQZBC2SkONUKN; browserid=GAps1pg85rN5g0YDvglcd6ZQEFeMo7TokCR5YsaDjaiSflPKj2D53f74xsE; lang=en; TSID=Up5C4cTtOkGuj8B16MY6ZquXbTQF8daH; __bid_n=18f812ac399371f4ee4207; _ga=GA1.1.1015758587.1715859015; ndus=YyRNt3yteHuiHmmvokhUU2y2UwrQDsqpSSB408g5; ndut_fmt=EB796D5D7F63DCD33930CF62A48A9586BB94E070872510B1992D1F95E511B627; _ga_06ZNKL8C2E=GS1.1.1715859014.1.1.1715860025.44.0.0")
