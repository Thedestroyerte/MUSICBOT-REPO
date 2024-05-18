# Powered By @ZeroNxz & @Professor7x
# Join @ZeronxzTech For More Updates
# Join @Zero For Hacks
# Join Our Chats @ZeroChats & @Professor7x


from pyrogram import filters
from pyrogram.types import Message

from Zero.config import BANNED_USERS
from Zero.nxz import get_command
from Zero import app
from Zero.core.call import Zero
from Zero.utils.database import is_music_playing, music_off
from Zero.utils.decorators import AdminRightsCheck
from Zero.utils.inline.play import close_keyboard

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@app.on_message(
    filters.command(PAUSE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Zeroo.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.first_name),
        reply_markup=close_keyboard
    )


# Powered By @ZeroNxz & @Professor7x
# Join @ZeronxzTech For More Updates
# Join @Zero For Hacks
# Join Our Chats @ZeroChats & @Professor7x
