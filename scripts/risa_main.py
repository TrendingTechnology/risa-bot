
from hentai import Hentai, Utils, Sort
from discord.ext import commands, tasks
from discord.flags import Intents
from risa_utils import RisaUtils
from risa_embeds import RisaPaginatedEmbed
from risa_embeds import RisaDownloadEmbed
from risa_embeds import RisaIntroEmbed
from risa_embeds import RisaReadEmbed
from risa_embeds import RisaHelpEmbed
from risa_embeds import RisaLoadEmbed
from risa_embeds import RisaEmbed
from risa_settings import *

risa_utils = RisaUtils()
h_utils = Utils()

risaBot = commands.Bot(
    command_prefix=PREFIX,
    case_insensitive=True,
    intents=Intents.all()
)
risaBot.remove_command('help')

@tasks.loop(hours=1)
async def get_updates():
    risa_utils.get_updates()


@risaBot.event
async def on_reaction_add(reaction, user):

    if reaction.emoji == EMOJI_BOOK and reaction.count > 1:
        embed = reaction.message.embeds[0]
        id = risa_utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        read_embed = RisaReadEmbed(obj)
        read_message = await reaction.message.channel.send(embed=read_embed)
        for react in READ_MESSAGE_EMOJIS:
            await read_message.add_reaction(react)

    elif reaction.emoji == EMOJI_FIRST_PAGE and reaction.count > 1:
        embed = reaction.message.embeds[0]
        id = risa_utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        page = 1
        read_embed = RisaReadEmbed(obj, index=page)
        read_message = await reaction.message.edit(embed=read_embed)

    elif reaction.emoji == EMOJI_LAST_PAGE and reaction.count > 1:
        embed = reaction.message.embeds[0]
        id = risa_utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        page = len(obj.pages)
        read_embed = RisaReadEmbed(obj, index=page)
        read_message = await reaction.message.edit(embed=read_embed)
    
    elif reaction.emoji == EMOJI_NEXT_PAGE and reaction.count > 1:
        embed = reaction.message.embeds[0]
        footer = embed.footer.text
        page = int(risa_utils.extract_curr_page_from_footer(footer)) + 1
        id = risa_utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        read_embed = RisaReadEmbed(obj, index=page)
        read_message = await reaction.message.edit(embed=read_embed)

    elif reaction.emoji == EMOJI_BACK_PAGE and reaction.count > 1:
        embed = reaction.message.embeds[0]
        footer = embed.footer.text
        page = int(risa_utils.extract_curr_page_from_footer(footer)) - 1
        id = risa_utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        read_embed = RisaReadEmbed(obj, index=page)
        read_message = await reaction.message.edit(embed=read_embed) 

    elif reaction.emoji == EMOJI_BACK_PAGE_ALT and reaction.count > 1:
        embed = reaction.message.embeds[0]
        title = embed.title
        footer = embed.footer.text
        page = int(risa_utils.extract_curr_page_from_footer(footer)) - 1

        if title == 'Popular Uploads':
            ref_name = 'Popular Uploads'
            data = risa_utils.popular

        elif title == 'Newest Uploads':
            ref_name = 'Newest Uploads'
            data = risa_utils.newest

        elif title.startswith("Search"):
            ref_name = title
            data = risa_utils.retrieve_search_data(title)

        book_list = risa_utils.remove_banned_tags(data)
        embed = RisaPaginatedEmbed(book_list, ref_name, index=page)
        await reaction.message.edit(embed=embed, delete_after=EMBED_DELETE_TIMER)

    elif reaction.emoji == EMOJI_NEXT_PAGE_ALT and reaction.count > 1:
        embed = reaction.message.embeds[0]
        title = embed.title
        footer = embed.footer.text
        page = int(risa_utils.extract_curr_page_from_footer(footer)) + 1

        if title == 'Popular Uploads':
            ref_name = 'Popular Uploads'
            data = risa_utils.popular

        elif title == 'Newest Uploads':
            ref_name = 'Newest Uploads'
            data = risa_utils.newest
        
        elif title.startswith("Search"):
            ref_name = title
            data = risa_utils.retrieve_search_data(title)

        book_list = risa_utils.remove_banned_tags(data)
        embed = RisaPaginatedEmbed(book_list, ref_name, index=page)
        await reaction.message.edit(embed=embed, delete_after=EMBED_DELETE_TIMER)

    elif reaction.emoji == EMOJI_BACK_PAGE_10 and reaction.count > 1:
        embed = reaction.message.embeds[0]
        title = embed.title
        footer = embed.footer.text
        page = int(risa_utils.extract_curr_page_from_footer(footer)) - 10

        if title == 'Popular Uploads':
            ref_name = 'Popular Uploads'
            data = risa_utils.popular

        elif title == 'Newest Uploads':
            ref_name = 'Newest Uploads'
            data = risa_utils.newest

        elif title.startswith("Search"):
            ref_name = title
            data = risa_utils.retrieve_search_data(title)

        book_list = risa_utils.remove_banned_tags(data)
        embed = RisaPaginatedEmbed(book_list, ref_name, index=page)
        await reaction.message.edit(embed=embed, delete_after=EMBED_DELETE_TIMER)

    elif reaction.emoji == EMOJI_NEXT_PAGE_10 and reaction.count > 1:
        embed = reaction.message.embeds[0]
        title = embed.title
        footer = embed.footer.text
        page = int(risa_utils.extract_curr_page_from_footer(footer)) + 10

        if title == 'Popular Uploads':
            ref_name = 'Popular Uploads'
            data = risa_utils.popular

        elif title == 'Newest Uploads':
            ref_name = 'Newest Uploads'
            data = risa_utils.newest

        elif title.startswith("Search"):
            ref_name = title
            data = risa_utils.retrieve_search_data(title)

        book_list = risa_utils.remove_banned_tags(data)
        embed = RisaPaginatedEmbed(book_list, ref_name, index=page)
        await reaction.message.edit(embed=embed, delete_after=EMBED_DELETE_TIMER)

    elif reaction.emoji == EMOJI_BOOK_GET and reaction.count > 1:
        embed = reaction.message.embeds[0]
        id = risa_utils.extract_url_from_descrip(embed.description)
        obj = Hentai(id)
        embed = RisaIntroEmbed(obj)
        intro_mess = await reaction.message.channel.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
        for react in INTRO_MESSAGE_EMOJIS:
            await intro_mess.add_reaction(react)

    elif reaction.emoji == EMOJI_RANDOM and reaction.count > 1:
        embed = reaction.message.embeds[0]
        obj = risa_utils.get_safe_source()
        embed = RisaIntroEmbed(obj)
        intro_mess = await reaction.message.edit(embed=embed, delete_after=EMBED_DELETE_TIMER)

    elif reaction.emoji == EMOJI_DOWNLOAD and reaction.count > 1:
        embed = reaction.message.embeds[0]
        id = risa_utils.extract_url_from_descrip(embed.description)
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
@risaBot.group(
    invoke_without_command=True,
    case_insensitive=True,
    aliases=READ_ALIASES
)
async def read(ctx, message):
    book = risa_utils.get_source_by_id(message)
    if book:
        if not risa_utils.check_for_banned_tags(book):
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
@read.command(
    case_insensitive=True,
    aliases=POPULAR_ALIASES
)
async def popular(ctx):
    book_list = risa_utils.remove_banned_tags(risa_utils.popular)
    embed = RisaPaginatedEmbed(book_list, 'Popular Uploads')
    paginated_mess = await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
    for react in PAGINATED_MESSAGE_EMOJIS:
        await paginated_mess.add_reaction(react)


