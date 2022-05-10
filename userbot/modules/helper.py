""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, ice_cmd


@ice_cmd(pattern="ihelp$")
async def usit(event):
    await edit_or_reply(
        event,
        f"**Hai {owner} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"✮ **Group :** [𝗣𝗥𝗢𝗝𝗘𝗖𝗧 𝗖𝗜𝗢​](t.me/projectcio)\n"
        f"✮ **Channel :** [𝗖𝗜𝗢 𝗠𝗨𝗦𝗜𝗖](t.me/ciomusic)\n"
        f"✮ **Owner Repo :** [ᴋɪɴɢ ᴄɪᴏ](t.me/cioyourfvboy)\n"
        f"✮ **Repo :** [ᴄɪᴏ-Usᴇʀʙᴏᴛ](https://github.com/cioyourfvboynih/Cio-Userbot)\n",
    )


@ice_cmd(pattern="listvar$")
async def var(event):
    await edit_or_reply(
        event,
        "**Daftar Lengkap Vars Dari Ice-Userbot:** [KLIK DISINI](https://telegra.ph/List-Variabel-Heroku-untuk-Man-Userbot-09-22)",
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  •  **Syntax :** `{cmd}ihelp`\
        \n  •  **Function : **Bantuan Untuk Cio-Userbot.\
        \n\n  •  **Syntax :** `{cmd}listvar`\
        \n  •  **Function : **Melihat Daftar Vars.\
        \n\n  •  **Syntax :** `{cmd}repo`\
        \n  •  **Function : **Melihat Repository Cio-Userbot.\
        \n\n  •  **Syntax :** `{cmd}string`\
        \n  •  **Function : **Link untuk mengambil String Cio-Userbot.\
    "
    }
)
