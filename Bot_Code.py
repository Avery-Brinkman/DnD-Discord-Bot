import discord
import os

from Dice_Roller_Function import *
from Character_Sheet import *

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('$roll '):
        msgContent = message.content[6:]
        await message.channel.send(roll(msgContent, True))

    if message.content.lower().startswith('$setchar '):
        charName = message.content[9:]
        await message.channel.send('Character set to ' + charName)

    if message.content.lower().startswith('$ability '):
        msgContent = message.content[9:]
        
        try: charName
        except: await message.channel.send('No character set!')

        await message.channel.send(abilityRoll(msgContent, charName))

client.run('ODMzMDU0NzUyODQ5NjU3ODc2.YHswsg.FE2KVBTo9hJX6k3EFKMJoJJdeP4')
