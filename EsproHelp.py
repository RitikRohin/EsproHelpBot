from pyrogram import Client, filters
from pyrogram.types import Message
import re

API_ID = os.environ.get("API_ID", "none") 
API_HASH = os.environ.get("API_HASH", "none") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", "none") 



app = Client(
    "Espro Help" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
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



app = Client("your_bot", bot_token="YOUR_BOT_TOKEN", api_id=12345, api_hash="your_api_hash")

# Delete "user joined" messages
@app.on_message(filters.new_chat_members)
async def delete_join_message(client: Client, message: Message):
    await message.delete()

# Delete "user left" messages
@app.on_message(filters.left_chat_member)
async def delete_left_message(client: Client, message: Message):
    await message.delete()


app.run()
