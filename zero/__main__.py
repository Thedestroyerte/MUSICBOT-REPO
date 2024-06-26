import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

from Zero import config
from Zero import LOGGER, app, userbot
from Zero.core.call import Bikashh
from Zero.misc import sudo
from plugins import ALL_MODULES
from Zero.utils.database import get_banned_users, get_gbanned
from Zero.config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("plugins" + all_module)
    LOGGER("plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Zero.start()
    await Zero.decorators()
    LOGGER("Zero").info(
        "bot started"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Zero").info("Stopping Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
