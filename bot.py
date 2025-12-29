# -*- coding: utf-8 -*-

import os
import threading
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ParseMode
# 👉 IMPORT MODULE 
from Fsub import setup_force_sub
from ID_genrator import setup_img_id_handler
from AutoApprove import setup_auto_approve

# ================= CONFIG =================
API_ID = # your api id
API_HASH = ""  # your api hash key
BOT_TOKEN = "" # your telegram bot token
# =========================================

bot = Client(
    "simple_start_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =================================================
# 🔒 FORCE SUB MUST BE REGISTERED FIRST
# Allows /start, blocks everything else
# =================================================
setup_force_sub(bot)

# =================================================
# 🔗 IMAGE ID HANDLER (BLOCKED UNTIL FORCE SUB DONE)
# =================================================
setup_img_id_handler(bot)

# =================================================
# 🔗 AUTO APPROVE HANDLER (BLOCKED UNTIL FORCE SUB DONE)
# =================================================
setup_auto_approve(bot)

# ---------- START (ALWAYS ALLOWED) ----------
@bot.on_message(filters.command("start"))
async def start_cmd(client, message): 
    photo_id = "" # change your photo id if you want

    caption = (  # you can change the text as you want
        "<code>WELCOME TO THE ADVANCED AUTO APPROVAL SYSTEM.\n"
        "WITH THIS BOT, YOU CAN MANAGE JOIN REQUESTS AND\n"
        "KEEP YOUR CHANNELS SECURE.</code>\n\n"
        "<blockquote><b>➥ MAINTAINED BY : "
        "<a href='https://t.me/Akuma_Rei_Kami'>Akuma_Rei</a>"
        "</b></blockquote>"
    )
# ---------- BUTTONS ----------     # you can change the buttons as you want
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("➥ 𝐀𝐁𝐎𝐔𝐓", callback_data="about")],
            [
                InlineKeyboardButton("➥ 𝗢𝗪𝗡𝗘𝗥", url="https://t.me/Akuma_Rei_Kami"),
                InlineKeyboardButton("➥ 𝐍𝐄𝐓𝐖𝐎𝐑𝐊", url="https://t.me/BotifyX_Pro")
            ],
            [InlineKeyboardButton("➥ 𝗖𝗟𝗢𝗦𝗘", callback_data="close_msg")]
        ]
    )

    await message.reply_photo(
        photo=photo_id,
        caption=caption,
        reply_markup=buttons,
        parse_mode=ParseMode.HTML
    )

# ---------- HELPERS ----------
@bot.on_callback_query(filters.regex("^close_msg$"))
async def close_msg(client, callback_query):
    await callback_query.message.delete()

@bot.on_callback_query(filters.regex("^back_start$"))
async def back_start(client, callback_query):
    await callback_query.message.delete()
    await start_cmd(client, callback_query.message)

# ---------- ABOUT ----------
@bot.on_callback_query(filters.regex("^about$"))
async def about_callback(client, callback_query): 
    photo_id2 = "" # change your photo id if you want

    about_text = ( # you can change the text as you want
        "<pre>BOT INFORMATION AND STATISTICS</pre>\n\n"
        "<blockquote> <b>»» My Name :</b>"
        "<a href='https://t.me/MORVESSA_NIGHTMARE_BOT'>𝙈𝙊𝙍𝙑𝙀𝙎𝙎𝘼</a>\n"
        "<b>»» Developer :</b> @Akuma_Rei_Kami\n"
        "<b>»» Library :</b> <a href='https://docs.pyrogram.org/'>Pyrogram v2</a>\n"
        "<b>»» Language :</b> <a href='https://www.python.org/'>Python 3</a>\n"
        "<b>»» Database :</b> <a href='https://www.mongodb.com/docs/'>MongoDB</a>\n"
        "<b>»» Hosting :</b> <a href='https://render.com/'>Render</a>"
        "</blockquote>"
    )

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➥ SUPPORT", url="https://t.me/BotifyX_support"),
                InlineKeyboardButton("➥ CLOSE", callback_data="close_msg")
            ]
        ]
    )

    await callback_query.message.reply_photo(
        photo=photo_id2,
        caption=about_text,
        reply_markup=buttons,
        parse_mode=ParseMode.HTML
    )

    await callback_query.answer()

# -------- WEB SERVER (RENDER) --------  
# to keep bot alive on render.com
# no change needed here it is just a simple flask app to keep bot alive
         # work it work on render it is needed so don't change anything here
         # it's very important don't change anything here
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# -------- MAIN --------
if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot.run()








