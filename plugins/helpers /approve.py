import os
import asyncio
import random
import pytz
import datetime
from pyrogram import Client, filters
from pyrogram.types import Message, User, InlineKeyboardMarkup, InlineKeyboardButton, ChatJoinRequest
from info import CHAT_ID, TEXT, APPROVED, PICS

@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client, message: ChatJoinRequest):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined (Approved)") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)       
    buttons = [[
                InlineKeyboardButton('• Jᴏɪɴ Gʀᴏᴜᴘ¹ •', url='https://t.me/+pyrfAbBUsMExOTZl'),       
                InlineKeyboardButton('• Jᴏɪɴ Gʀᴏᴜᴘ² •', url='https://t.me/+_B8Y75f6gGQ5MjU1')
            ]]      
    k = await client.send_photo(
        photo=random.choice(PICS),
        chat_id=message.from_user.id, 
        caption=TEXT.format(mention=user.mention, title=chat.title),
        reply_markup=InlineKeyboardMarkup(buttons)
        )   
    await asyncio.sleep(20)
    await k.delete()
    await message.delete()
