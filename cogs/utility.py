import base64
import binascii
import collections
import string
import urllib.parse
import json
import random
import discord
from discord.ext import commands


naughty_list = ["akram09"]
class Utility(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # @commands.command(aliases=['purge'])
    # async def clear(self, ctx, amount):
    #     amount = int(amount)
    #     await ctx.message.delete()
        
    #     try:
    #         for amount in range(amount, 0, (- 100)):
    #             await ctx.channel.purge(limit=amount)
    #     except discord.errors.HTTPException:
    #         await ctx.send("Can't delete messages more than 14 days old!  Try a lower number.")

    @commands.command(aliases=['char'])
    async def characters(self, ctx, string):
        await ctx.send(len(string))

    @commands.command(aliases=['wc'])
    async def wordcount(self, ctx, *args):
        await ctx.send(len(args))

    @commands.command(aliases=['rev'])
    async def reverse(self, ctx, message):
        await ctx.send(message[::(- 1)])

    @commands.command()
    async def counteach(self, ctx, message):
        count = {}
        
        for char in message:
            if char in count.keys():
                count[char] += 1
            else:
                count[char] = 1
        
        await ctx.send(str(count))

    @commands.command(aliases=['head'])
    async def magicb(self, ctx, filetype):
        file = open('magic.json').read()
        alldata = json.loads(file)
        try:
            messy_signs = str(alldata[filetype]['signs'])
            signs = messy_signs.split('[')[1].split(',')[0].split(']')[0].replace("'", '')
            filetype = alldata[filetype]['mime']
            await ctx.send(f'''{filetype}: {signs}''')
        except: # if the filetype is not in magicb.json...
            await ctx.send(f"{filetype} not found :(  If you think this filetype should be included please do `!request \"magicb {filetype}\"`")

    @commands.command()
    async def twitter(self, ctx, twituser):
        await ctx.send('https://twitter.com/' + twituser)

    @commands.command()
    async def github(self, ctx, gituser):
        await ctx.send('https://github.com/' + gituser)

    @commands.command(aliases=['5050', 'flip'])
    async def cointoss(self, ctx):
        choice = random.randint(1, 2)
        
        if choice == 1:
            await ctx.send('heads')
        
        if choice == 2:
            await ctx.send('tails')

    @commands.command()
    async def add_swear(self, ctx, *new_swear):
        swear = " ".join(new_swear)
        if "#name#" not in swear:
            await ctx.channel.send('Can\'t find "#name#" in your ta3richa, check `!help utility`',tts=True)
            return 0
        swear = swear.replace('#name#','%s')
        try:
            with open('swears.json','r') as f:
                sw = json.load(f)
                f.close()
            sw["swears"].append(swear)
            with open('swears.json','w') as f:
                json.dump(sw ,f)
                f.close()
        except Exception as e:
            await ctx.channel.send('Ta3richa could not be saved!\nFor the reason:\n'+e,tts=True)
            return 0
        await ctx.channel.send('Ta3richa saved!',tts=True)

    @commands.command()
    async def arech(self, ctx, mate, number=1):
        try:
            with open('swears.json','r') as f:
                sw = json.load(f)['swears']
                f.close()
            authors_name = str(ctx.author)
            if any((name in authors_name for name in cool_names)):
                await ctx.channel.send(authors_name+' nta kharay matahkomch fiya', tts=True)
            if (int(number) > 10):
                await ctx.channel.send('bzzzfff na9es chwi!', tts=True)
            if 'akram' in mate:
                await ctx.channel.send('It\'s akram again!! I should call him KHARAY', tts=True)
                mate = 'KHARAY'
            else:
                for i in range(int(number)):
                    choice = random.choice(sw)
                    choice = choice % mate
                    await ctx.channel.send(choice, tts=True)
        except Exception as e:
            await ctx.channel.send('I can\'t ne3arech :(\nFor the reason:\n'+e,tts=True)

def setup(bot):
    bot.add_cog(Utility(bot))