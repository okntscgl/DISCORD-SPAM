import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix= "!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"{bot.user.name} successfully logged in!")

@bot.command
async def spam(ctx, target: discord.User, times: int, delay: float):
    await ctx.send(f"{target.name} will receive ' Kiss me ' {times} times.")

    for i in range(times):
        try:
            await target.send("Kiss me")
            await ctx.send(f" 'Kiss me' message sent to {target.name}.")
        except Exception as e:
            await ctx.send(f"Failed to send message: {e} ")
        await asyncio.sleep(delay)


@bot.command
async def channel_spam(ctx, channel: discord.TextChannel, times: int, delay: float):
    await ctx.send(f"'Kiss me' will be sent {times} times in the {channel.name} channel.")

    for i in range(times):
        try:
            await channel.send("Kiss me")
            await ctx.send(f"'Kiss me' message sent to the {channel.name} channel.")
        except Exception as e:
            await ctx.send(f"Failed to send message: {e}")
        await asyncio.sleep(delay)

bot.run("YOUR_TOKEN_HERE")
