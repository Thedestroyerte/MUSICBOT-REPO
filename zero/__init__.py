from Zero.core.bot import ZeroBot
from Zero.core.dir import dirr
from Zero.core.git import git
from Zero.core.userbot import Userbot
from Zero.misc import dbb, heroku

from .logging import LOGGER

git()


dirr()

dbb()

heroku()

# Clients
app = ZeroBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
