from pyrogram import Client, filters

from Bikash import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(
    filters.command("donate")
    )
async def donate(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/filea10fdd5b3d87e220e8d9b.jpg",
        caption=f"𝗭𝗲𝗿𝗼 𝐈𝐬 𝐎𝐰𝐧𝐞𝐫 𝐎𝐟 𝗭𝗲𝗿𝗼 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 🌺, 𝐂𝐥𝐢𝐜𝐤 𝐁𝐞𝐥𝐨𝐰 𝐁𝐮𝐭𝐭𝐨𝐧 𝐅𝐨𝐫 𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝘇𝗲𝗿𝗼 ♕, 𝐈𝐟 𝐘𝐨𝐮 𝐖𝐚𝐧𝐭 𝐏𝐫𝐨𝐦𝐨𝐭𝐞 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩𝐬 𝐎𝐫 𝐎𝐭𝐡𝐞𝐫𝐬 𝐋𝐢𝐧𝐤, 𝐓𝐡𝐞𝐧 𝐂𝐥𝐢𝐜𝐤 𝐏𝐫𝐨𝐦𝐨𝐭𝐢𝐨𝐧 𝐁𝐮𝐭𝐭𝐨𝐧 𝐂𝐥𝐢𝐜𝐤 𝐎𝐭𝐡𝐞𝐫𝐬 𝐁𝐮𝐭𝐭𝐨𝐧 & 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 𝐎𝐫 𝐆𝐫𝐨𝐮𝐩.. 🥀 [𝗖𝗵𝗮𝗻𝗻𝗲𝗹](""https://t.me/+BWruaT7T_iE5ZGJl")",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 𝙕𝙚𝙧𝙤 🥀", url=f"https://t.me/ZERO_NXZ")
            ],          
            [
                    InlineKeyboardButton(
                        "🥀 𝙕𝙚𝙧𝙤 🥀", url=f"https://t.me/ZERO_NXZ")
                ],
                [
                    InlineKeyboardButton(
                        "🥀 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 🥀", url=f"https://t.me/+BWruaT7T_iE5ZGJl")
                    ),
                    InlineKeyboardButton(
                        "🥀 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 🥀", url=f"https://t.me/+x3M8fu6wkJM4Njc1")
                ]
            ]
        ),
    )
