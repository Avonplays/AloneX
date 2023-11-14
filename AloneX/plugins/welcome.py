import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AloneX import app  

photo = [
    "https://telegra.ph/file/8fd9c28fe4892255c0f0b.jpg",
    "https://telegra.ph/file/338583613bb47f1cebd6d.jpg",
    "https://telegra.ph/file/3b68802676fa0b25e7c0f.jpg",
    "https://telegra.ph/file/717de0f92512309d618ae.jpg",
    "https://telegra.ph/file/4ab6a94e4aef57286e8f0.jpg",
    "https://telegra.ph/file/82ebd673870991031b4e3.jpg",
    "https://telegra.ph/file/61f4d8fce57537a751eee.jpg",
    "https://telegra.ph/file/e6efafb5d00c20a795b03.jpg",
    "https://telegra.ph/file/d6ce1612e3cf51dc2a006.jpg",
    "https://telegra.ph/file/254191c8f969bc68bc7bc.jpg",
    "https://telegra.ph/file/4eacc8d46fe9a2ce2a4e2.jpg",
    "https://telegra.ph/file/f7ec07013ec11e07fea58.jpg",
    "https://telegra.ph/file/f62c320c2d79f9ad03915.jpg",
    "https://telegra.ph/file/44068c62784b424af34ae.jpg",
    "https://telegra.ph/file/ea84fe9f4e2793f2a1401.jpg",
    
]


@app.on_message(filters.new_chat_members, group=3)
async def join_watcher(_, message):    
    chat = message.chat
    
    for members in message.new_chat_members:
        
            count = await app.get_chat_members_count(chat.id)

            msg = (
                f"**🌷𝐇ᴇʏ {message.from_user.mention} 𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐀 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳**\n\n"
                f"**📝𝐂ʜᴀᴛ 𝐍ᴀᴍᴇ:** {message.chat.title}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**🔐𝐂ʜᴀᴛ 𝐔.𝐍:** @{message.chat.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**💖𝐔ʀ 𝐈d:** {message.from_user.id}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**✍️𝐔ʀ 𝐔.𝐍:** @{message.from_user.username}\n➖➖➖➖➖➖➖➖➖➖➖\n"
                f"**👥𝐂ᴏᴍᴘʟᴇᴛᴇᴅ {count} 𝐌ᴇᴍʙᴇʀ𝐬🎉**"
            )
            await app.send_photo(message.chat.id, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(f"🥳ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴄʜᴀᴛ🥳", url=f"https://t.me/{app.username}?startgroup=true")]
         ]))
