import discord
import json

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

MESSAGE_ID = config["message_id"]
CHANNEL_ID = config["channel_id"]
TOKEN = config["token"]

@client.event
async def on_ready():
    print('Bot is logged in.')
    try:
        channel = client.get_channel(CHANNEL_ID)
        message = await channel.fetch_message(MESSAGE_ID)
        await message.add_reaction("1️⃣")
        await message.add_reaction("2️⃣")
        print('Reactions added to the message.')
    except Exception as e:
        print(f'Error adding reactions: {e}')


@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == MESSAGE_ID:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name =="1️⃣":
            role = discord.utils.get(guild.roles, name='Master 1')
        elif payload.emoji.name =="2️⃣":
            role = discord.utils.get(guild.roles, name='Master 2')
        else:
            print("KO")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 1146377506446901290:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name =="1️⃣":
            role = discord.utils.get(guild.roles, name='Master 1')
        elif payload.emoji.name =="2️⃣":
            role = discord.utils.get(guild.roles, name='Master 2')
        else:
            print("KO")
        if role is not None:
            member = discord.utils.find(lambda m: m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)
                

                                   
client.run(TOKEN)