from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", "28167530")  # api id
API_HASH = environ.get("API_HASH", "202a9e8b13b7663417ddacc671420ad9")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "7051688091:AAGVzaPqoaNDDZOc2V5Jo2CD9UnHuzTsA3U")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "redis-13976.c239.us-east-1-2.ec2.cloud.redislabs.com")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", "13976")  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "J3RaGqWkhOaE7wRQ49xvBTvZ3EZzHZAr"
)  # redis password


ADMINS = [6440245883,5015968435]
OWNER_ID = 6440245883  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002021142183  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1001160455229
DUMP_CHANNEL = -1001160455229


# Config
COOKIE = environ.get("COOKIE", "csrfToken=Nj_j3_HMv8poQHVganXv1ZBU; browserid=fLzlNHEVZEORHUNzW6e5MCc7lqF__8NLlyTlSUhcY6mZRGceM9ko8B80KjI; lang=en; TSID=PYZuS6QWzjaWVjC13VQb5wybFLsn3cRl; __bid_n=18f772965e3f3512b24207; _ga=GA1.1.759117559.1712506087; ndus=YV4153yteHuicc9ZPmzRJr82Lo_Q2_Vac_ILJdaj; ndut_fmt=9EDE39D2FD9E5A59EABB6CCC766D368426A54F6824A887F880175CFCCF28BA83; _ga_06ZNKL8C2E=GS1.1.1712905616.2.1.1712907169.60.0.0;")
