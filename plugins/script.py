from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Script(object):



    START_TEXT = """
Hey {} 

Ben altyazı gömme botuyum

Srt ve aas destekliyorum

Help Komutunu kullan. 

Yapan 💕 By @mmagneto
"""
    HELP_TEXT = """
Bilmiyosan kullanma dostum
"""
    ABOUT_TEXT = """
SİKTİR ET
 
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Apdeyt Çenıl', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 sapırt Grup', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ kapat', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Ev', callback_data='home'),
        InlineKeyboardButton('👲 Hakkımda', callback_data='about'),
        InlineKeyboardButton('⛔ kapat', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Ev', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Kapat', callback_data='close')
        ]]
    )
