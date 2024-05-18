# Powered By @ZeroNxz & @Professor7x
# Join @ZeronxzTech For More Updates
# Join @Zero For Hacks
# Join Our Chats @ZeroChats & @Professor7x


from pyrogram import filters
from pyrogram.types import Message

from Zero.config import BANNED_USERS
from Zero.nxz import get_command
from Zero import app
from Zero.core.call import Bikashh
from Zero.utils.database import set_loop
from Zero.utils.decorators import AdminRightsCheck
from Zero.utils.bgtmusic.bk import command
from Zero.utils.inline.play import close_keyboard

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    filters.command(STOP_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Zero.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.first_name),
        reply_markup=close_keyboard,
    )



# Powered By @ZeroNxz & @Professor7x
# Join @ZeronxzTech For More Updates
# Join @Zero For Hacks
# Join Our Chats @ZeroChats & @Professor7x
