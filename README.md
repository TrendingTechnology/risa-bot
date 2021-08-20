# Risa

<img src="https://i.ibb.co/JnkVh0L/18-cropped.jpg" width="250" height="250">

### Introduction
Risa is an nHentai discord bot that will help you browse and download your favorite doujin inside your own discord server.

### Hosting

###### Manual Hosting
To manual host Risa, just simply go into the `config` folder and edit the `config.txt` by replacing `YourDiscordBotTokenHere` with your discord app token and changing the file extension from `.txt` to `.json`.

###### Heroku Hosting
Risa is now host-ready for heroku! To host, just simply add your token as a config var 
to your heroku app with the name `BOT_TOKEN`.

### Commands

##### Read Command

###### Usage
`!read <popular/newest/random/id>`
- returns a message/paginated message based on id or keyword in the input.
###### Examples
* `!read popular`
 returns a paginated message containing popular uploads.
* `!read newest`
 returns a paginated message containing newest uploads.
* `!read random`
 returns a message containing the doujin with random id.
* `!read 177013`
 returns a message containing the doujin with id of "177013".

##### Search Command

###### Usage
* `!search <query>`
 Returns a paginated message containing all matches on the query. Uses the same query system on the nh website.
 Note: there should be **no spaces** between **colons**, use **double quotes** for accuracy on tag name, and use **dash line** to avoid a tag. See the nh website guide [here](https://nhentai.net/info/).
###### Examples
* `!search Madoka Higuchi`
 returns all matching doujins with name "Madoka Higuchi".
* `!search parody:Bang Dream`
 returns all matching doujins with a parody name "Bang Dream"
* `!search tag:mind break characters:Lizbeth`
 returns all matching doujins with tag name "mind break" and character name "Lizbeth".
* `!search artists:"artistname" -tag:"tentacles"`
 returns only the matching doujins with artist name "artistname" but not with tag "tentacles".


##### Download Command

###### Usage
* `!download <id>`------- returns a message containing the download link of the doujin on the given id.
###### Examples
* `!download 367361`
 returns a message containing the download link of the doujin with id of "367361".

### Changelogs
* Fixed some text bugs in some commands
* Added 10-page jump on paginated messages
* Added loading embed on search command

### More Info
Add risa to your server [here](https://discord.com/api/oauth2/authorize?client_id=874157314565881876&permissions=0&scope=bot)





