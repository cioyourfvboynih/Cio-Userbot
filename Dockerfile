# Using Python Slim-Buster
FROM skyzuxzy/skyzu-userbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Skyzuu-Userbot ━━━━━

RUN git clone -b Ciio-Userbot https://github.com/cioyourfvboynih/Cio-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

CMD [ "bash", "start" ]
