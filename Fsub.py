# -*- coding: utf-8 -*-

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ================= FORCE SUB CONFIG =================

FORCE_SUB_CHANNEL_IDS = [
    -1003538176254, # your channel id
    -1003466949099, # your channel id and so on
]

FORCE_SUB_CHANNEL_LINKS = [
    "https://t.me/BotifyX_Pro",                   # your channel url link
    "https://t.me/Shadow_Slave_Sunless_Star",     # your channel url link and so on
]
# ===================================================
# here you can put your own photo id
FORCE_SUB_PHOTO_ID = "AgACAgUAAxkBAAIB7mlSIsT2RNCVERLvm9oc9_QJPfb3AAJeC2sbFqKQVjNjG-mOqPKPAAgBAAMCAAN5AAceBA"

# ===================================================


# ✅ EXPORTED FUNCTION (USED BY AUTO-APPROVE)
async def is_user_joined_all(client, user_id):
    for channel_id in FORCE_SUB_CHANNEL_IDS:
        try:
            member = await client.get_chat_member(channel_id, user_id)
            if member.status not in (
                ChatMemberStatus.MEMBER,
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER
            ):
                return False
        except Exception:
            return False
    return True


def setup_force_sub(bot):

    @bot.on_message(filters.private & ~filters.command(["start", "img_id", "upscale"]))
    async def force_sub_handler(client, message):

        joined = await is_user_joined_all(client, message.from_user.id)
        if joined:
            return

        mention = message.from_user.mention

        fsub_text = (      # can change the text as you want
            f"◈ Hᴇʏ  {mention} ×\n\n"
            "›› ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️  "
            "ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ "
            "ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, "
            "sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs\n\n"
            "›› Pᴏᴡᴇʀᴇᴅ ʙʏ : "
            "<a href='https://t.me/Akuma_Rei_Kami'>Akuma Rei</a>" #UPDATE YOUR CREDIT LINK IF YOU WANT
        )

        join_buttons = [
            [InlineKeyboardButton(f"➥ JOIN CHANNEL {i+1}", url=link)]
            for i, link in enumerate(FORCE_SUB_CHANNEL_LINKS)
        ]

        join_buttons.append(
            [InlineKeyboardButton("➥ CHECK JOIN", callback_data="check_fsub")]
        )

        await message.reply_photo(
            photo=FORCE_SUB_PHOTO_ID,
            caption=fsub_text,
            reply_markup=InlineKeyboardMarkup(join_buttons),
            parse_mode=ParseMode.HTML
        )

        message.stop_propagation()

    @bot.on_callback_query(filters.regex("^check_fsub$"))
    async def check_force_sub(client, callback_query):

        joined = await is_user_joined_all(client, callback_query.from_user.id)

        if joined:
            await callback_query.message.delete()
            await callback_query.answer(
                "✅ Access granted! You can now use the bot.",
                show_alert=True
            )
        else:
            await callback_query.answer(
                "❌ You must join ALL required channels first!",
                show_alert=True
            )