class script(object):
    START_TXT = """<b>{} {},    
ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ.</b>"""

    STARTER_TXT = """<b>{} 
    
• എന്താണ് സഹോദരന് വേണ്ടത്? സ്റ്റാർട്ട്‌ ആയപ്പോ ഒരു സുഖം കിട്ടി അല്ലേ.. 🤭😜

• എന്തായാലും വന്നതല്ലേ. ഇവിടെ കാണുന്ന ചാനൽ & ഗ്രൂപ്പ് ൽ ഒക്കെ Join ചെയ്തേക്ക് 😎 Ok bye..</b>"""

    HELPER_TXT = """<b>ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.</b>"""
    
    ABOUT_TXT = """<b>◆ ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/Oru_adaar_Robot'>♡ Nᴀɴᴄʏ ᵛ³</a>
◆ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/Hacker_Jr'>HᴀᴄKᴇʀ Jʀ 〆⁪⁬⁮⁮⁮</a>
◆ ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>ᴘʀᴏɢʀᴀᴍ</a>
◆ ʟᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/'>ᴘʏᴛʜᴏɴ 𝟹</a>
◆ ᴅᴀᴛᴀ ʙᴀsᴇ: <a href='https://cloud.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
◆ ʙᴏᴛ sᴇʀᴠᴇʀ: <a href='tg://settings'>ᴘʀɪᴠᴀᴛᴇ</a>
◆ ʙᴜɪʟᴅ sᴛᴀᴛᴜs: v4.5 [ sᴛᴀʙʟᴇ ]</b>"""
    
    SOURCE_TXT = """<b>ᴛʜɪꜱ ɴᴏᴛ ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ

»sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ~ ᴘʀɪᴠᴀᴛᴇ 🤒</b>"""

    MANUELFILTER_TXT = """<b><u>FILTERS COMMANDS</u></b>

• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """<b><u>BUTTONS NOTE:-</u></b>

• ᴛᴇʟᴇɢʀᴀᴍ ᴡɪʟʟ ɴᴏᴛ ᴀʟʟᴏᴡs ʏᴏᴜ ᴛᴏ sᴇɴᴅ ʙᴜᴛᴛᴏɴs ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴄᴏɴᴛᴇɴᴛ, sᴏ ᴄᴏɴᴛᴇɴᴛ ɪs ᴍᴀɴᴅᴀᴛᴏʀʏ.
• ɴᴀɴᴄʏ ʙᴏᴛ sᴜᴘᴘᴏʀᴛs ʙᴜᴛᴛᴏɴs ᴡɪᴛʜ ᴀɴʏ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ.
• ʙᴜᴛᴛᴏɴs sʜᴏᴜʟᴅ ʙᴇ ᴘʀᴏᴘᴇʀʟʏ ᴘᴀʀsᴇᴅ ᴀs ᴍᴀʀᴋᴅᴏᴡɴ ꜰᴏʀᴍᴀᴛ.

