from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import os
import re

API_ID = int(os.environ.get("API_ID", 12345))  # Replace 12345 with your real API_ID
API_HASH = os.environ.get("API_HASH", "your_api_hash")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "your_bot_token")
BOT_IMAGE = os.environ.get("BOT_IMAGE", "https://ibb.co/8npYwYvg")  # Must be direct image URL

app = Client(
    "EsproHelp",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Regex to detect links
link_pattern = re.compile(r"(https?://|www\.|t\.me/|telegram\.me/|@\w+|\.com|\.net|\.org|\.in|\.xyz)")
 
@app.on_message(filters.command("start") & filters.private)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=BOT_IMAGE,
        caption=f"""\n\n┏────────────────────┓\n┃✦ ᴛʜɪs ɪs ʜᴇʟᴘ ʙσᴛ ✔️\n┃✦ ηᴏ ʟᴧɢ | ηᴏ ᴀᴅs | ηᴏ ᴘʀσϻᴏ ⚡️\n┣─────⟨𝐄𝗌ρ𝗋ⱺ ✘ 𝐇ᴇʟᴘ⟩─────┫\n┃✦ ғᴧsᴛ ʀєᴘʟʏ & ηᴏ ᴅσᴡηᴛɪϻє. ❤️ \n┃✦ ʀєᴘʟʏ ɪη ɢʀσᴜᴘs & ᴘʀɪᴠᴧᴛє. 🦋 \n┗────────────────────┛\n<b>๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.</b>""",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔎 How To Use? Command Menu", callback_data="future")],
            [InlineKeyboardButton("✚ Add Me To Your Group ✚", url="https://t.me/EsproHelpBot?startgroup=true")],
            [InlineKeyboardButton("👤 Owner", url="https://t.me/Ur_Haiwan")]
        ])
    )

@app.on_callback_query()
async def button_click(client: Client, callback_query: CallbackQuery):
    if callback_query.data == "future":
        await callback_query.answer("command is coming soon!", show_alert=True)

@app.on_message(filters.group & filters.text)
async def delete_links(client: Client, message: Message):
    if link_pattern.search(message.text or ""):
        if message.from_user and not message.from_user.is_bot:
            try:
                await message.delete()
                print(f"Deleted message with link from {message.from_user.first_name}")
            except Exception as e:
                print(f"Error deleting message: {e}")


@app.on_message(filters.new_chat_members)
async def delete_join_message(client: Client, message: Message):
    await message.delete()

@app.on_message(filters.left_chat_member)
async def delete_left_message(client: Client, message: Message):
    await message.delete()

@app.on_message(filters.forwarded & filters.group)
async def delete_forwarded_messages(client: Client, message: Message):
    try:
        await message.delete()
        print(f"Deleted forwarded message from {message.from_user.first_name}")
    except Exception as e:
        print(f"Failed to delete forwarded message: {e}")


@app.on_message(filters.group & filters.text & ~filters.via_bot)
async def check_bio_for_links(client: Client, message: Message):
    try:
        user = await client.get_chat(message.from_user.id)  # Use get_chat, not get_users
        bio = user.bio or ""  # Correct attribute is 'bio'

        if link_pattern.search(bio):
            await message.delete()
            print(f"Deleted message from @{message.from_user.username or message.from_user.first_name} due to link in bio.")
    except Exception as e:
        print(f"Error: {e}")
 
 
print("Bot ⭐ Running...")
app.run()
