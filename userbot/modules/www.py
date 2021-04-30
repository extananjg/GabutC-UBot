# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

from datetime import datetime

from speedtest import Speedtest
from userbot import CMD_HELP, StartTime, ALIVE_NAME
from userbot.events import register
import time


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern="^.sping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**★ xᴛᴀᴀ ★**")
    await pong.edit("**★✫ ꜰᴏᴜɴᴅᴛᴀᴀ ★✫**")
    await pong.edit("**★✫★ Ping ★✫★**")
    await pong.edit("**★✫★✫ Pong ★✫★✫**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**❅ xᴛᴀᴀɴᴊᴋɴᴛʟ♆ ** "
                    f"\n  ➥ `%sms` \n"
                    f"**❅ ₄₀₄ 𝖊𝖗𝖗𝖔𝖗,𝖓𝖔𝖙 𝖋𝖔𝖚𝖓𝖉〄 ** "
                    f"\n  ➥ `{ALIVE_NAME}` \n" % (duration))


@register(outgoing=True, pattern="^.lping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Love Ping..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**✣ PONG!**\n"
                    f"𐛐 **Ping:** "
                    f"`%sms` \n"
                    f"𐛐 **Uptime:** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.xping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Ping..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**NGENTOD:v**\n"
                    f"➠ **Astagfirullah:** "
                    f"`%sms` \n"
                    f"➠ **Mantap sekali:**"
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.gabutping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Bos Ping..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**☻ 𝖝𝖙𝖆𝖆 Ping!!!**\n"
                    f"☻ **Ping:** "
                    f"`%sms` \n"
                    f"☻ **Uptime:** "
                    f"`{uptime}` \n"
                    f"🐣 **My Enemy:v** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern="^.speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Tinggi...🚀`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Hasil Tes:\n**"
                   "✓ **Dimulai Pada:** "
                   f"`{result['timestamp']}` \n"
                   "✓ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✓ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✓ **Ping:** "
                   f"`{result['ping']}` \n"
                   "✓ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   "✓ **BOT:** ` GabutC-UBot`")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Apa Sih KNTL?..............`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"** Halah Ngentod!!! **\n**Air Mani :** %sms\n**Bot Uptime  :** {uptime} ⏱" % (duration))


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("`Pong.....🔌`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit("🌻 **Apa anjing? **\n`%sms`" % (duration))

CMD_HELP.update(
    {"ping": "`.ping` ; `.lping` ; `.xping` ; `.sping`\
    \nUsage: Untuk menunjukkan ping bot.\
    \n\n`.speed`\
    \nUsage: Untuk menunjukkan kecepatan.\
    \n\n`.pong`\
    \nUsage: sama kaya perintah ping."
     })
