import discord
import responses
import random


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    
    except Exception as e:
        print(e)


def run_bot():
    TOKEN = 'MTA2Mjg4NzE4NjIwNDIwNTA5Ng.GIJbJs.uWit6mkIbwIMCavyjw6iWURZVMgbx0NHaDy3sQ'
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

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

        #if user_message[]

        if message.content.startswith("!random") and message.author != client.user:
            random_messages = []
            async for msg in message.channel.history(limit=300):
                if msg.author != client.user:
                    random_messages.append(msg)
            if len(random_messages) > 0:
                random_message = random.choice(random_messages)
                if len(random_message.attachments) > 0:
                    attachment = random_message.attachments[0]
                    if attachment.is_spoiler:
                        await message.channel.send(f"Attachment was uploaded from local computer, it can't be sent again.")
                    else:
                        await message.channel.send(file=discord.File(attachment.url))
                else:
                    await message.channel.send(random_message.content)
            else:
                await message.channel.send("No messages found")

    '''    
    async def get_random_message(channel, limit):
        random_messages = []
        last_message_timestamp = None
        while len(random_messages) < limit:
            messages = await channel.history(limit=min(limit, 100), before=last_message_timestamp).flatten()
            messages = [m for m in messages if m.author != client.user]
            random_messages.extend(messages)
            last_message_timestamp = messages[-1].created_at
        return random.choice(random_messages)

    @client.event
    async def on_message(message):
        if message.content.startswith("!random") and message.author != client.user:
            try:
                limit = int(message.content.split(" ")[1])
            except (IndexError, ValueError):
                limit = 100
            random_message = await get_random_message(message.channel, limit)
            if len(random_message.attachments) > 0:
                attachment = random_message.attachments[0]
                if attachment.is_spoiler:
                    await message.channel.send(f"Attachment was uploaded from local computer, it can't be sent again.")
                else:
                    await message.channel.send(file=discord.File(attachment.url))
            else:
                await message.channel.send(random_message.content)
        '''


    client.run(TOKEN)
