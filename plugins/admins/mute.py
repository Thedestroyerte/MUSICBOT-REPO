# Powered By @ZeroNxz & @Professor7x
# Join @ZeronxzTech For More Updates
# Join @Zero For Hacks
# Join Our Chats @ZeroChats & @Professor7x

from pyrogram import filters
from pyrogram.types import Message

from Zero.config import BANNED_USERS
from Zero import app
from Zero.core.call import Zero
from Zero.utils.database import is_muted, mute_on
from Zero.utils.decorators import AdminRightsCheck


@app.on_message(
    filters.command(["mute", "cmute"])
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1 or message.reply_to_message:
        return await message.reply_text("**❌ 𝐄𝐫𝐫𝐨𝐫, 𝐖𝐫𝐨𝐧𝐠 𝐔𝐬𝐚𝐠𝐞 𝐎𝐟 𝐂𝐨𝐦𝐦𝐚𝐧𝐝❗...**")
    if await is_muted(chat_id):
        return await message.reply_text("**🔇 𝐁𝐠𝐭 𝐌𝐮𝐬𝐢𝐜 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐌𝐮𝐭𝐞𝐝 🌷 ...**")
    await mute_on(chat_id)
    await Zeroo.mute_stream(chat_id)
    await message.reply_text("**🔇 𝐌𝐮𝐭𝐞𝐝 🌷 ...**\n\n⎿𝐑𝐞𝐪𝐮𝐞𝐬𝐭𝐞𝐝 𝐁𝐲 > {}")



# Powered By @ZeroNxz & @Professor7x
# Join @ZeronxzTech For More Updates
# Join @Zero For Hacks
# Join Our Chats @ZeroChats & @Professor7x
