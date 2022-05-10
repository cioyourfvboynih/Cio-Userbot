#Cio-Userbot @cioyourfvboy
FROM cioyourfvboy/cio-userbot:buster

RUN git clone -b Ciio-Userbot https://github.com/cioyourfvboynih/Cio-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot



CMD [ "bash", "start" ]
