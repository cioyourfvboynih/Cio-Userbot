# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Copyright (C) 2021 TeamUltroid for autobot
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
# credits by @cioyourfvboy kalau copas ya kasih credits
# 
""" Userbot start point """

import sys
from importlib import import_module
from pytgcalls import idle
import requests
from userbot import BOT_TOKEN, BOT_USERNAME, BOT_VER, BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import DEVS, LOGS, bot, branch, call_py
from userbot.modules import ALL_MODULES
from userbot.utils import autobot, checking, autopilot

try:
    bot.start()
    call_py.start()
    user = bot.get_me()
    blacklistman = requests.get(
        "https://raw.githubusercontent.com/cioyourfvboy/Reforestation/master/manblacklist.json"
    ).json()
    if user.id in blacklistman:
        LOGS.warning(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOTNYA GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @mrismanaziz\nClone: @escape_aja"
        )
        sys.exit(1)
    if 1780709155 not in DEVS:
        LOGS.warning(
            f"EOL\nCio-UserBot v{BOT_VER}, Copyright © 2021-2022 ᴋɪɴɢ ᴄɪᴏ• <https://github.com/cioyourfvboynih>"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Jika {user.first_name} Membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/projectcio"
)

LOGS.info(f"Cio-Userbot ⚙🔥 V{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")

if not BOTLOG_CHATID:
    LOGS.info(
        "BOTLOG_CHATID Vars tidak terisi, Memulai Membuat Grup Otomatis..."
    )
    bot.loop.run_until_complete(autopilot())

async def ice_userbot_on():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_message(
                BOTLOG_CHATID,
                f"🔥 **Cio-Userbot Berhasil Di Aktifkan**\n━━\n➠ **Userbot Version -** `{BOT_VER}@{branch}`\n➠ **Ketik** `{cmd}alive` **Untuk Mengecek Bot**\n━━",
            )
    except Exception as e:
        LOGS.info(str(e))
    

bot.loop.run_until_complete(checking())
bot.loop.run_until_complete(ice_userbot_on())
if not BOT_TOKEN:
    bot.loop.run_until_complete(autobot())
idle()
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
