import asyncio
import discord
from discord.ext.commands import Bot
import subprocess
import re
import os
import time
import sys
import threading
import keep_alive
keep_alive.keep_alive()
import keep_alive2
keep_alive2.run()

llIIIlIllllIllIIIlIIllII = os.getenv('llIIIlIllllIllIIIlIIllII')
bot = Bot(command_prefix='')
prefix = "epy"
val = 0
blacklist = []

def preventinfiniteloop():
  didthecommandwork = 0
  time.sleep(300)
  while True:
    time.sleep(1)
    if didthecommandwork == 0:
      try:
        os.execv(sys.executable, ['python'] + sys.argv)
        didthecommandwork = 1
      except:
        didthecommandwork = 0

startthefunctiontopreventinfiniteloop = threading.Thread(target=preventinfiniteloop)
startthefunctiontopreventinfiniteloop.start()

async def fdgvuydrgvytertv(message, message2):
  await message.channel.send(message2)

def sendMessage(message, message2):
  loop2 = asyncio.get_running_loop()
  loop2.run_until_complete(fdgvuydrgvytertv(message, message2))
  loop2.close()

def findcharlength(txtfile):
    with open(txtfile) as infile:
        words = 0
        characters = 0
        for lineno, line in enumerate(infile, 1):
            wordslist = line.split()
            words += len(wordslist)
            characters += sum(len(word) for word in wordslist)
    return characters

async def processCode(message):
  if llIIIlIllllIllIIIlIIllII in message.content:
    await message.channel.send("<@" + str(message.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message.content:
    await message.channel.send("<@" + str(message.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message.content:
    await message.channel.send("<@" + str(message.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message.content:
    await message.channel.send("<@" + str(message.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message.content:
    await message.channel.send("<@" + str(message.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message.channel.send("<@" + str(message.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message.channel.send("<@" + str(message.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message.cannel.send("<@" + str(message.author.id) + "> no response")
                  else:
                      sendMessage(message, "<@" + str(message.author.id) + ">")
                      sendMessage(message, std.stdout)
        else:
          await message.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message.channel.send("<@" + str(message.author.id) + "> no")

def start_loop(message):
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  loop.run_until_complete(processCode(message))
  loop.close()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
  if str(message.author.id) in blacklist:
    await message.delete()
  if message.author.bot:
    return
  if message.content == "test":
    await message.channel.send("python bot alive")

  if message.content.startswith(prefix):
    t = threading.Thread(target=start_loop, args=(message,))
    t.start()

bot.run(llIIIlIllllIllIIIlIIllII)
