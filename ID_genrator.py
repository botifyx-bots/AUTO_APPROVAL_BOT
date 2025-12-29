# -*- coding: utf-8 -*-
# NO CHANGE IN THIS FILE IS NEEDED TO BE DONE
from pyrogram import filters

def setup_img_id_handler(bot):

    @bot.on_message(filters.command("img_id") & filters.reply)
    async def img_id_handler(client, message):

        replied = message.reply_to_message

        if replied.photo:
            file_id = replied.photo.file_id

        elif replied.document and replied.document.mime_type and replied.document.mime_type.startswith("image/"):
            file_id = replied.document.file_id

        else:
            await message.reply_text(
                "❌ The replied message is not an image.",
                quote=True
            )
            return

        await message.reply_text(
            "✅ **Photo ID Generated Successfully!**\n\n"
            f"`{file_id}`",
            quote=True
        )

    @bot.on_message(filters.command("img_id"))
    async def img_id_no_reply(client, message):
        await message.reply_text(
            "❌ Please reply to an image with /img_id.",
            quote=True
        )