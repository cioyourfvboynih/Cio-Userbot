#Ice-Userbot @UsersBanned
FROM cioyourfvboy/cio-userbot:buster

RUN git clone -b Cio-Userbot https://github.com/cioyourfvboynih/Cio-Userbot /home/ciouserbot/ \
    && chmod 777 /home/iceuserbot \
    && mkdir /home/ciouserbot/bin/

WORKDIR /home/ciouserbot/

CMD [ "bash", "start" ]
