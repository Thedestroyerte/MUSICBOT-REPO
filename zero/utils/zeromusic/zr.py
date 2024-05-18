# Powered By @ZERO_NXZ @professor_7x

from typing import Union, List
from pyrogram import filters
from Zero.config import COMMAND_PREFIXES



def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)
