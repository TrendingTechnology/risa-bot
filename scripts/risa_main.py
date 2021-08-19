
from hentai import Hentai, Utils, Sort
from discord.ext import commands, tasks
from discord.flags import Intents
from hentai.hentai import Homepage
from risa_utils import RisaUtils
from risa_embeds import RisaPaginatedEmbed
from risa_embeds import RisaDownloadEmbed
from risa_embeds import RisaIntroEmbed
from risa_embeds import RisaReadEmbed
from risa_embeds import RisaHelpEmbed
from risa_embeds import RisaEmbed
from risa_settings import *

utils = RisaUtils()
h_utils = Utils()

risaBot = commands.Bot(
    command_prefix=PREFIX,
    intents = Intents.all()
)
risaBot.remove_command('help')

@tasks.loop(hours=1)
async def get_updates():
    h_utils.get_homepage()


@risaBot.event
async def on_reaction_add(reaction, user):

    if reaction.emoji == EMOJI_BOOK and reaction.count > 1:
        embed = reaction.message.embeds[0]
        id = utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        read_embed = RisaReadEmbed(obj)
        read_message = await reaction.message.channel.send(embed=read_embed)
        for react in READ_MESSAGE_EMOJIS:
            await read_message.add_reaction(react)

    elif reaction.emoji == EMOJI_FIRST_PAGE and reaction.count > 1:
        embed = reaction.message.embeds[0]
        id = utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        page = 1
        read_embed = RisaReadEmbed(obj, index=page)
        read_message = await reaction.message.edit(embed=read_embed)

    elif reaction.emoji == EMOJI_LAST_PAGE and reaction.count > 1:
        embed = reaction.message.embeds[0]
        id = utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        page = len(obj.pages)
        read_embed = RisaReadEmbed(obj, index=page)
        read_message = await reaction.message.edit(embed=read_embed)
    
    elif reaction.emoji == EMOJI_NEXT_PAGE and reaction.count > 1:
        embed = reaction.message.embeds[0]
        footer = embed.footer.text
        page = int(utils.extract_curr_page_from_footer(footer)) + 1
        id = utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        read_embed = RisaReadEmbed(obj, index=page)
        read_message = await reaction.message.edit(embed=read_embed)

    elif reaction.emoji == EMOJI_BACK_PAGE and reaction.count > 1:
        embed = reaction.message.embeds[0]
        footer = embed.footer.text
        page = int(utils.extract_curr_page_from_footer(footer)) - 1
        id = utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        read_embed = RisaReadEmbed(obj, index=page)
        read_message = await reaction.message.edit(embed=read_embed) 

    elif reaction.emoji == EMOJI_BACK_PAGE_ALT and reaction.count > 1:
        embed = reaction.message.embeds[0]
        title = embed.title
        footer = embed.footer.text
        page = int(utils.extract_curr_page_from_footer(footer)) - 1

        if title == 'Popular Uploads':
            ref_name = 'Popular Uploads'
            data = utils.popular

        elif title == 'Newest Uploads':
            ref_name = 'Newest Uploads'
            data = utils.newest

        elif title.startswith("Search"):
            ref_name = title
            data = utils.retrieve_search_data(title)

        book_list = utils.remove_banned_tags(data)
        embed = RisaPaginatedEmbed(book_list, ref_name, index=page)
        await reaction.message.edit(embed=embed, delete_after=EMBED_DELETE_TIMER)

    elif reaction.emoji == EMOJI_NEXT_PAGE_ALT and reaction.count > 1:
        embed = reaction.message.embeds[0]
        title = embed.title
        footer = embed.footer.text
        page = int(utils.extract_curr_page_from_footer(footer)) + 1

        if title == 'Popular Uploads':
            ref_name = 'Popular Uploads'
            data = utils.popular

        elif title == 'Newest Uploads':
            ref_name = 'Newest Uploads'
            data = utils.newest
        
        elif title.startswith("Search"):
            ref_name = title
            data = utils.retrieve_search_data(title)

        book_list = utils.remove_banned_tags(data)
        embed = RisaPaginatedEmbed(book_list, ref_name, index=page)
        await reaction.message.edit(embed=embed, delete_after=EMBED_DELETE_TIMER)

    elif reaction.emoji == EMOJI_BOOK_GET and reaction.count > 1:
        embed = reaction.message.embeds[0]
        id = utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        embed = RisaIntroEmbed(obj)
        intro_mess = await reaction.message.channel.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
        for react in INTRO_MESSAGE_EMOJIS:
            await intro_mess.add_reaction(react)

    elif reaction.emoji == EMOJI_RANDOM and reaction.count > 1:
        embed = reaction.message.embeds[0]
        obj = utils.get_safe_source()
        embed = RisaIntroEmbed(obj)
        intro_mess = await reaction.message.edit(embed=embed, delete_after=EMBED_DELETE_TIMER)

    elif reaction.emoji == EMOJI_DOWNLOAD and reaction.count > 1:
        embed = reaction.message.embeds[0]
        id = utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        embed = RisaDownloadEmbed(obj)
        intro_mess = await reaction.message.channel.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
        await intro_mess.add_reaction(EMOJI_WASTEBASKET)

    elif reaction.emoji == EMOJI_WASTEBASKET and reaction.count > 1:
        await reaction.message.delete()


