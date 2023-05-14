import asyncio, discord

bot = discord.Client()

token = 'Your bot token'

@bot.event
async def on_ready():
    print(f"Login: {bot.user}\nInvite Link: https://discord.com/oauth2/authorize?bot_id={bot.user.id}&permissions=8&scope=bot")
    while True:
        await bot.change_presence(activity=discord.Game(f"SPAM LINK KILLER | {len(bot.guilds)}서버 사용중"),status=discord.Status.online)
        await asyncio.sleep(3)

@bot.event
async def on_message_edit(before, after):
    if before.author.bot:
        return
    else:
        if "https://discord.gg" in after.content.lower() or "http://discord.gg" in after.content.lower() or "discord.gg" in after.content.lower() or "https://discord.com/invite" in after.content.lower() or "http://discord.com/invite" in after.content.lower() or "discord.com/invite" in after.content.lower():
            if not after.author.guild_permissions.administrator:
                await after.delete()
                
                try:
                    await after.author.kick()
                except Exception:
                    pass



@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if "https://discord.gg" in message.content.lower() or "http://discord.gg" in message.content.lower() or "discord.gg" in message.content.lower() or "https://discord.com/invite" in message.content.lower() or "http://discord.com/invite" in message.content.lower() or "discord.com/invite" in message.content.lower():
        if not message.author.guild_permissions.administrator:
            await message.delete()
            
            try:
                await message.author.kick()
            except:
                pass

bot.run(token)
