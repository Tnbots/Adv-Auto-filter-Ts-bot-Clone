#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG | @Hillard_Har 

class Translation(object):
    
    START_TEXT = """
😅 Hai {}, 

I am a filter bot with advanced features 
currently working for @{} 

⚜️ 𝐌𝐚𝐢𝐧𝐭𝐚𝐢𝐧𝐞𝐝 𝐁𝐲 👉 @{}

START_IMG = os.environ.get('START_IMG', None)
if START_IMG is None:
    img = "https://telegra.ph/file/fc734b227985a1524e715.jpg"
else:
  img = START_IMG    
"""   
    
    HELP_TEXT = """
<u>💡 𝐇𝐞𝐥𝐩</u>
Not for u
"""
    
    ABOUT_TEXT = """
📕 𝐀𝐛𝐨𝐮𝐭 𝐌𝐞 ,
\n○ ᴍʏ ɴᴀᴍᴇ : {}

○ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 

○ ғʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏʀᴏɢʀᴀᴍ 

○ sᴇʀᴠᴇʀ : ʜᴇʀᴏᴋᴜ 

○ ᴠᴇʀsɪᴏɴ : 1.0.0

ᴄʀᴇᴀᴛᴏʀ : [Blasters Links](https://t.me/blasters_links)

**[© Blasters Links](https://t.me/blasters_links)**
"""
