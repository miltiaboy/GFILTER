class script(object):
    START_TXT = """<b>{} {},    
ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs, ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴇɴᴊᴏʏ.</b>"""

    STARTER_TXT = """<b>{} 
    
• എന്താണ് സഹോദരന് വേണ്ടത്? സ്റ്റാർട്ട്‌ ആയപ്പോ ഒരു സുഖം കിട്ടി അല്ലേ.. 🤭😜

• എന്തായാലും വന്നതല്ലേ. ഇവിടെ കാണുന്ന ചാനൽ & ഗ്രൂപ്പ് ൽ ഒക്കെ Join ചെയ്തേക്ക് 😎 Ok bye..</b>"""

    HELPER_TXT = """<b>ᴛʜᴇ ʜᴇʟᴘ ғᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.</b>"""
    
    ABOUT_TXT = """<b>◆ ᴍʏ ɴᴀᴍᴇ : <a href='https://t.me/Oru_adaar_Robot'>♡ Nᴀɴᴄʏ ᵛ³</a>
◆ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/Hacker_Jr'>HᴀᴄKᴇʀ Jʀ 〆⁪⁬⁮⁮⁮</a>
◆ ʟɪʙʀᴀʀʏ: <a href='https://pyrofork.mayuri.my.id/'>ᴘʏʀᴏғᴏʀᴋ</a>
◆ ʟᴀɴɢᴜᴀɢᴇ: <a href='https://www.python.org/'>ᴘʏᴛʜᴏɴ 𝟹</a>
◆ ᴅᴀᴛᴀ ʙᴀsᴇ: <a href='https://cloud.mongodb.com/'>ᴍᴏɴɢᴏ ᴅʙ</a>
◆ ʙᴏᴛ sᴇʀᴠᴇʀ: <a href='tg://settings'>ᴘʀɪᴠᴀᴛᴇ</a></b>"""
    
    SOURCE_TXT = """<b>ᴛʜɪꜱ ɴᴏᴛ ᴀɴ ᴏᴘᴇɴ sᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ

» sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ~ ᴘʀɪᴠᴀᴛᴇ 🤒</b>"""

    MANUELFILTER_TXT = """<b>➪ <u>MANUAL FILTER NOTE:</u>
    
Filter Is The Feature Were Users Can Set Automated Replies For A Particular Keyword And I Will Respond Whenever A Keyword Is Found The Message.

➥ This Bot Should Have Admin Privilege
➥ Only Admins Can Add Filters In A Chat
➥ Alert Buttons Have A Limit Of 64 Characters
    
➪ <u>𝖠𝖵𝖠𝖨𝖫𝖠𝖡𝖫𝖤 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖲:</u>
• /filter - Add A Filter In Chat
• /filters - List All The Filters Of A Chat
• /del - Delete A Specific Filter In Chat
• /delall - Delete The Whole Filters In A Chat (Chat Owner Only)</b>"""

    BUTTON_TXT = """<b>➪ <u>BUTTONS NOTE:</u>

➥ Telegram Will Not Allows You To Send Buttons Without Any Content, So Content Is Mandatory.
➥ This Bot Supports Buttons With Any Telegram Media Type.
➥ Buttons Should Be Properly Parsed As Markdown Format.

➪ <u>URL BUTTONS:</u>
[Button Text](buttonurl:https://t.me/Team_KL)

➪ <u>ALERT BUTTONS:</u>
[Button Text](buttonalert:This Is An Alert Message)</b>"""

    AUTOFILTER_TXT = """<b>➪ <u>AUTO FILTER NOTE:</u>
    
AutoFilter Module Searches IMDB For Movie Details And Database For Files And Sends Results For Each Message In A Groups.

• This Command Only Works For My Admin

➥ Enable  : /autofilter on
➥ Disable : /autofilter off</b>"""

    FILEINDEX_TXT = """<blockquote><b>➪ <u>FILE INDEX NOTE:</u>

➥ Make Me The Admin Of Your Channel If It's Private.
➥ Make Sure That Your Channel Does Not Contains Camrips, Porn And Fake Files.
➥ Forward The Last Message To Me With Quotes. I'll Add All The Files In That Channel To My Database.</b></blockquote>"""

    CONNECTION_TXT = """<b>➪ <u>CONNECTIONS NOTE:</u>
    
Used To Connect Bot To PM For Managing Filters 
It Helps To Avoid Spamming In Groups.

➥ Only Admins Can Add A Connection.
➥ Send <code>/connect</code> For Connecting Me To YOUR PM

➪ <u>𝖠𝖵𝖠𝖨𝖫𝖠𝖡𝖫𝖤 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖲:</u>
• /connect  - Connect A Particular Chat To Your PM
• /disconnect  - Disconnect From A Chat
• /connections - List All Your Connections</b>"""

    EXTRAMOD_TXT = """<b>➪ <u>EXTRA MODULES COMMANDS:</u>

• /id - Get Id of A Specified User.
• /info  - Get Information About A User.
• /imdb  - Get The Film Information From IMDb Source.
• /search  - Get The Film Information From Various Sources.</b>"""

    FSUB_MSG = """<b>➪ <u>REQUEST FORCESUB MOD:</u>
    
➥ This Module Only Works For My Admin

/setchat : Add ForceSub / Request Channel Id
/delchat : Deleted ForceSub Channel
/viewchat : Get Saved ForceSub Channel Detail
/totalrequests : Get Total Request Counts On Current FSub Channel
/purgerequests : Clear Requests On Current FSub Channel</b>"""
    
    ADMIN_TXT = """<b>➪ <u>ADMIN MODS COMMANDS:</u></b>
    
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

    LOG_TEXT_G = """<b>#New_Group - {}

