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
COOKIE = environ.get("COOKIE", "csrfToken=tTs9B8Ca_Srj1DVzRPXqhGwi; browserid=WfWOtiyA4OBW2sUnBIx8oCDqVJyRmNLXsVCCWuCc9U6PbCjUG4WKXOD7Zls=; lang=en; TSID=3EiWs6jUeJZ7xw9bvsAbbdasP0m7UEt4; __bid_n=18bce1e49fadca6fe94207; _ga=GA1.1.759117559.1712506087; ndus=YQ0hgexteHuixPDQ6pnSqo3f-lHx_yj6NJvHP3WH; ndut_fmt=C3C70E50C42E04ADAD688A56413483A414AA1ADAABB8936BA1156E80B5C35092; _ga_06ZNKL8C2E=GS1.1.1712905616.2.1.1712907169.60.0.0;")
