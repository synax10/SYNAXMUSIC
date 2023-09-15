from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, Message

from PrachiMusic.utilities.config import BANNED_USERS
from PrachiMusic.utilities.strings import get_command
from PrachiMusic import bot
from PrachiMusic.modules.main.database import (get_playmode, get_playtype,
                                       is_nonadmin_chat)
from PrachiMusic.modules.main.decorators import language
from PrachiMusic.utilities.inline.settings import playmode_users_markup

### Commands
PLAYMODE_COMMAND = get_command("PLAYMODE_COMMAND")


@bot.on_message(
    filters.command(PLAYMODE_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def playmode_(client, message: Message, _):
    playmode = await get_playmode(message.chat.id)
    if playmode == "Direct":
        Direct = True
    else:
        Direct = None
    is_non_admin = await is_nonadmin_chat(message.chat.id)
    if not is_non_admin:
        Group = True
    else:
        Group = None
    playty = await get_playtype(message.chat.id)
    if playty == "Everyone":
        Playtype = None
    else:
        Playtype = True
    buttons = playmode_users_markup(_, Direct, Group, Playtype)
    response = await message.reply_text(
        _["playmode_1"].format(message.chat.title),
        reply_markup=InlineKeyboardMarkup(buttons),
    )
