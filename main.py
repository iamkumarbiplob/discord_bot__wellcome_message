import discord
import asyncio
from discord.ext import commands

intents = discord.Intents()
intents.members = True

TOKEN = 'Token'
bot=commands.Bot(command_prefix='!',intents=intents)

#Events
@bot.event
async def on_member_join(member):
    message=f"""Hello {member.mention}! \nWelcome to ***Decentralized Brains*** https://decentralizedbrains.com/,\nHere we work on several markets in the Blockchain, NFT's and Web3 sectors. \n\n"""+\
            """You must pass a test to demonstrate your skill and resolve before you are allowed to join our team.\n\n"""+\
            """ Here is what you need to do right away:"""+\
            """```fix\n1. Provide your CV in the server channel called #cv-github-website.```"""+\
            """```fix\n2. Include a link of your github profile so that we may view your projects and experience.```"""+\
            """```fix\n3. Describe the position you would like to have, such as front-end developer, back-end developer, or UI/UX designer.```\n"""+\
            """Best Wishes!\n\n"""+\
            """~~This is an auto generated bot message. Don't Reply here.~~"""
    message2=f"""If you have any problem or query don't hesitate to contact Biplob Kumar (iamkumarbiplob#6357) or Rashid Shahriar (10KNOOB#3619) through Discord App ."""
    message3=f"""The best time for a new beginning is right now. Good luck on your new journey"""
    await member.send(f"{message}")
    await asyncio.sleep(5)
    await member.send(f"{message2}")
    await asyncio.sleep(5)
    await member.send(f"{message3}")
    print(f"{member.name} -Join the Decentralized Brains server.")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

bot.run(TOKEN)


