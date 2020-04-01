import discord
import os

#port = int(os.environ.get('PORT', 5000))

client = discord.Client()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$$hello'):
            await message.channel.send('Hello {0.author.mention}'.format(message))

client.run('NjQwMTA0OTg3MDY1NTgxNTgz.XoSLnA.Vvi-bg_SgiOQL60sl2GW0e5hSQ0')
