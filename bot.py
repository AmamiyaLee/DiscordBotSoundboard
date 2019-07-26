import discord
from discord.ext import commands
import asyncio

TOKEN='NjAzODQyMzc5NzY5ODM5NjIx.XTrcNQ.xKj2AB1WWIapA_jjPaNOvucDLgY'

bot = commands.Bot(command_prefix='')
@bot.command(name='<:PIN:601452935091847199>')
async def missing (ctx):  
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio('ping_missing.mp3'))
    ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)

@bot.command(name='<:NOTNOW:569890140575629313>')
async def not_now (ctx):  
    #source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(''))
    #ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
    await ctx.send('先不要')
'''
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
'''
@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()
    print('Bot joined the channel.')
@bot.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()
@bot.event
async def on_ready():
    print('Logged in as',bot.user.name)
    '''
@bot.listen()
async def on_message(message):
    
    if message.content.startswith(':howdy'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel,msg)
        '''
bot.run(TOKEN)