○ Group Name :- {}
○ Group Id :- <code>{}</code> 
○ Group Username :- @{}
○ Group Link :- {}
○ Total Members :- <code>{}</code>
○ User :- {}</b>"""

    LOG_TEXT_P = """<b>#New_User
    
≈ ᴜsᴇʀ ɪᴅ:- <code>{}</code>
≈ ɴᴀᴍᴇ:- {}</b>"""
    
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
   
    CUSTOM_FILE_CAPTION = """<b>⍟ ғɪʟᴇ ɴᴀᴍᴇ : {file_name}

⍟ ғɪʟᴇ sɪᴢᴇ : {file_size}

‣ @KLxFiles 
‣ @KLMovieGroup</b>"""    

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
    
    MVE_NT_FND = """<b><u>🎞 This Movie Not Available For Reason 👇</u>
 
◉) OTT Or DVD Not Released..!
◉) Type Name With Year..!
◉) Check Your Correct Spelling..!
◉) Movie Is Not Available in My Database.. Report To Admin @KLAdmin1Bot</b>"""

    CUDNT_FND = """<b>➠ No Movie Found For Your Query <u>{}</u>

➠ Choose The Correct Movie Name Below 👇</b>​"""

    I_CUDNT = """Hᴇʟʟᴏ {}, I Cᴏᴜʟᴅɴ'ᴛ Fɪɴᴅ Aɴʏ Mᴏᴠɪᴇ Iɴ Tʜᴀᴛ Nᴀᴍᴇ​"""

    I_CUD_NT = """Hᴇʟʟᴏ {}, I Cᴏᴜʟᴅɴ'ᴛ Fɪɴᴅ Aɴʏᴛʜɪɴɢ​ Rᴇʟᴀᴛᴇᴅ Tᴏ Tʜᴀᴛ. Cʜᴇᴄᴋ Yᴏᴜʀ Sᴘᴇʟʟɪɴɢ​"""    
    
    REPRT_MSG = """Reported To Admin"""    

    WHYJOIN = """Iғ Tʜᴇ Gʀᴏᴜᴘ Cᴏᴘʏ Rɪɢʜᴛ Iꜱ Lᴏꜱᴛ, Wʜᴇɴ A Nᴇᴡ Gʀᴏᴜᴘ Iꜱ Sᴛᴀʀᴛᴇᴅ, Iᴛ Wɪʟʟ Bᴇ Nᴏᴛɪғɪᴇᴅ Oɴ Tʜɪꜱ Cʜᴀɴɴᴇʟ 🤥

© @Team_KL"""

    OWNER_INFO = """
<b>⍟───[ ᴏᴡɴᴇʀ ᴅᴇᴛᴀɪʟꜱ ]───⍟
    
 ‣ ꜰᴜʟʟ ɴᴀᴍᴇ : • HᴀᴄKᴇʀ Jʀ ~ 🕊 
 ‣ ᴜꜱᴇʀɴᴀᴍᴇ : @Hacker_Jr
 ‣ ᴄᴏᴜɴᴛʀʏ : ɪɴᴅɪᴀ 🇮🇳
 ‣ ʟᴏɢᴏ ᴍᴀᴋᴇʀ : <a href='t.me/PremiumlogoPro'>ᴘʀᴇᴍɪᴜᴍ ʟᴏɢᴏ ᴘʀᴏ</a></b>"""

    GROUP_INFO = """
<b>⍟ Wᴇʟᴄᴏᴍᴇ Tᴏ Tᴇᴀᴍ Kʟ Lɪɴᴋs ⍟</b>"""

    FIlTERS_TXT = """
<b>ᴛʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs..</b>"""

    GLOBE_TXT = """<b>➪ 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 𝖦𝗅𝗈𝖻𝖺𝗅 𝖥𝗂𝗅𝗍𝖾𝗋𝗌. 𝖦𝗅𝗈𝖻𝖺𝗅 𝖥𝗂𝗅𝗍𝖾𝗋𝗌 𝖠𝗋𝖾 𝖳𝗁𝖾 𝖥𝗂𝗅𝗍𝖾𝗋𝗌 𝖲𝖾𝗍 𝖡𝗒 𝖡𝗈𝗍 𝖠𝖽𝗆𝗂𝗇𝗌 𝖶𝗁𝗂𝖼𝗁 𝖶𝗂𝗅𝗅 𝖶𝗈𝗋𝗄 𝖮𝗇 𝖠𝗅𝗅 𝖦𝗋𝗈𝗎𝗉𝗌.

➪ <u>𝖠𝖵𝖠𝖨𝖫𝖠𝖡𝖫𝖤 𝖢𝖮𝖬𝖬𝖠𝖭𝖣𝖲:</u>
• /gfilter - To Create A Global Filters.
• /gfilters - To View All Global Filters.
• /delg - To Delete A Particular Global Filters.
• /delallg - To Delete All Global Filters.</b>"""

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

    DISCL_TXT = """<blockquote><b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ᴏʀ ʙʏ ᴀɴʏ ᴍᴇᴀɴꜱ, ꜱʜᴀʀᴇ, ᴏʀ ᴄᴏɴꜱᴜᴍᴇ, ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.</b></blockquote>"""
    
