from discord.ext import commands
import discord
import json
import sys
import traceback

with open('config.json') as f:
    json_data = json.load(f)

def get_prefix(bot, message):
    if not message.guild:
        pass
    return commands.when_mentioned_or(get_prefix)(bot, message)

prefixes = json_data['pref']
bot = commands.Bot(command_prefix=prefixes)
token = json_data['token']

initial_extensions =[
        'cogs.music'
    ]

for extension in initial_extensions:
            try:
                bot.load_extension(extension)
            except Exception as e:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()

@bot.event
async def on_ready():
    print("Starting..")
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("Discord.py"))    
    print("Startup successful.")
bot.run(token, bot=True, reconnect=True)
