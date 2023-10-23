import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, User, ChatJoinRequest
from info import CHAT_ID, TEXT, APPROVED 


@Client.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client, message: ChatJoinRequest):
    chat=message.chat 
    user=message.from_user 
    print(f"{user.first_name} Joined (Approved)") 
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)  
    buttons = [[
                InlineKeyboardButton('🔮 Jᴏɪɴ Mᴏᴠɪᴇs Gʀᴏᴜᴘ 🔮', url='https://t.me/KL_GROUP1')
              ],[       
                InlineKeyboardButton('💥 Jᴏɪɴ Mᴏᴠɪᴇs Cʜᴀɴɴᴇʟ 💥', url='https://t.me/Team_KL')
            ]]
    await client.send_photo(
        photo="https://telegra.ph/file/39e246de80d814ff8bdfd.jpg",
        chat_id=message.from_user.id, 
        caption=TEXT.format(mention=user.mention, title=chat.title),
        reply_markup=InlineKeyboardMarkup(buttons)
        )   
    
