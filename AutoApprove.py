# -*- coding: utf-8 -*-

from pyrogram.enums import ParseMode
from Fsub import (
    is_user_joined_all,
    FORCE_SUB_PHOTO_ID,
    FORCE_SUB_CHANNEL_LINKS
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


APPROVE_PHOTO_ID = ""   # HERE YOU CAN PUT AN APPROVAL PHOTO ID IF YOU WANT


def setup_auto_approve(bot):

    @bot.on_chat_join_request()
    async def auto_approve_handler(client, join_request):

        join_user = join_request.from_user
        join_chat = join_request.chat

        user_mention = join_user.mention
        chat_name = join_chat.title

        # 🔒 FORCE-SUB CHECK
        joined = await is_user_joined_all(client, join_user.id)

        # ❌ NOT JOINED → SEND TEXT FIRST, THEN FSUB MESSAGE
        if not joined:

            mention = join_user.mention

            # 1️⃣ SEND TEXT MESSAGE FIRST
            try:
                await client.send_message(
                    chat_id=join_user.id,
                    text=(                                           # FORCE-SUB TEXT MESSAGE-1
                        f"◈ Hᴇʏ  {mention} ×\n\n"
                        "›› ʏᴏᴜ ᴍᴜsᴛ ᴊᴏɪɴ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟs "
                        "ʙᴇғᴏʀᴇ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴄᴀɴ ʙᴇ ᴀᴘᴘʀᴏᴠᴇᴅ."
                        "‼️𝖠𝖥𝖳𝖤𝖱 𝖩𝖮𝖨𝖭𝖨𝖭𝖦 𝖳𝖧𝖤  𝖥𝖮𝖱𝖢𝖤 𝖲𝖴𝖡 𝖢𝖧𝖠𝖭𝖭𝖤𝖫 "
                        "𝖳𝖱𝖸 𝖩𝖮𝖨𝖭ING 𝖳𝖧𝖤 𝖢𝖧𝖠𝖭𝖭𝖤𝖫 𝖠𝖦𝖠𝖨𝖭.\n\n"
                    ),
                    parse_mode=ParseMode.HTML
                )
            except Exception:
                pass

            # 2️⃣ SEND FULL FORCE-SUB MESSAGE (PHOTO + BUTTONS)
            fsub_text = (
                f"◈ Hᴇʏ  {mention} ×\n\n"
                "›› ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️  "
                "ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ "
                "ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, "
                "sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs\n\n"
                "›› Pᴏᴡᴇʀᴇᴅ ʙʏ : "
                "<a href='https://t.me/Akuma_Rei_Kami'>Akuma Rei</a>"
            )

            join_buttons = [
                [InlineKeyboardButton(f"➥ JOIN CHANNEL {i+1}", url=link)]
                for i, link in enumerate(FORCE_SUB_CHANNEL_LINKS)
            ]

            try:
                await client.send_photo(
                    chat_id=join_user.id,
                    photo=FORCE_SUB_PHOTO_ID,
                    caption=fsub_text,
                    reply_markup=InlineKeyboardMarkup(join_buttons),
                    parse_mode=ParseMode.HTML
                )
            except Exception:
                pass

            return  # ❌ DO NOT APPROVE



        # ✅ APPROVE JOIN REQUEST
        await join_request.approve()

        approval_caption = (
            f"◈ Hᴇʏ {user_mention} ×\n\n"
            f"›› ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {chat_name} "
            "ʜᴀs ʙᴇᴇɴ ᴀᴘᴘʀᴏᴠᴇᴅ.\n\n"
            "›› Pᴏᴡᴇʀᴇᴅ ʙʏ : "
            "<a href='https://t.me/Akuma_Rei_Kami'>Akuma Rei</a>" #UPDATE YOUR CREDIT LINK IF YOU WANT
        )

        try:
            await client.send_photo(
                chat_id=join_user.id,
                photo=APPROVE_PHOTO_ID,
                caption=approval_caption,
                parse_mode=ParseMode.HTML
            )
        except Exception:
            pass