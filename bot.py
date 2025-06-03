import discord
from discord.ext import commands
import os

# Botの設定
intents = discord.Intents.default()
intents.message_content = True
intents.guild_messages = True
intents.dm_messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Botが起動したときに実行されるイベント
@bot.event
async def on_ready():
    print(f'Bot {bot.user} が起動しました！')

# テストコマンド
@bot.command()
async def hello(ctx):
    await ctx.send('こんにちは！')

# メッセージを受信したときに実行されるイベント
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'こんにちは':
        await message.channel.send('こんにちは！')

    await bot.process_commands(message)

# Botを起動
if __name__ == '__main__':
    # トークンを直接設定
    token = "MTM3OTI3NTk2MDQ0ODMyMzU5NA.Ge7_Yt.szb1JN4vGot4774dYRRImVmGbb3Q6Lf2sTuX3w"
    bot.run(token)
