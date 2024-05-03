from pyrogram import filters
from Downloader import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo(photo="https://telegra.ph/file/92a26585c37a4530112c0.jpg", caption="**𝙷𝚒!**\n\n**𝙶𝚒𝚟𝚎 /txt 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚝𝚘 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙵𝚛𝚘𝚖 𝚊 𝚃𝚎𝚡𝚝 𝚏𝚒𝚕𝚎.**🎓✨",
                            reply_markup=InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_")
                ],             
                [
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/+W6cfPgJu8yU1MzFh"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/+W6cfPgJu8yU1MzFh")
                ]
                            ]))


@app.on_callback_query(filters.regex("^help_$"))
async def help_command_callback(_, callback_query):
    await callback_query.answer()
    await callback_query.message.edit_text("** 𝗞𝗛𝗨𝗗 𝗕𝗛𝗜 𝗠𝗘𝗛𝗡𝗔𝗧 𝗞𝗔𝗥 𝗟𝗘 𝗧𝗛𝗢𝗗𝗜**", reply_markup=InlineKeyboardMarkup([
        [
            InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="back_")
        ]
    ]))


@app.on_callback_query(filters.regex("^back_$"))
async def back_to_start_callback(_, callback_query):
    await callback_query.answer()
    await callback_query.message.edit_text("**𝙷𝚒!**\n\n**𝙶𝚒𝚟𝚎 /txt 𝙲𝚘𝚖𝚖𝚊𝚗𝚍 𝚝𝚘 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍 𝙵𝚛𝚘𝚖 𝚊 𝚃𝚎𝚡𝚝 𝚏𝚒𝚕𝚎.**🎓✨",
                                          reply_markup=InlineKeyboardMarkup([
                                              [
                                                  InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_")
                                              ],
                                              [
                                                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/+W6cfPgJu8yU1MzFh"),
                                                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/+W6cfPgJu8yU1MzFh")
                                              ]
                                          ]))
