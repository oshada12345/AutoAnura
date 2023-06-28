#### This Code Was Devloped By @AM_ROBOTS ####

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://paisakamalo.in/')
    START_TXT = """Hello {},

My name is <a href=/https://t.me/film_studiox2_bot</a>!

<b>🌝I can provide Movies. ♨️A Telegram Auto Filter Bot.
💐Its Easy To Use Me :) ☁️


ᴍᴀɪɴᴛᴀɪɴ ʙʏ ᴠɪᴍᴜᴋᴛʜɪ ᴏꜱʜᴀᴅᴀ  ☣️

🗣ʏᴏᴜ ᴄᴀɴ ʟᴇᴀᴠᴇ ᴀɴ ɪɴʙᴏx ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴛʜᴇ ᴀᴅᴍɪɴ ᴀɴᴅ ᴛᴇʟʟ ᴀʟʟ ᴛʜᴇ ᴘʀᴏʙʟᴇᴍꜱ ʏᴏᴜ ʜᴀᴠᴇ. 
🔜ɪɴꜰᴏʀᴍ ᴛʜᴇ ᴀᴅᴍɪɴ ᴀʙᴏᴜᴛ ᴛʜᴇ ᴅᴇꜰɪᴄɪᴇɴᴄɪᴇꜱ ᴀɴᴅ ᴀᴅᴅ ᴍᴏʀᴇ

📣ඔයට Movies සහ Tv Series වැනි දෙවල් Download කර ගන්න Group එකට Join වෙන්න🌷<a href='https://t.me/filmstudiodl'>Film Studio</a></b>"""


    HELP_TXT = """🙋🏻‍♂️   𝖧𝖾𝗅𝗅𝗈𝗈𝗈  {} 🤓

○  𝗂𝗍'𝗌 𝖭𝗈𝗍𝖾 𝖢𝗈𝗆𝗉𝗅𝗂𝖼𝖺𝗍𝖾𝖽...🤓

○  𝖲𝖾𝖺𝗋𝖼𝗁 𝗎𝗌𝗂𝗇𝗀 𝗂𝗇𝗅𝗂𝗇𝖾 𝗆𝗈𝖽𝖾
𝖳𝗁𝗂𝗌 𝗆𝖾𝗍𝗁𝗈𝖽 𝗐𝗈𝗋𝗄𝗌 𝗈𝗇 𝖺𝗇𝗒 𝖼𝗁𝖺𝗍, 𝖩𝗎𝗌𝗍 𝗍𝗒𝗉𝖾 <b>Bot Username</b> 𝖺𝗇𝖽 𝗍𝗁𝖾𝗇 𝗅𝖾𝖺𝗏𝖾 𝖺 𝗌𝗉𝖺𝖼𝖾 𝖺𝗇𝖽 𝗌𝖾𝖺𝗋𝖼𝗁 𝖺𝗇𝗒 𝗆𝗈𝗏𝗂𝖾 𝗒𝗈𝗎 𝗐𝖺𝗇𝗍...



○ 𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌
     
 /alive - Check I'm Alive..
 /status - Bot Status
 /info - User info
 /ping - To get your ping
 /id - User id
 /stats - Db status  
 /broadcast - Broadcast (𝖮𝗐𝗇𝖾𝗋 𝖮𝗇𝗅𝗒)

○ <u>𝖭𝗈𝗍𝗂𝖼𝖾</u> 📙:-

𝖣𝗈𝗇𝗍 𝖲𝗉𝖺𝗆 𝖬𝖾...🤒
"""
    ABOUT_TXT = """<b>○ 𝖬𝗒 𝖭𝖺𝗆𝖾: {}
○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='https://t.me/vimukthioshada'>𝖳𝗁𝗂𝗌 𝖯𝖾𝗋𝗌𝗈𝗇</a>
○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇 𝟥 
○ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆 𝖺𝗌𝗒𝗇𝖼𝗂𝗈 𝟢.𝟣𝟩.𝟣 
○ 𝖲𝖾𝗋𝗏𝖾𝗋 : Contabo
○ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : <a href='https://www.mongodb.com'>𝖬𝗈𝗇𝗀𝗈𝖣𝖡 𝖥𝗋𝖾𝖾 𝖳𝗂𝖾𝗋</a>
○ 𝖡𝗎𝗂𝗅𝖽 𝖲𝗍𝖺𝗍𝗎𝗌 : v1.0.1 [BeTa]
○ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍 𝖦𝗋𝗈𝗎𝗉 : <a href='https://t.me/filmstudiodl'>𝖳𝖺𝗉 𝖧𝖾𝗋𝖾</a>"""
    SOURCE_TXT = """<b>NOTE:</b>
Special Thanks to EvaMaria Devs & Cloners for the codes 
<b>DEV:</b>

- <a href=https://t.me/FilmStudiohub2>『Filmstudio』</a>

- Source - https://github.com/ritheshrkrm/PiroAutoFilterBot""" #please don't change repo link give credit :)

    MANUELFILTER_TXT = """ʜᴇʟᴘ: <b>ꜰɪʟᴛᴇʀꜱ</b>
- ꜰɪʟᴛᴇʀ ɪꜱ ᴀ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ɪ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ
<b>ɴᴏᴛᴇ:</b>
1. ᴛʜɪꜱ ʙᴏᴛ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟᴇɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

Cᴏᴍᴍᴀɴᴅs Aɴᴅ Usᴀɢᴇ:

• /filter - <code>ᴀᴅᴅ ᴀ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /filters - <code>ʟɪꜱᴛ ᴀʟʟ ᴛʜᴇ ꜰɪʟᴛᴇʀꜱ ᴏꜰ ᴀ ᴄʜᴀᴛ</code>
• /del - <code>ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴛᴇʀ ɪɴ ᴀ ᴄʜᴀᴛ</code>
• /delall - <code>ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴡʜᴏʟᴇ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ (ᴄʜᴀᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- ᎯℕUℛᎯᎶ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ᎯℕUℛᎯᎶ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Am_RoBots)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of ᎯℕUℛᎯᎶ

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
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
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫  
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
