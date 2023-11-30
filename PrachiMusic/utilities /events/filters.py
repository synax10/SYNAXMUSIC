# Powered By @synax_network

from typing import Union, List
from pyrogram import filters
from SankiMusic.utilities.config import COMMAND_PREFIXES


# ╔══╗╔══╗╔═╦╗╔╦╗╔══╗  ╔═╦═╗╔╦╗╔══╗╔══╗╔═╗
#   ⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️    ║║║║║║║║║══╣╚║║╝║╔╝
#                      ║║║║║║║║╠══║╔║║╗║╚╗
# ╚══╝╚╝╚╝╚╩═╝╚╩╝╚══╝  ╚╩═╩╝╚═╝╚══╝╚══╝╚═╝

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
