import discord
import random


def run_bot():
    TOKEN = 'MY_TOKEN'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is running!')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if message.content.startswith('!random') and message.author != client.user:
            random_messages = []
            async for msg in message.channel.history(limit=300):
                if msg.author != client.user:
                    random_messages.append(msg)
            if len(random_messages) > 0:
                global random_message
                random_message = random.choice(random_messages)
                if len(random_message.attachments) > 0:
                    attachment = random_message.attachments[0]
                    if attachment.is_spoiler:
                        await message.channel.send(f"Attachment was uploaded from local computer, it can't be sent again.")
                    else:
                        await message.channel.send(file=discord.File(attachment.url))
                else:
                    await message.channel.send(random_message.content)
        if message.content.startswith('!guess'):
            guess = str(message.content)
            answer = str(random_message.author)
            if guess[7:] == answer[:-5]:
                await message.channel.send('Correct!')
            else:
                await message.channel.send(f'Unlucky, go next. The answer is {answer[:-5]}')

    client.run(TOKEN) 