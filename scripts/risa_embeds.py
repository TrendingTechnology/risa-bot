
from datetime import datetime
from os import name
from discord import Embed, Colour
from hentai.hentai import Format
from risa_settings import *
from risa_utils import RisaUtils

utils = RisaUtils()


class RisaEmbed(Embed):
    def __init__(self):
        super().__init__()
        self.set_thumbnail(url=RISA_THUMB_URL)
        self.title = "Hello! I am Risa"
        self.color = Colour.light_grey()
        self.description = f"I am an nHentai discord bot that will help you browse"\
        " and download your favorite doujin inside your own discord server. You can"\
        " invite me to your server [here](https://discord.com/api/oauth2/authorize?client_id=874157314565881876&permissions=0&scope=bot). Type "\
        f"`{PREFIX}help` to start using me!"
        self.add_field(name="Contact My Owner", value=f"[Github]({GITHUB_LINK})\n"\
            f"[G-mail]({GMAIL})")

        self.add_field(name="More Info Here", value=f"[Full Guide]({GITHUB_README_LINK})\n[Source Code]({SOURCE_CODE})")
        self.timestamp = datetime.utcnow()


class RisaHelpEmbed(Embed):
    def __init__(self):
        super().__init__()
        self.set_author(name=TOP_EMBED_TEXT, icon_url=ICON_URL)
        self.title = "Here are Risa's commands"
        self.add_field(name=f"`{PREFIX}read <id/popular/newest/random>`",
            value=f"- returns a message/paginated message that matches to the given <id> or <popular/newest/random>.",
            inline=False
        )
        self.add_field(name=f"`{PREFIX}download <id>`",
            value="- returns a message containing the download link of the given <id>.",
            inline=False
        )
        self.add_field(name=f"`{PREFIX}search <query>`",
            value="- returns a paginated message containing all matches on the given <query>.",
            inline=False
        )
        self.add_field(name="Contact My Owner", value=f"[Github]({GITHUB_LINK})\n"\
            f"[G-mail]({GMAIL})"
        )
        self.add_field(name="More Info Here", value=f"[Full Guide]({GITHUB_README_LINK})\n[Source Code]({SOURCE_CODE})")
        self.timestamp = datetime.utcnow()

class RisaIntroEmbed(Embed):
    def __init__(self, obj):
        super().__init__()
        self.set_author(name=TOP_EMBED_TEXT, icon_url=ICON_URL)
        self.set_image(url=obj.cover)
        self.description = "**[{}]({})**".format(obj.title(Format.Pretty), obj.url)
        self.parody = utils.capitalize_and_join(utils.extract_names(obj.parody))
        self.add_field(name='Parody', value=self.parody if self.parody != '' else "None")
        self.chars = utils.capitalize_and_join(utils.extract_names(obj.character))
        self.add_field(name='Character', value=self.chars if self.chars != '' else "None")
        self.artists = utils.capitalize_and_join(utils.extract_names(obj.artist))
        self.add_field(name='Artist', value=f"**{self.artists}**" if self.artists != '' else "None")
        self.languages = utils.capitalize_and_join(utils.extract_names(obj.language))
        self.add_field(name='Language', value=self.languages if self.languages != '' else "None")
        self.categories = utils.capitalize_and_join(utils.extract_names(obj.category))
        self.add_field(name='Category', value=self.categories if self.categories != '' else "None")
        self.pages = len(obj.pages)
        self.add_field(name='Pages', value=self.pages if self.pages != '' else "None")
        self.num_fav = obj.num_favorites
        self.add_field(name='Favorites', value=str(self.num_fav) if self.num_fav != 0 else "None")
        self.upload_date = utils.convert_upload_date(obj.upload_date)
        self.add_field(name='Uploaded on', value=self.upload_date if self.upload_date != '' else "None", inline=False)
        self.tags = utils.capitalize_and_join(utils.extract_names(obj.tag))
        self.add_field(name='Tags', value=self.tags if self.tags != '' else "None", inline=False)
        self.set_footer(text=f"React {EMOJI_BOOK} to read #{obj.id}.")

        
class RisaReadEmbed(Embed):
    def __init__(self, obj, index=1):
        super().__init__()
        self.set_author(name=TOP_EMBED_TEXT, icon_url=ICON_URL)
        self.set_image(url=obj.pages[index-1].url)
        self.set_footer(text=f"Page {index}/{len(obj.pages)}")
        self.description = "**[{}]({})**".format(obj.title(Format.Pretty), obj.url)


class RisaDownloadEmbed(Embed):
    def __init__(self, obj):
        super().__init__()
        self.set_author(name=TOP_EMBED_TEXT, icon_url=ICON_URL)
        self.set_thumbnail(url=obj.cover)
        self.id = obj.id
        self.url = f"https://nhdl.herokuapp.com/download/nhentai/{self.id}/"
        self.description = "**[{}]({})**\nClick the title to download.".format(
            obj.title(Format.Pretty), self.url
        )

class RisaPaginatedEmbed(Embed):
    def __init__(self, obj_list, title, index=1):
        super().__init__()
        self.set_author(name=TOP_EMBED_TEXT, icon_url=ICON_URL)
        self.title = title
        self.index = utils.normalize_page_index(index, len(obj_list))
        self.obj = obj_list[self.index-1]
        self.languages = utils.capitalize_and_join(utils.extract_names(self.obj.language))
        self.add_field(name='Language', value=self.languages if self.languages != '' else "None")
        self.pages = len(self.obj.pages)
        self.add_field(name='Pages', value=self.pages if self.pages != '' else "None")
        self.num_fav = self.obj.num_favorites
        self.add_field(name='Favorites', value=str(self.num_fav) if self.num_fav != 0 else "None", inline=False)
        self.set_image(url=self.obj.cover)
        self.set_footer(text=f"Page {self.index}/{len(obj_list)} | React {EMOJI_BOOK_GET} to check #{self.obj.id}.")
        self.description = "**[{}]({})**".format(self.obj.title(Format.Pretty), self.obj.url)

class RisaLoadEmbed(Embed):
    def __init__(self, gif, text):
        super().__init__()
        self.description = text
        self.set_image(url=gif)

