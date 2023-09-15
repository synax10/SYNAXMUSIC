from aiohttp import ClientSession
from .console import LOGGER

from PrachiMusic.modules.core.app import App
from PrachiMusic.modules.core.bot import Bot
from PrachiMusic.modules.core.dirs import dirr
from PrachiMusic.modules.core.git import git
from PrachiMusic.misc import dbb, heroku, sudo

dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = App()

bot = Bot()


from PrachiMusic.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
