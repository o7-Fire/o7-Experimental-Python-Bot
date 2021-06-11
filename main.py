import asyncio
import discord
from discord.ext.commands import Bot
import subprocess
import re
import os
import time
import sys
import random
import threading
from discord.ext import tasks
import keep_alive
keep_alive.keep_alive()
#import keep_alive2
#keep_alive2.run()

message2 = ""
activeornot1 = False
activeornot2 = False
activeornot3 = False
activeornot4 = False
activeornot5 = False
activeornot6 = False
activeornot7 = False
activeornot8 = False
activeornot9 = False
activeornot10 = False
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

#async def fdgvuydrgvytertv(message, message2):
  #await message.channel.send(message2)

#def sendMessage(message, message2):
  #loop2 = asyncio.get_running_loop()
  #asyncio.ensure_future(fdgvuydrgvytertv(message, message2))

def findcharlength(txtfile):
    with open(txtfile) as infile:
        words = 0
        characters = 0
        for lineno, line in enumerate(infile, 1):
            wordslist = line.split()
            words += len(wordslist)
            characters += sum(len(word) for word in wordslist)
    return characters

@tasks.loop(seconds = 0.1)
async def processCode1():
  global message2
  global activeornot1
  if activeornot1 == False:
    return
  activeornot1 = False
  if llIIIlIllllIllIIIlIIllII in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message2.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message2.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message2.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message2.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message2.channel.send("<@" + str(message2.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message2.cannel.send("<@" + str(message2.author.id) + "> no response")
                  else:
                      await message2.channel.send("<@" + str(message2.author.id) + ">")
                      await message2.channel.send(std.stdout)
        else:
          await message2.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message2.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message2.channel.send("<@" + str(message2.author.id) + "> no")


@tasks.loop(seconds = 0.1)
async def processCode2():
  global message2
  global activeornot2
  if activeornot2 == False:
    return
  activeornot2 = False
  if llIIIlIllllIllIIIlIIllII in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message2.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message2.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message2.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message2.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message2.channel.send("<@" + str(message2.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message2.cannel.send("<@" + str(message2.author.id) + "> no response")
                  else:
                      await message2.channel.send("<@" + str(message2.author.id) + ">")
                      await message2.channel.send(std.stdout)
        else:
          await message2.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message2.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message2.channel.send("<@" + str(message2.author.id) + "> no")


@tasks.loop(seconds = 0.1)
async def processCode3():
  global message2
  global activeornot3
  if activeornot3 == False:
    return
  activeornot3 = False
  if llIIIlIllllIllIIIlIIllII in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message2.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message2.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message2.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message2.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message2.channel.send("<@" + str(message2.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message2.cannel.send("<@" + str(message2.author.id) + "> no response")
                  else:
                      await message2.channel.send("<@" + str(message2.author.id) + ">")
                      await message2.channel.send(std.stdout)
        else:
          await message2.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message2.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message2.channel.send("<@" + str(message2.author.id) + "> no")

@tasks.loop(seconds = 0.1)
async def processCode4():
  global message2
  global activeornot4
  if activeornot4 == False:
    return
  activeornot4 = False
  if llIIIlIllllIllIIIlIIllII in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message2.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message2.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message2.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message2.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message2.channel.send("<@" + str(message2.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message2.cannel.send("<@" + str(message2.author.id) + "> no response")
                  else:
                      await message2.channel.send("<@" + str(message2.author.id) + ">")
                      await message2.channel.send(std.stdout)
        else:
          await message2.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message2.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message2.channel.send("<@" + str(message2.author.id) + "> no")

@tasks.loop(seconds = 0.1)
async def processCode5():
  global message2
  global activeornot5
  if activeornot5 == False:
    return
  activeornot5 = False
  if llIIIlIllllIllIIIlIIllII in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message2.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message2.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message2.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message2.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message2.channel.send("<@" + str(message2.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message2.cannel.send("<@" + str(message2.author.id) + "> no response")
                  else:
                      await message2.channel.send("<@" + str(message2.author.id) + ">")
                      await message2.channel.send(std.stdout)
        else:
          await message2.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message2.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message2.channel.send("<@" + str(message2.author.id) + "> no")

@tasks.loop(seconds = 0.1)
async def processCode6():
  global message2
  global activeornot6
  if activeornot6 == False:
    return
  activeornot6 = False
  if llIIIlIllllIllIIIlIIllII in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message2.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message2.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message2.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message2.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message2.channel.send("<@" + str(message2.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message2.cannel.send("<@" + str(message2.author.id) + "> no response")
                  else:
                      await message2.channel.send("<@" + str(message2.author.id) + ">")
                      await message2.channel.send(std.stdout)
        else:
          await message2.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message2.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message2.channel.send("<@" + str(message2.author.id) + "> no")

@tasks.loop(seconds = 0.1)
async def processCode7():
  global message2
  global activeornot7
  if activeornot7 == False:
    return
  activeornot7 = False
  if llIIIlIllllIllIIIlIIllII in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message2.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message2.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message2.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message2.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message2.channel.send("<@" + str(message2.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message2.cannel.send("<@" + str(message2.author.id) + "> no response")
                  else:
                      await message2.channel.send("<@" + str(message2.author.id) + ">")
                      await message2.channel.send(std.stdout)
        else:
          await message2.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message2.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message2.channel.send("<@" + str(message2.author.id) + "> no")

@tasks.loop(seconds = 0.1)
async def processCode8():
  global message2
  global activeornot8
  if activeornot8 == False:
    return
  activeornot8 = False
  if llIIIlIllllIllIIIlIIllII in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message2.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message2.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message2.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message2.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message2.channel.send("<@" + str(message2.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message2.cannel.send("<@" + str(message2.author.id) + "> no response")
                  else:
                      await message2.channel.send("<@" + str(message2.author.id) + ">")
                      await message2.channel.send(std.stdout)
        else:
          await message2.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message2.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message2.channel.send("<@" + str(message2.author.id) + "> no")

@tasks.loop(seconds = 0.1)
async def processCode9():
  global message2
  global activeornot9
  if activeornot9 == False:
    return
  activeornot9 = False
  if llIIIlIllllIllIIIlIIllII in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message2.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message2.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message2.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message2.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message2.channel.send("<@" + str(message2.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message2.cannel.send("<@" + str(message2.author.id) + "> no response")
                  else:
                      await message2.channel.send("<@" + str(message2.author.id) + ">")
                      await message2.channel.send(std.stdout)
        else:
          await message2.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message2.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message2.channel.send("<@" + str(message2.author.id) + "> no")

@tasks.loop(seconds = 0.1)
async def processCode10():
  global message2
  global activeornot10
  if activeornot10 == False:
    return
  activeornot10 = False
  if llIIIlIllllIllIIIlIIllII in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
    return
  if "netsh" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
    return
  if "zipbomb" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
    return
  if "@everyone" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
    return
  if "@here" in message2.content:
    await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
    return
  if 1 == 1:
    file_object  = open("pee.py", "w+")
    removedpy = message2.content.replace(prefix, "", 1)
    calc = [m.start() for m in re.finditer("input()", removedpy)]
    for i in range(len(calc)):
        try:
            await message2.channel.send("input:")
            msg = await bot.wait_for("message", timeout=30)  # 30 seconds to reply
            removedpy = removedpy.replace("input()", str(msg.content), 1)
        except asyncio.TimeoutError:
            await message2.channel.send("Sorry, you didn't reply in time!")
            return
    file_object.write("import os\nos.environ['llIIIlIllllIllIIIlIIllII'] = 'a'\n" + removedpy)
    file_object.close()
    std = subprocess.run(['python', 'pee.py'], capture_output=True, text=True)
    os.remove("pee.py")
    if llIIIlIllllIllIIIlIIllII in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 0 (message contains bot token)")
        return
    if "netsh" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 1 (message contains netsh)")
        return
    if "zipbomb" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 2 (message contains zipbomb)")
        return
    if "@everyone" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 3 (message contains @ everyone)")
        return
    if "@here" in std.stdout:
        await message2.channel.send("<@" + str(message2.author.id) + "> lmao no 4 (message contains @ here)")
        return
    else:
        if not std.stderr:
            if val == 1:
                with open('assad.txt', 'w') as file:
                    file.write(std.stdout)
                with open('assad.txt', 'r') as file:
                    msg = file.read(2000).strip()
                    while len(msg) > 0:
                        await message2.channel.send(msg)
                        msg = file.read(2000).strip()
            else:
                  if len(std.stdout) >= 2000:
                      with open("result.txt", "w") as file:
                          file.write(std.stdout)
                      with open("result.txt", "rb") as file:
                          await message2.channel.send("<@" + str(message2.author.id) + "> Your file is:", file=discord.File(file, "result.txt"))
                  elif std.stdout == None:
                      await message2.cannel.send("<@" + str(message2.author.id) + "> no response")
                  else:
                      await message2.channel.send("<@" + str(message2.author.id) + ">")
                      await message2.channel.send(std.stdout)
        else:
          await message2.channel.send("Discord Error - " + str("none yet because nexity lazy") + '\n')
          await message2.channel.send("Tracebacks:\n " + str(std.stderr))
  else:
    await message2.channel.send("<@" + str(message2.author.id) + "> no")

#def start_loop(message):
#  loop = asyncio.new_event_loop()
#  asyncio.set_event_loop(loop)
#  loop.run_until_complete(processCode(message))
#  loop.close()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

processCode1.start()
processCode2.start()
processCode3.start()
processCode4.start()
processCode5.start()
processCode6.start()
processCode7.start()
processCode8.start()
processCode9.start()
processCode10.start()

def changeactive(i):
  global activeornot1, activeornot2, activeornot3, activeornot4, activeornot5, activeornot6, activeornot7, activeornot8, activeornot9, activeornot10
  if i == 1:
    activeornot1 = True
  elif i == 2:
    activeornot2 = True
  elif i == 3:
    activeornot3 = True
  elif i == 4:
    activeornot4 = True
  elif i == 5:
    activeornot5 = True
  elif i == 6:
    activeornot6 = True
  elif i == 7:
    activeornot7 = True
  elif i == 8:
    activeornot8 = True
  elif i == 9:
    activeornot9 = True
  elif i == 10:
    activeornot10 = True

@bot.event
async def on_message(message):
  global message2
  if str(message.author.id) in blacklist:
    await message.delete()
  if message.author.bot:
    return
  if message.content == "test":
    await message.channel.send("python bot alive")

  if message.content.startswith(prefix):
    #t = threading.Thread(target=start_loop, args=(message,))
    #t.start()
    message2 = message
    changeactive(random.randint(1, 10))

bot.run(llIIIlIllllIllIIIlIIllII)
