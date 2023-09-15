from pyrogram import filters

from PrachiMusic.utilities.config import BANNED_USERS
from PrachiMusic import YouTube, bot
from PrachiMusic.modules.utils.channelplay import get_channeplayCB
from PrachiMusic.modules.main.decorators.language import languageCB
from PrachiMusic.modules.main.streamer.stream import stream


@bot.on_callback_query(filters.regex("LiveStream") & ~BANNED_USERS)
@languageCB
async def play_live_stream(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    vidid, user_id, mode, cplay, fplay = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                _["playcb_1"], show_alert=True
            )
        except:
            return
    try:
        chat_id, channel = await get_channeplayCB(
            _, cplay, CallbackQuery
        )
    except:
        return
    video = True if mode == "v" else None
    user_name = CallbackQuery.from_user.first_name
    await CallbackQuery.message.delete()
    try:
        await CallbackQuery.answer()
    except:
        pass
    mystic = await CallbackQuery.message.reply_text(
        _["play_2"].format(channel) if channel else _["play_1"]
    )
    try:
        details, track_id = await YouTube.track(vidid, True)
    except Exception:
        return await mystic.edit_text(_["play_3"])
    ffplay = True if fplay == "f" else None
    if not details["duration_min"]:
        try:
            await stream(
                _,
                mystic,
                user_id,
                details,
                chat_id,
                user_name,
                CallbackQuery.message.chat.id,
                video,
                streamtype="live",
                forceplay=ffplay,
            )
        except Exception as e:
            ex_type = type(e).__name__
            err = (
                e
                if ex_type == "AssistantErr"
                else _["general_3"].format(e)
            )
            return await mystic.edit_text(err)
    else:
        return await mystic.edit_text("ɪ ᴅᴏɴ'ᴛ ᴛʜɪɴᴋ ᴛʜᴀᴛ ɪᴛ's ᴀ ʟɪᴠᴇ sᴛʀᴇᴀᴍ.")
    await mystic.delete()