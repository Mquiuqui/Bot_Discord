import discord
import os
from discord.ext import commands
import random
import time
from random import randint
from dotenv import load_dotenv
import youtube_dl
from discord import FFmpegAudio
from lol import buscar_contato,enviar_mensagem


voice = None

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix=">", case_insensitive = True)

@client.event
async def on_ready():
    print('Entramos como {0.user}' .format(client))
    

@client.command()
async def Ola(oi):
    await oi.send(f"Oi, {oi.author} meu amor sz")
    return

@client.command()
async def Baka(baka):
    await baka.send("b-baka :point_right: :point_left: ")
    return
@client.command()
async def LG(lg):
    embed = discord.Embed(title="LG?", color=0xfc7eee)
    embed.add_field(name="LG:", value=("\n>LG \n>LG \n>LG \n>LG \n>LG \nLG" ))
    await lg.send(embed=embed)
    return

@client.command()
async def lol(lol , *nicks):
    print(nicks)
    buscar_contato(nicks)
    conta = enviar_mensagem()
    embed = discord.Embed(title="ULTIMA PARTIDA", color=0xfc7eee ) #,color=Hex code
    embed.add_field(name=nicks[0], value=(f"\nCHAMPION : {conta[0]}\nMODO : {conta[1]}\nDURAÇÃO : {conta[2]}\nRESULTADO : {conta[3]}\nKDA : {conta[4]} / {conta[5]} / {conta[6]}"))
    await lol.send(embed=embed)
    return

@client.command()
async def Ajuda(ctxx):
    embed = discord.Embed(title="QUER AJUDA PUTA?", color=0xfc7eee)
    embed.add_field(name="COMANDOS:", value=("\nAjuda - não vou perder meu tempo pra explicar né \nOi - Para carentes \nLol - para ver a ultima partida no histórico do OP.GG. \nUepa - RRRRRRRAAATINHOOOO! \nRogers - ffffffiUUUUUUUUUUUU... POW \nDigas - é o digas rs" ))
    await ctxx.send(embed=embed)
    return

#TESTES PARA FUNÇÃO PLAY MUSIC

@client.command()
async def uepa(uepa):
    channel = uepa.author.voice.channel
    await uepa.send("UEEEEPA!")
    global voice
    try:   
        voice = await channel.connect() # use the channel object you put into a variable
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/uepa.mp3"))

    except:
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/uepa.mp3"))
    return


@client.command()
async def rogers(rogers):
        # Gets voice channel of message author
    channel = rogers.author.voice.channel
    await rogers.send("Rogers!")
    global voice
    try:   
        voice = await channel.connect() # use the channel object you put into a variable
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/rojao.mp3"))
        dir(voice)
    except:
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/rojao.mp3"))
    return


@client.command()
async def Digas(digas):
    await digas.send(file = discord.File("MEMES/0.jpeg"))
        # Gets voice channel of message author
    channel = digas.author.voice.channel
    global voice
    try:   
        voice = await channel.connect() # use the channel object you put into a variable
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/yamete.mp3"))
        dir(voice)
    except:
        voice.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:/yamete.mp3"))
    return


@client.command()
async def disco(disco):
    global voice
    await voice.disconnect() # use the channel object you put into a variable
    return


@client.command()
async def dado(rando1):
 
    res = random.randint(1,4)

    await rando1.send(res)

    return
client.run(TOKEN)  


'''  
    channel = ctx.author.voice.channel
    voice = await channel.connect() # use the channel object you put into a variable
    source = FFmpegAudio('uepa.mp3')
    player = voice.play(source)
'''

'''
@client.command()
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()
'''
   


