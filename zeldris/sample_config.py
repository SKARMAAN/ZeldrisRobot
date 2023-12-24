# ZeldrisRobot
# Copyright (C) 2017-2019, Paul Larsen
# Copyright (C) 2022, IDNCoderX Team, <https://github.com/IDN-C-X/ZeldrisRobot>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


if not __name__.endswith("sample_config"):
    import sys

    print(
        "The README is there to be read. Extend this sample config to a config file, don't just rename and change "
        "values here. Doing that WILL backfire on you.\nBot quitting.",
        file=sys.stderr,
    )
    sys.exit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    TOKEN = "6536934928:AAGz2-ARFY6CkU8MD1kcWccbu7TWAV9TZLw"  # Take from @BotFather
    OWNER_ID = (
        "5332414680"  # If you dont know, run the bot and do /id in your private chat with it
    )
    OWNER_USERNAME = "@Armaan512"
    API_HASH = "06baef4020832888ccf3ebf4e746d52b"  # for purge stuffs
    API_ID = "29098103"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://kvbtopvx:rn5dFC0Q9FYOrf9koHbpEaPu9HFuA4cz@cornelius.db.elephantsql.com/kvbtopvx"  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    REDIS_URL = "redis://default:ctYvtErg2kYzBWkfq1YnJsfh6NrSY76X@redis-19332.c299.asia-northeast1-1.gce.cloud.redislabs.com:19332"  # needed for afk module, get from redislab
    LOAD = []
    NO_LOAD = []
    WEBHOOK = False
    URL = None
    MONGO_URI = "mongodb+srv://godgamer9434:0ilJ0eM4yi5Z5hmd@cluster0.yx21dk8.mongodb.net/?retryWrites=true&w=majority"
    MONGO_PORT = 27017  # leave it as it is
    MONGO_DB = "godgamer9434"

    # OPTIONAL
    DEV_USERS = (
        []
    )  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = (
        []
    )  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = (
        []
    )  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    WHITELIST_CHATS = []
    BLACKLIST_CHATS = []
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = None  # banhammer marie sticker
    ALLOW_EXCL = False  # DEPRECATED, USE BELOW INSTEAD! Allow ! commands as well as /
    CUSTOM_CMD = False  # Set to ('/', '!') or whatever to enable it, like ALLOW_EXCL but with more custom handler!
    API_OPENWEATHER = None  # OpenWeather API
    SPAMWATCH_API = None  # Your SpamWatch token
    WALL_API = None
    SPAMMERS = None


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
