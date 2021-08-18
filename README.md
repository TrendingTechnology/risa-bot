# Risa Bot
 
#### Introduction

    Risa is an nHentai discord bot that will help you browse and download your favorite doujin
inside your own discord server.

#### Manual Hosting

    To manual host Risa, just simply go into the `config` folder and edit the `config.txt` by 
replacing `YourDiscordBotTokenHere` with your discord app token.

#### Heroku Hosting

    Risa is now host-ready for heroku! To host, just simply use add your token as a config var 
to your heroku app with the name `BOT_TOKEN`.

#### Command list

###### Read Command

usage: 
    `!read popular` - returns a paginated message containing popular uploads.
    `!read newest`  - returns a paginated message containing newest uploads.   
    `!read <id>`    - returns a message containing the doujin.  

    