<b><u>URL BUTTONS:-</u></b>
<code>[Button Text](buttonurl:https://t.me/Oru_adaar_Robot)</code>

<b><u>ALERT BUTTONS:-</u></b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """<b><u>AUTO FILTER NOTE:-</u></b>

• ᴍᴀᴋᴇ ᴍᴇ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏꜰ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜰ ɪᴛ's ᴘʀɪᴠᴀᴛᴇ.
• ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴅᴏᴇs ɴᴏᴛ ᴄᴏɴᴛᴀɪɴs ᴄᴀᴍʀɪᴘs, ᴘᴏʀɴ ᴀɴᴅ ꜰᴀᴋᴇ ꜰɪʟᴇs.
• ꜰᴏʀᴡᴀʀᴅ ᴛʜᴇ ʟᴀsᴛ ᴍᴇssᴀɢᴇ ᴛᴏ ᴍᴇ ᴡɪᴛʜ ǫᴜᴏᴛᴇs. ɪ'ʟʟ ᴀᴅᴅ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇs ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴍʏ ᴅʙ.</b>"""

    CONNECTION_TXT = """<b><u>CONNECTIONS NOTE:-</u></b>

1. ONLY ADMINS CAN ADD A CONNECTION.
2. SEND <code>/connect</code> FOR CONNECTING ME TO UR PM

<b><u>COMMANDS AND USAGE:-</u></b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    EXTRAMOD_TXT = """<b><u>EXTRA MODULES COMMANDS</u></b>

• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """<b><u>ADMIN MODS COMMANDS</u></b>
    
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /bcspeed - <code>to speed broadcast a message to all users</code>
• /grp_broadcast - <code>to broadcast a message to all groups</code>
• /gfilter - <code>To add global filter</code>
• /gfilters - <code>To view global filters</code>
• /delallg - <code>To delete all global filters from database</code>
• /delg - <code>To delete a specific global filter</code>
• /setskip - <code>Skip no of files before indexing</code>
• /send - <code>Send any message through bot to users. /send (username/userid) reply with message </code>"""

    STATUS_TXT = """<b>◉ ᴛᴏᴛᴀʟ ғɪʟᴇs : <code>{}</code>
◉ ᴛᴏᴛᴀʟ ᴜsᴇʀs : <code>{}</code>
◉ ᴛᴏᴛᴀʟ ᴄʜᴀᴛs : <code>{}</code>
◉ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ : <code>{}</code>
◉ ғʀᴇᴇ sᴛᴏʀᴀɢᴇ : <code>{}</code></b>"""   
    
    LOG_TEXT_G = """#NewUser
 <b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {a}(<code>{b}</code>)</b>
 <b>᚛› 𝐆 𝐈𝐃 ⪼ @{c}
 <b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ {d}</b>
 <b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {e}</b>
 By {f}"""

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}"""
    
    FILE_MSG = """
<b>Hai 👋 {} 😍

📫 Your File is Ready

📂 Fɪʟᴇ Nᴀᴍᴇ: <code>{}</code>              
                       
⚙️ Fɪʟᴇ Sɪᴢᴇ: {}
"""
    CHANNEL_CAP = """
<b>Hai 👋 {}</b> 😍

<code>{}</code>

⚠️ <b>This file will be deleted from here within 10 minute as it has copyright ... !!!</b>

<b>കോപ്പിറൈറ്റ് ഉള്ളതുകൊണ്ട് ഫയൽ 10 മിനിറ്റിനുള്ളിൽ ഇവിടെനിന്നും ഡിലീറ്റ് ആകുന്നതാണ് അതുകൊണ്ട് ഇവിടെ നിന്നും മറ്റെവിടെക്കെങ്കിലും മാറ്റിയതിന് ശേഷം ഡൗൺലോഡ് ചെയ്യുക!</b>

<b>© Powered by {}</b>
"""
    
    IMDB_TEMPLATE_TXT = """
<b>⍞ TɪᴛLᴇ : {title}
⌬ YᴇAʀ : {year}
✇ LᴀNɢUᴀGᴇ : {languages}
⛦ RᴀTɪNɢ : {rating} / 10.0
〄 QᴜAʟIᴛY : HDRip

★ ροωєяє∂ ϐγ : @Team_KL</b>"""
   
    CUSTOM_FILE_CAPTION = """<b>▷ ғɪʟᴇ ɴᴀᴍᴇ : {file_name}

▷ ғɪʟᴇ sɪᴢᴇ : {file_size}

★ @Team_KR
★ @KLMovieGroup</b>"""    

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""

    MELCOW_ENG = """<b>Hᴇʟʟᴏ {}, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ"""

    ALRT_TXT = """• This Is Not Your Movie Request. 
    
