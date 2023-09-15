# Powered By @AdityaHalder

from typing import Union, List
from pyrogram import filters
from PrachiMusic.utilities.config import COMMAND_PREFIXES


# @THE_WEBNET_NETWORK
def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
