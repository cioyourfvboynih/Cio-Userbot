""" Userbot module for other small commands. """
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, owner
from userbot.utils import edit_or_reply, ice_cmd


@ice_cmd(pattern="ihelp$")
async def usit(event):
    await edit_or_reply(
        event,
        f"**Hai {owner} Kalo Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        f"â® **Group :** [ð£ð¥ð¢ðððð§ ððð¢â](t.me/projectcio)\n"
        f"â® **Channel :** [ððð¢ ð ð¨ð¦ðð](t.me/ciomusic)\n"
        f"â® **Owner Repo :** [á´ÉªÉ´É¢ á´Éªá´](t.me/cioyourfvboy)\n"
        f"â® **Repo :** [á´Éªá´-Usá´ÊÊá´á´](https://github.com/cioyourfvboynih/Cio-Userbot)\n",
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
        \n\n  â¢  **Syntax :** `{cmd}ihelp`\
        \n  â¢  **Function : **Bantuan Untuk Cio-Userbot.\
        \n\n  â¢  **Syntax :** `{cmd}listvar`\
        \n  â¢  **Function : **Melihat Daftar Vars.\
        \n\n  â¢  **Syntax :** `{cmd}repo`\
        \n  â¢  **Function : **Melihat Repository Cio-Userbot.\
        \n\n  â¢  **Syntax :** `{cmd}string`\
        \n  â¢  **Function : **Link untuk mengambil String Cio-Userbot.\
    "
    }
)
