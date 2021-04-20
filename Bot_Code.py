import discord
import os

from Dice_Roller_Function import roll

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower().startswith('$roll a '):
        msgContent = message.content[8:]
        await message.channel.send(max(roll(msgContent, True), roll(msgContent, True)))
        return
    
    if message.content.lower().startswith('$roll d '):
        msgContent = message.content[8:]
        await message.channel.send(min(roll(msgContent, True), roll(msgContent, True)))
        return

    if message.content.lower().startswith('$roll '):
        msgContent = message.content[6:]
        await message.channel.send(roll(msgContent, True))
        return

client.run('ODMzMDU0NzUyODQ5NjU3ODc2.YHswsg.FE2KVBTo9hJX6k3EFKMJoJJdeP4')
