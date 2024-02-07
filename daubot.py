import discord
import config  # config.py contains a function getToken() that returns my private Discord bot token, not to be uploaded publicly
import daubotResponses
import asyncio

class DauBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} is online!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        print(f'{message.author}: {message.content} ({message.channel.name})')

        await self.respond_to_message(message)

    async def respond_to_message(self, message):
        response = daubotResponses.getResponse(message.content)
        if response:
            await message.channel.send(response)

async def main():
    TOKEN = config.getToken()
    if not TOKEN:
        raise ValueError("Token cannot be found. Please check your configuration.")

    intents = discord.Intents.default()
    intents.messages = True
    intents.message_content = True

    client = DauBot(intents=intents)
    await client.start(TOKEN)