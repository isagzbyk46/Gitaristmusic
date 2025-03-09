from gitaristmusic.core.bot import TGN
from gitaristmusic.core.dir import dirr
from gitaristmusic.core.git import git
from gitaristmusic.core.userbot import Userbot
from gitaristmusic.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = TGN()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