# newest command
@read.command(
    case_insensitive=True,
    aliases=NEWEST_ALIASES
)
async def newest(ctx):
    book_list = risa_utils.remove_banned_tags(risa_utils.newest)
    embed = RisaPaginatedEmbed(book_list, 'Newest Uploads')
    paginated_mess = await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
    for react in PAGINATED_MESSAGE_EMOJIS:
        await paginated_mess.add_reaction(react)


# random command
@read.command(
    case_insensitive=True,
    aliases=RANDOM_ALIASES
)
async def random(ctx):
    book = risa_utils.get_safe_source()
    embed = RisaIntroEmbed(book)
    intro_mess = await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)
    for react in INTRO_MESSAGE_EMOJIS:
        await intro_mess.add_reaction(react)
    await intro_mess.add_reaction(EMOJI_RANDOM)

# search command
@risaBot.group(
    invoke_without_command=True,
    case_insensitive=True,
    aliases=SEARCH_ALIASES
)
async def search(ctx, *, message):
    query = message.strip()
    if not risa_utils.check_query(query):
        embed = RisaLoadEmbed(LOAD_GIF_URL, LOAD_MSG)
        paginated_mess = await ctx.send(embed=embed)
        book_list = list(h_utils.search_all_by_query(query + risa_utils.query_filter(BANNED_TAGS),
                    sort=Sort.PopularWeek,
                    progressbar=True
                )
            )
        print(query + risa_utils.query_filter(BANNED_TAGS))
        if book_list != []:
            risa_utils.save_search_data(query, book_list)
            data = risa_utils.retrieve_search_data(f'Search results on `{query}`') 
            embed = RisaPaginatedEmbed(data, f'Search results on `{query}`')
            await paginated_mess.edit(embed=embed, delete_after=EMBED_DELETE_TIMER)
            for react in PAGINATED_MESSAGE_EMOJIS:
                await paginated_mess.add_reaction(react)
        else:
            embed = RisaLoadEmbed(NO_RESULT_GIF_URL, NO_RESULT_MSG)
            await paginated_mess.edit(embed=embed, delete_after=5)
    else:
        await ctx.send(BANNED_TAG_MSG, delete_after=SHORT_MSG_DELETE_TIMER)

# download
@risaBot.command(
    case_insensitive=True,
    aliases=DOWNLOAD_ALIASES
)
async def download(ctx, message):
    book = risa_utils.get_source_by_id(message)
    if book:
        if not risa_utils.check_for_banned_tags(book):
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

# help command
@risaBot.command(
    case_insensitive=True
)
async def help(ctx):
    embed = RisaHelpEmbed()
    await ctx.send(embed=embed)

# misc commands
@risaBot.command(
    case_insensitive=True
)
async def risa(ctx):
    embed = RisaEmbed()
    await ctx.send(embed=embed, delete_after=EMBED_DELETE_TIMER)

risaBot.run(TOKEN)
