import discord
import os

port = int(os.environ.get('PORT', 5000))

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
        elif message.content.startswith('$$about'):
            await message.channel.send('This bot was made by Conner Black for the purposes of Stock Trading. Any questions about it must be dmed to {0.ConnerBlack.mention}'.format(message))
            

client.run('NjQwMTA0OTg3MDY1NTgxNTgz.XoSBbg.VW3b3Zh_0nKsrOu-4FZtRgGSGvE')