@risaBot.event
async def on_ready():
    await risaBot.change_presence(activity=BOT_STATUS)
    get_updates.start()
    print("ready")


# read command
@risaBot.group(invoke_without_command=True)
async def read(ctx, message):
    book = utils.get_source_by_id(message)
    if book:
        if not utils.check_for_banned_tags(book):
            embed = RisaIntroEmbed(book)
            intro_mess = await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
            for react in INTRO_MESSAGE_EMOJIS:
                await intro_mess.add_reaction(react)
        else:
            await ctx.send(
                BANNED_TAG_MSG,
                delete_after=SHORT_MSG_DELETE_TIMER
            )
    else:
        await ctx.send(
                NOT_EXIST_MSG,
                delete_after=SHORT_MSG_DELETE_TIMER
            )

# popular command
@read.command()
async def popular(ctx):
    book_list = utils.remove_banned_tags(utils.popular)
    embed = RisaPaginatedEmbed(book_list, 'Popular Uploads')
    paginated_mess = await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
    for react in PAGINATED_MESSAGE_EMOJIS:
        await paginated_mess.add_reaction(react)


# newest command
@read.command()
async def newest(ctx):
    book_list = utils.remove_banned_tags(utils.newest)
    embed = RisaPaginatedEmbed(book_list, 'Newest Uploads')
    paginated_mess = await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
    for react in PAGINATED_MESSAGE_EMOJIS:
        await paginated_mess.add_reaction(react)


# random command
@read.command()
async def random(ctx):
    book = utils.get_safe_source()
    embed = RisaIntroEmbed(book)
    intro_mess = await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
    for react in INTRO_MESSAGE_EMOJIS:
        await intro_mess.add_reaction(react)
    await intro_mess.add_reaction(EMOJI_RANDOM)


# search command
@risaBot.group(invoke_without_command=True)
async def search(ctx, *, message):
    query = message.strip()
    book_list =  utils.remove_banned_tags(
            list(h_utils.search_all_by_query(query,
            sort=Sort.Popular,
            progressbar=True
        )
    ))
    utils.save_search_data(query, book_list)
    data = utils.retrieve_search_data(f'Search results on "{query}"') 
    embed = RisaPaginatedEmbed(data, f'Search results on "{query}"')
    paginated_mess = await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
    for react in PAGINATED_MESSAGE_EMOJIS:
        await paginated_mess.add_reaction(react)

# download
@risaBot.command()
async def download(ctx, message):
    book = utils.get_source_by_id(message)
    if book:
        if not utils.check_for_banned_tags(book):
            embed = RisaDownloadEmbed(book)
            intro_mess = await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
            await intro_mess.add_reaction(EMOJI_WASTEBASKET)
        else:
            await ctx.send(
                BANNED_TAG_MSG,
                delete_after=SHORT_MSG_DELETE_TIMER
            )
    else:
        await ctx.send(
                NOT_EXIST_MSG,
                delete_after=SHORT_MSG_DELETE_TIMER
            )

@risaBot.command()
async def risa(ctx):
    embed = RisaEmbed()
    await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)

@risaBot.command()
async def help(ctx):
    embed = RisaHelpEmbed()
    await ctx.send(embed=embed)

risaBot.run(TOKEN)
