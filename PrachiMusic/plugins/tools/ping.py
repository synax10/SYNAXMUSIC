from datetime import datetime
from pyrogram import filters
from pyrogram.types import Message

from PrachiMusic.utilities.config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from PrachiMusic.utilities.strings import get_command
from PrachiMusic import bot
from PrachiMusic.modules.core.call import Kaal
from PrachiMusic.modules.utils.sys import bot_sys_stats
from PrachiMusic.modules.main.decorators.language import language
from PrachiMusic.utilities.inline.play import close_keyboard

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@bot.on_message(
    filters.command(PING_COMMAND)
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Kaal.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ),
        reply_markup=close_keyboard
    )
