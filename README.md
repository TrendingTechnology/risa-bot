# Risa

![Risa](https://i.ibb.co/JnkVh0L/18-cropped.jpg)

#### Introduction

Risa is an nHentai discord bot that will help you browse and download your favorite doujin inside your own discord server.

#### Manual Hosting

To manual host Risa, just simply go into the `config` folder and edit the `config.txt` by replacing `YourDiscordBotTokenHere` with your discord app token and changing the file extension from `.txt` to `.json` and then execute the `scripts/risa_main.py` file.

#### Heroku Hosting

Risa is now host-ready for heroku! To host, just simply add your token as a config var 
to your heroku app with the name `BOT_TOKEN`.

#### Command list

##### Read Command

###### Usage
* `!read popular`-------- returns a paginated message containing popular uploads.
* `!read newest`--------- returns a paginated message containing newest uploads.
* `!read random`--------- returns a message containing the doujin with random id. 
* `!read <id>`----------- returns a message containing the doujin on the given id. 

##### Search Command

###### Usage
* `!search <query>`------ returns a paginated message containing all matches on the query.


##### Download Command

###### Usage
* `!download <id>`------- returns a message containing the download link of the doujin on the given id.


#### More Info

[risa invite link](https://discord.com/api/oauth2/authorize?client_id=874157314565881876&permissions=0&scope=bot)
