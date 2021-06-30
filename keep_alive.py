import discord
import os
import colorama
from colorama import Fore, Style
import requests
import time
from colorama import Fore
from dotenv import load_dotenv
from keep_alive import keep_alive


message = "Your Message Here"


load_dotenv()
token = os.getenv('DISCORD_TOKEN')


b = Style.BRIGHT
print(f"""
{b+Fore.GREEN}
{b+Fore.BLUE} > {Fore.RESET}MASS DM v1
{b+Fore.BLUE} > {Fore.RESET}Support - Zityy#0001 Zityy#0002
{b+Fore.GREEN}
""")


massdmzityy = discord.Client()


@massdmzityy.event
async def on_connect():
  for user in massdmzityy.user.friends:
    try:
      await user.send(message)
      time.sleep(.1)
      print(f'Sent:' + Fore.GREEN + f' {user.name}')
    except:
       print(f"Failed: {user.name}")
       print(f"Messaged All Users!")

keep_alive()
massdmzityy.run(token, bot=False)
