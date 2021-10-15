@Client.on_message(
    command(["game", f"game@{BOT_USERNAME}"])
    & ~filters.edited
    & ~filters.bot
    & ~filters.private
)
@authorized_users_only
async def music_onoff(_, message):
    global que
    global useer
    await message.delete()
    global DISABLED_GROUPS
    try:
        message.from_user.id
    except:
        return
    if len(message.command) != 2:
        await message.delete()
        await message.reply_text(
            "**i'm only know** `/game on` **and** `/game off`"
        )
        return
    status = message.text.split(None, 1)[1]
    message.chat.id
    if status == "ON" or status == "on" or status == "On":
        lel = await message.reply("`processing...`")
        if not message.chat.id in DISABLED_GROUPS:
            await lel.edit("» **game already turned on.**")
            return
        DISABLED_GROUPS.remove(message.chat.id)
        await lel.edit(f"✅ **game turned on**\n\n💬 `{message.chat.id}`")

    elif status == "OFF" or status == "off" or status == "Off":
        lel = await message.reply("`processing...`")

        if message.chat.id in DISABLED_GROUPS:
            await lel.edit("» **game already turned off.**")
            return
        DISABLED_GROUPS.append(message.chat.id)
        await lel.edit(f"✅ **game turned off**\n\n💬 `{message.chat.id}`")
    else:
        await message.reply_text(
            "**i'm only know** `/game on` **and** `/game off`"
        )

from telethon.tl.types import InputMediaDice

from LaylaRobot.events import register


@register(pattern="^/dicee(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice(""))
    input_int = int(input_str)
    if input_int > 6:
        await event.reply("hey nigga use number 1 to 6 only")
    
    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice(""))
        except BaseException:
            pass


@register(pattern="^/dartt(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice("🎯"))
    input_int = int(input_str)
    if input_int > 6:
        await event.reply("hey nigga use number 1 to 6 only")
    
    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🎯"))
        except BaseException:
            pass


@register(pattern="^/balll(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    r = await event.reply(file=InputMediaDice("🏀"))
    input_int = int(input_str)
    if input_int > 5:
        await event.reply("hey nigga use number 1 to 6 only")
    
    else:
        try:
            required_number = input_int
            while r.media.value != required_number:
                await r.delete()
                r = await event.reply(file=InputMediaDice("🏀"))
        except BaseException:
            pass



__help__ = """
 *Play Game With Emojis:*
  - /dice or /dice 1 to 6 any value
  - /ball or /ball 1 to 5 any value
  - /dart or /dart 1 to 6 any value
 Usage: hahaha just a magic.
 warning: you would be in trouble if you input any other value than mentioned.
 *Truth And Dare:*
  - /Truth : for random truth.
  - /dare : for random dare.
"""

__mod_name__ = "Game"
