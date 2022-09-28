from venv import create
import interactions
from interactions import Button, ButtonStyle, CommandContext, SelectMenu, SelectOption, ActionRow, Modal, TextInput, TextStyleType, Embed
from interactions import (
    extension_listener,
    extension_component,
    Extension,
    Client,
    ComponentContext,
    Message,
    Channel,
    ChannelType,
    File,
    Member,
)

bot = interactions.Client("", intents=interactions.Intents.DEFAULT | interactions.Intents.GUILD_MESSAGES)

## Create Forum ##

@bot.command(name="sf", description="สแปม Forum ตึงๆ", scope=1023756261818376263, options=[
    interactions.Option(
            name="type_channels",
            description="ไอดีห้อง Forum",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    interactions.Option(
            name="type_amount",
            description="รายละเอียดโพส Forum",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
    interactions.Option(
            name="type_title",
            description="หัวข้อ Forum",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    interactions.Option(
            name="type_content",
            description="รายละเอียดโพส Forum",
            type=interactions.OptionType.STRING,
            required=True,
        ),
])

async def sf(ctx: interactions.CommandContext, type_channels: str, type_amount: int, type_title: str, type_content: str):
    await ctx.send("กำลังสแปม...")
    while True:
        forumChannel = await interactions.get(bot, interactions.Channel, object_id=type_channels)
        await forumChannel.create_forum_post(name=type_title, content=f"@everyone {type_content} \n ")

## Del Forum ##

@bot.command(name="sd", description="ลบ Forum ตึงๆ", scope=1023756261818376263, options=[
    interactions.Option(
            name="type_channels",
            description="ไอดีห้อง Forum",
            type=interactions.OptionType.INTEGER,
            required=True,
        ),
    interactions.Option(
            name="type_text",
            description="หัวข้อ Forum",
            type=interactions.OptionType.STRING,
            required=True,
        ),
])

async def sf(ctx: interactions.CommandContext, type_channels: int, type_text: str):
    await ctx.send("กำลังลบ...")
    forumChannel = await interactions.get(bot, interactions.Channel, object_id=1023942235806498898)
    await forumChannel.delete(name="Test", content="Test")

bot.start()
