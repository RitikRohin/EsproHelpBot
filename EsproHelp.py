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
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐇𝐢  𝐈'𝐦 𝐀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 🌷.\n\n📌 𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 𝐕 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 🌷 𝐅𝐨𝐫𝐦 𝐈𝐧𝐝𝐢𝐚 🇮🇳 \n\n🌷 𝐈'𝐦 𝐀 𝐀𝐫𝐭𝐢𝐟𝐢𝐜𝐢𝐚𝐥 𝐈𝐧𝐭𝐞𝐥𝐥𝐢𝐠𝐞𝐧𝐜𝐞 🌷\n\n /chatbot - [on|off] 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐔𝐬𝐞 𝐎𝐧𝐥𝐲 𝐀𝐧𝐲 𝐆𝐫𝐨𝐮𝐩


💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝
𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐂𝐡𝐚𝐭.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕", url=f"https://t.me/EsproHelpBot?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@app.on_message(filters.command(["start"]) & filters.group)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_IMAGE}",
        caption=f"""💥 𝐇𝐢! 𝐈'𝐦 𝐀 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 𝐂𝐡𝐚𝐭 𝐁𝐨𝐭 🌷.\n\n📌 𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 𝐕 𝐁𝐨𝐭 🌷 𝐅𝐨𝐫𝐦 𝐈𝐧𝐝𝐢𝐚 🇮🇳 \n\n🌷 𝐈'𝐦 𝐀 𝐀𝐫𝐭𝐢𝐟𝐢𝐜𝐢𝐚𝐥 𝐈𝐧𝐭𝐞𝐥𝐥𝐢𝐠𝐞𝐧𝐜𝐞 🌷\n\n𝐀𝐧𝐲 𝐏𝐫𝐨𝐛𝐥𝐞𝐦 𝐓𝐨 [𝐑𝐞𝐩𝐨𝐫𝐭](https://t.me/{SUPPORT_GROUP})  🥀\n\n[𝐔𝐩𝐝𝐚𝐭𝐞𝐬](https://t.me/{UPDATES_CHANNEL}) 🌷\n\n /chatbot - [on|off]""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 💥 𝐉𝐨𝐢𝐧 𝐎𝐮𝐫 𝐂𝐡𝐚𝐭 𝐆𝐫𝐨𝐮𝐩 💞", url=f"https://t.me/bgt_chat")
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

# Only group admins can use these commands
def admin_filter():
    return filters.group & filters.user(lambda _, __, msg: msg.from_user and msg.chat.get_member(msg.from_user.id).status in ["administrator", "creator"])

@app.on_message(filters.command("admin") & admin_filter())
async def promote_user(client, message):
    if not message.reply_to_message:
        return await message.reply("Kisi member ko reply karke /admin likho.")
    user_id = message.reply_to_message.from_user.id
    await client.promote_chat_member(
        chat_id=message.chat.id,
        user_id=user_id,
        can_change_info=True,
        can_delete_messages=True,
        can_invite_users=True,
        can_restrict_members=True,
        can_pin_messages=True,
        can_promote_members=False
    )
    await message.reply(f"User [{user_id}](tg://user?id={user_id}) ab admin ban gaya.")

@app.on_message(filters.command("unadmin") & admin_filter())
async def demote_user(client, message):
    if not message.reply_to_message:
        return await message.reply("Kisi member ko reply karke /unadmin likho.")
    user_id = message.reply_to_message.from_user.id
    await client.promote_chat_member(
        chat_id=message.chat.id,
        user_id=user_id,
        can_change_info=False,
        can_delete_messages=False,
        can_invite_users=False,
        can_restrict_members=False,
        can_pin_messages=False,
        can_promote_members=False
    )
    await message.reply(f"User [{user_id}](tg://user?id={user_id}) se admin rights hata diye gaye.")

@app.on_message(filters.command("ban") & admin_filter())
async def ban_user(client, message):
    if not message.reply_to_message:
        return await message.reply("Kisi member ko reply karke /ban likho.")
    user_id = message.reply_to_message.from_user.id
    await client.ban_chat_member(message.chat.id, user_id)
    await message.reply(f"User [{user_id}](tg://user?id={user_id}) ko ban kar diya gaya.")

@app.on_message(filters.command("unban") & admin_filter())
async def unban_user(client, message):
    if not message.reply_to_message:
        return await message.reply("Kisi member ko reply karke /unban likho.")
    user_id = message.reply_to_message.from_user.id
    await client.unban_chat_member(message.chat.id, user_id)
    await message.reply(f"User [{user_id}](tg://user?id={user_id}) ko unban kar diya gaya.")

print("Bot ⭐")
app.run()