• Don't Click Others Results 🥴."""
    
    OLD_ALRT_TXT = """You Are Using One Of My Old Messages, Please Send The Request Again"""

    TOP_ALRT_MSG = """<b>𝕊𝕖𝕒𝕣𝕔𝕙𝕚𝕟𝕘 ℝ𝕖𝕤𝕦𝕝𝕥𝕤 🥴</b>"""
    
    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""   

    SPEL_CHK = """<b>🥺 Sorry No File Found <u>{}</u>

▪️Use The Button Below To Search On <u>Google</u> Or <u>IMDB</u> And Copy The Correct Movie Name And Paste..!!

▪️Don't Ask Movies That Are Not Released In OTT Platform..!!

▪️Try To Ask In [Moviename, Year, Language] This Format..!! 

🚯 Don't Use: ➠ ':(!,./) 🙅‍♂</b>"""
    
    MVE_NT_FND = """<b>This Movie Not Available 😢

<u>For Reasons</u> 👀

◉) OTT Or DVD Not Released..!
◉) Type Name With Year..!
◉) check your correct spelling..!
◉) Movie Is Not Available in My Database..!
◉) Don't Ask Theater Print 🥴..!</b>"""

    CUDNT_FND = """<b>➠ No Movie Found For Your Query <u>{}</u>

➠ Choose The Correct Movie Name Below 👇</b>​"""

    I_CUDNT = """Hᴇʟʟᴏ {}, I Cᴏᴜʟᴅɴ'ᴛ Fɪɴᴅ Aɴʏ Mᴏᴠɪᴇ Iɴ Tʜᴀᴛ Nᴀᴍᴇ​"""

    I_CUD_NT = """Hᴇʟʟᴏ {}, I Cᴏᴜʟᴅɴ'ᴛ Fɪɴᴅ Aɴʏᴛʜɪɴɢ​ Rᴇʟᴀᴛᴇᴅ Tᴏ Tʜᴀᴛ. Cʜᴇᴄᴋ Yᴏᴜʀ Sᴘᴇʟʟɪɴɢ​"""    
    
    REPRT_MSG = """Reported To Admin"""    

    WHYJOIN = """Iғ Tʜᴇ Gʀᴏᴜᴘ Cᴏᴘʏ Rɪɢʜᴛ Iꜱ Lᴏꜱᴛ, Wʜᴇɴ A Nᴇᴡ Gʀᴏᴜᴘ Iꜱ Sᴛᴀʀᴛᴇᴅ, Iᴛ Wɪʟʟ Bᴇ Nᴏᴛɪғɪᴇᴅ Oɴ Tʜɪꜱ Cʜᴀɴɴᴇʟ 🤥

© @Team_KL"""

    OWNER_INFO = """
<b>⍟───[ Oᴡɴᴇʀ Dᴇᴛᴀɪʟꜱ ]───⍟
    
• Fᴜʟʟ Nᴀᴍᴇ : • HᴀᴄKᴇʀ Jʀ ~ 🕊 
• Uꜱᴇʀɴᴀᴍᴇ : @Hacker_Jr
• Lᴏɢᴏ Mᴀᴋᴇʀ : <a href='t.me/PremiumlogoPro'>Pʀᴇᴍɪᴜᴍ Lᴏɢᴏ Pʀᴏ</a></b>"""

    GROUP_INFO = """
<b>⍟ Wᴇʟᴄᴏᴍᴇ Tᴏ Tᴇᴀᴍ Kʟ Lɪɴᴋs ⍟</b>"""

    FIlTERS_TXT = """
<b>Tʜᴇsᴇ Aʀᴇ Mʏ Tʜʀᴇᴇ Tʏᴘᴇs Oғ Fɪʟᴛᴇʀs.</b>"""

    GLOBE_TXT = """
<b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
    
Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""

    FILE_STORE_TXT = """
<b>Fɪʟᴇ sᴛᴏʀᴇ ɪs ᴛʜᴇ ғᴇᴀᴛᴜʀᴇ ᴡʜɪᴄʜ ᴡɪʟʟ ᴄʀᴇᴀᴛᴇ ᴀ sʜᴀʀᴇᴀʙʟᴇ ʟɪɴᴋ ᴏғ ᴀ sɪɴɢʟᴇ ᴏʀ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""

    APPROVED_TEXT = """<b><i>🙋 Hello {mention}

◈ Your Request To Joined In ➤
 <u>{title}</u> Successfully.

◈ Tʜᴀɴᴋ Yᴏᴜ ❤️ {mention} 

◈ ροωєяє∂ ϐγ :- @Team_KL</i></b>"""

    AFTER_TXT = """<b><i>🙋🏻‍♀ Hey, {} Your Last Movies Request Has Been Deleted Because Of Copyright Issues..!

Kindly Request Again For Your Files.☺️</i></b>"""

    DISCL_TXT = """<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ᴏʀ ʙʏ ᴀɴʏ ᴍᴇᴀɴꜱ, ꜱʜᴀʀᴇ, ᴏʀ ᴄᴏɴꜱᴜᴍᴇ, ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.</b> 
    
