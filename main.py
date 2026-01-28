import os
import psutil
import shutil
import discord
from discord.ext import commands
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable not set!")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

def bytes_to_gb(b):
    return round(b / (1024 ** 3), 2)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command(name="specs")
async def specs(ctx):
    vcpu = os.cpu_count()
    vm = psutil.virtual_memory()
    ram_total = bytes_to_gb(vm.total)
    ram_used = bytes_to_gb(vm.used)
    du = shutil.disk_usage("/")
    disk_total = bytes_to_gb(du.total)
    disk_used = bytes_to_gb(du.used)

    msg = (
        f"**Host Specs**\n"
        f"- vCPU: `{vcpu}`\n"
        f"- RAM: `{ram_used} / {ram_total} GB`\n"
        f"- Disk: `{disk_used} / {disk_total} GB`"
    )
    await ctx.send(msg)

bot.run(TOKEN)
