import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 29164256
API_HASH = "92d6f00caf64ce989b390f288e755456"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8344467234:AAGsbncQzXtaTAdZHrfQAJXtX2y8GfaDFz4"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://ajaymaurya89812:ajaymaurya89812@cluster0.2nzf4xv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002736060889

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7294760523

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/KCD_KOREAN_DRAMA"
SUPPORT_GROUP = "https://t.me/+j3XemNA9I4NiODc1"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQG9AuAAIYjX49wSt20dppTlRJcH2pIskiheWRaoCQtIzQcc3ecXpuWz-nREkpg6qkwFrpWf6EwKvu-F7dH2Tz1NjhGP1JTrRTLtsl4UF_cv4cj6BhO8aJhaIcaixLDZAxridkvQ4bkenLNpgTFrbX3q9F7eRxMmPablBZzX1PkMeNKdh_FycLix5quWS8EYArYm_b6MIqFUVt24JsySdOZA-gkFO2OJKbl-DS5NqmW5LHJyuiiSsW47g8F7hv4b3gvnTEJTZ18KbDXHjY3Ad0O9sntNmlNkTn6ukhFQwVXgM8gfZAAFPQ-XylIry8jQPUeX1D0U7b5xjTqekdcEyKts3IDkGgAAAAGyzTZLAA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"

PING_IMG_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"
STATS_IMG_URL = "https://graph.org/file/f586172fe40a0b5d0b0df.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"
STREAM_IMG_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/c76afa6fc87c3819dce6b-d2e7f57ae2d58fc2f2.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )

