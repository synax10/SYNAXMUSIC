from pyrogram import filters

from PrachiMusic.utilities import config
from PrachiMusic.utilities.strings import get_command
from PrachiMusic import bot
from PrachiMusic.misc import SUDOERS
from PrachiMusic.modules.main.database import add_off, add_on
from PrachiMusic.modules.main.decorators.language import language

# Commands
LOGGER_COMMAND = get_command("LOGGER_COMMAND")


@bot.on_message(filters.command(LOGGER_COMMAND) & SUDOERS)
@language
async def logger(client, message, _):
    usage = _["log_1"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "enable":
        await add_on(config.LOG)
        await message.reply_text(_["log_2"])
    elif state == "disable":
        await add_off(config.LOG)
        await message.reply_text(_["log_3"])
    else:
        await message.reply_text(usage)
