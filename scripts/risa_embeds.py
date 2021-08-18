
from discord import Embed
from hentai.hentai import Format
from risa_settings import *
from risa_utils import RisaUtils

utils = RisaUtils()

class RisaIntroEmbed(Embed):
    def __init__(self, obj):
        super().__init__()
        self.set_author(name=TOP_EMBED_TEXT, icon_url=ICON_URL)
        self.set_image(url=obj.cover)
        self.description = "**[{}]({})**".format(obj.title(Format.Pretty), obj.url)
        self.parody = utils.capitalize_and_join(utils.extract_names(obj.parody))
        self.add_field(name='Parody', value=self.parody if self.parody != '' else "None", inline=False)
        self.chars = utils.capitalize_and_join(utils.extract_names(obj.character))
        self.add_field(name='Character', value=self.chars if self.chars != '' else "None", inline=False)
        self.artists = utils.capitalize_and_join(utils.extract_names(obj.artist))
        self.add_field(name='Artist', value=f"**{self.artists}**" if self.artists != '' else "None", inline=False)
        self.languages = utils.capitalize_and_join(utils.extract_names(obj.language))
        self.add_field(name='Language', value=self.languages if self.languages != '' else "None", inline=False)
        self.categories = utils.capitalize_and_join(utils.extract_names(obj.category))
        self.add_field(name='Category', value=self.categories if self.categories != '' else "None", inline=False)
        self.pages = len(obj.pages)
        self.add_field(name='Pages', value=self.pages if self.pages != '' else "None", inline=False)
        self.tags = utils.capitalize_and_join(utils.extract_names(obj.tag))
        self.add_field(name='Tags', value=self.tags if self.tags != '' else "None", inline=False)
        self.upload_date = utils.convert_upload_date(obj.upload_date)
        self.add_field(name='Uploaded', value=self.upload_date if self.upload_date != '' else "None", inline=False)

        
class RisaReadEmbed(Embed):
    def __init__(self, obj, index=1):
        super().__init__()
        self.set_author(name=TOP_EMBED_TEXT, icon_url=ICON_URL)
        self.set_image(url=obj.pages[index-1].url)
        self.set_footer(text=f"Page {index}/{len(obj.pages)}")
        self.description = "**[{}]({})**".format(obj.title(Format.Pretty), obj.url)


class RisaPaginatedEmbed(Embed):
    def __init__(self, obj_list, title, index=1):
        super().__init__()
        self.set_author(name=TOP_EMBED_TEXT, icon_url=ICON_URL)
        self.title = title
        self.set_image(url=obj_list[index-1].cover)
        self.set_footer(text=f"Page {index}/{len(obj_list)}")
        self.description = "**[{}]({})**".format(obj_list[index-1].title(Format.Pretty), obj_list[index-1].url)