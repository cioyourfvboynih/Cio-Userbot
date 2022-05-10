#Ice-Userbot @UsersBanned
FROM kenkannih/ice-userbot:buster

RUN git clone -b Cio-Userbot https://github.com/cioyourfvboynih/Cio-Userbot /home/iceuserbot/ \
    && chmod 777 /home/iceuserbot \
    && mkdir /home/iceuserbot/bin/

WORKDIR /home/iceuserbot/

CMD [ "bash", "start" ]
