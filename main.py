from typing import Final
import os

from discord.ext.commands import bot
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from morningMessages import get_morningmessage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord.ext import commands


#Load Token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

#Bot Setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


#Message funct.
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message empty because intents unabled)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


#Handling Startup
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


#Handle incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


#scheduled message i<3 stackoverflow
CHANNEL_ID = 1244750343334658108
USER_ID = 706742916004970506

async def func():
    c = client.get_channel(CHANNEL_ID)
    await c.send(get_morningmessage())

    print(USER_ID)
    me = await client.fetch_user(USER_ID)
    await me.send(get_morningmessage())
    #await c.send('Test123')

@client.event
async def on_ready():
    print("Ready")


    #initializing scheduler
    scheduler = AsyncIOScheduler()

    #sends "s!t" to the channel when time hits 10/20/30/40/50/60 seconds, like 12:04:20 PM
    scheduler.add_job(func, CronTrigger(hour="20", minute="43", second="20"))

    #starting the scheduler
    scheduler.start()




#Entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
