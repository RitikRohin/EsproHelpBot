from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import ChatPermissions
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import os
import re

API_ID = os.environ.get("API_ID", "none") 
API_HASH = os.environ.get("API_HASH", "none") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "none") 
BOT_IMAGE = os.environ.get("BOT_IMAGE", "https://ibb.co/8npYwYvg")




app = Client(
    "Espro Help" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


@app.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""\n\n┏────────────────────┓\n┃✦ ᴛʜɪs ɪs ʜᴇʟᴘ ʙσᴛ ✔️\n┃✦ ηᴏ ʟᴧɢ | ηᴏ ᴀᴅs | ηᴏ ᴘʀσϻᴏ ⚡️\n┣─────⟨𝐄𝗌ρ𝗋ⱺ ✘ 𝐇ᴇʟᴘ⟩─────┫\n┃✦ ғᴧsᴛ ʀєᴘʟʏ & ηᴏ ᴅσᴡηᴛɪϻє. ❤️ \n┃✦ ʀєᴘʟʏ ɪη ɢʀσᴜᴘs & ᴘʀɪᴠᴧᴛє. 🦋 \n┗────────────────────┛\n<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.</b>""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕", url=f"https://t.me/EsproHelpBot?startgroup=true")
                ]
                
           ]
        ),
    )
    
    


# Link detection regex (detects http, https, t.me, www)
LINK_REGEX = re.compile(r"(https?://|www\.|t\.me/|telegram\.me/)", re.IGNORECASE)

@app.on_message(filters.group & filters.text)
async def delete_links_from_members(client, message):
    # Skip if no sender
    if not message.from_user:
        return

    # If link is found in message
    if LINK_REGEX.search(message.text):
        # Get list of admins in this chat
        admins = await client.get_chat_members(message.chat.id, filter="administrators")
        admin_ids = [admin.user.id for admin in admins]

        # If sender is NOT admin, delete the message
        if message.from_user.id not in admin_ids:
            try:
                await message.delete()
                print(f"Deleted link from {message.from_user.first_name}")
            except Exception as e:
                print(f"Error deleting message: {e}")

# Delete "user joined" messages
@app.on_message(filters.new_chat_members)
async def delete_join_message(client: Client, message: Message):
    await message.delete()

# Delete "user left" messages
@app.on_message(filters.left_chat_member)
async def delete_left_message(client: Client, message: Message):
    await message.delete()

from pyrogram import Client, filters
from pyrogram.types import Message


# Filter to catch only forwarded messages
@app.on_message(filters.forwarded & filters.group)
async def delete_forwarded_messages(client: Client, message: Message):
    try:
        await message.delete()
        print(f"Deleted forwarded message from {message.from_user.first_name}")
    except Exception as e:
        print(f"Failed to delete message: {e}")

print("Bot ⭐")
app.run()
