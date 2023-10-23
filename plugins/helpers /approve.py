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
    T = datetime.datetime.now(pytz.timezone("Asia/Kolkata"))
    Time = T.hour        
    if Time < 12:
        afsu="Gᴏᴏᴅ Mᴏʀɴɪɴɢ" 
    elif Time < 15:
        afsu="Gᴏᴏᴅ AғᴛᴇʀNᴏᴏɴ" 
    elif Time < 20:
        afsu="Gᴏᴏᴅ Eᴠᴇɴɪɴɢ"
    else:
        afsu="Gᴏᴏᴅ Nɪɢʜᴛ"    
    buttons = [[
                InlineKeyboardButton('• Jᴏɪɴ Gʀᴏᴜᴘ¹ •', url='https://t.me/+pyrfAbBUsMExOTZl'),       
                InlineKeyboardButton('• Jᴏɪɴ Gʀᴏᴜᴘ² •', url='https://t.me/+_B8Y75f6gGQ5MjU1')
            ]]        
    k = await client.send_photo(
        photo=random.choice(PICS),
        chat_id=message.from_user.id, 
        caption=TEXT.format(afsu, mention=user.mention, title=chat.title),
        reply_markup=InlineKeyboardMarkup(buttons)
        )   
    await asyncio.sleep(7)
    await k.delete()
    await message.delete()
    
