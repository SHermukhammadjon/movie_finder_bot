from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup


class Buttons:
    def __init__(self):
        pass
    def get_headin(self, mode = 'admin'):
        if mode == 'user':
            buttons = [[InlineKeyboardButton(text = "📄 Qo'lanma", callback_data = "manual" ), InlineKeyboardButton(text = "⬇️ Ko'proq", callback_data = "more")],
                       [InlineKeyboardButton(text = "🔍 Kino Izlash", switch_inline_query_current_chat = "")]]
            return InlineKeyboardMarkup(keyboard = buttons)
        elif mode == 'admin':
            buttons = [[InlineKeyboardButton(text = "📄 Qo'lanma", callback_data = "manual" ), InlineKeyboardButton(text = "⬇️ Ko'proq", callback_data = "more")],
                       [InlineKeyboardButton(text = "🔍 Kino Izlash", switch_inline_query_current_chat = "")]]
            return InlineKeyboardMarkup(inline_keyboard = buttons)
    
    def get_headin_more(self, mode = 'admin'):
        if mode == 'user':
            buttons = [[InlineKeyboardButton(text = "⭐️ Saqlanganlar", callback_data = "saved"), InlineKeyboardButton(text = "⚡️ Primyeralar", callback_data = "premier")],
                       [InlineKeyboardButton(text = "🎲 Tasodifiy", callback_data = "random"), InlineKeyboardButton(text = "🏆 Top 100", callback_data = "top")],
                       [InlineKeyboardButton(text = "🧪 Kino qo'shish", callback_data = "add_movi"), InlineKeyboardButton(text = "📲 Aloqa", callback_data = "contact")],
                       [InlineKeyboardButton(text = "📈 Statistika", callback_data = "statistics")],
                       [InlineKeyboardButton(text = "📄 Qo'lanma", callback_data = "manual" ), InlineKeyboardButton(text = "⬆️ Kamroq", callback_data = "less")],
                       [InlineKeyboardButton(text = "🔍 Kino Izlash", switch_inline_query_current_chat = "")]]
            return buttons 
        
        elif mode == 'admin':
            buttons = [[InlineKeyboardButton(text = "⭐️ Saqlanganlar", callback_data = "saved"), InlineKeyboardButton(text = "⚡️ Primyeralar", callback_data = "premier")],
                       [InlineKeyboardButton(text = "🎲 Tasodifiy", callback_data = "random"), InlineKeyboardButton(text = "🏆 Top 100", callback_data = "top")],
                       [InlineKeyboardButton(text = "📄 Qo'lanma", callback_data = "manual" ), InlineKeyboardButton(text = "⬆️ Kamroq", callback_data = "less")],
                       [InlineKeyboardButton(text = "🔍 Kino Izlash", switch_inline_query_current_chat = "")]]
            return buttons
    
    def get_menu(self, mode = 'admin'):
        if mode == 'user':
            buttons = [[KeyboardButton(text="🎛 Menu"), KeyboardButton(text = "⚙️ Sozlamalar")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
        elif mode == 'admin':
            buttons =[[KeyboardButton(text = "🎛 Menu")],
                      [KeyboardButton(text = "📂 Media"), KeyboardButton(text = "📦 Review")],
                      [KeyboardButton(text = "✉️ Xabarlar"), KeyboardButton(text = "⚙️ Sozlamalar")],
                      [KeyboardButton(text = "📈 Statistika")]]
            return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
        
    def get_media(self):
        buttons = [[KeyboardButton(text = "🎬 Kino qo'shish"), KeyboardButton(text = "📺 Serial qo'shish")],
                   [KeyboardButton(text = "🔥 Primyeralarni taxrirlash"), KeyboardButton(text = "🧩 Yangi medialarga   ishlov berish")],
                    [KeyboardButton(text = "⬅️ Orqaga")]]
        return ReplyKeyboardMarkup(keyboard = buttons, resize_keyboard = True)
    
    def add_movi(self, mode = 'none'):
        if mode == 'none':
            buttons = [[KeyboardButton(text = "♻️ Avtomatik"), KeyboardButton(text = "👊 Qo'lda")],
                       [KeyboardButton(text = "👷🏻‍♂️ Kinolarga ishlov berish")],
                       [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]]
            return buttons 
        if mode == 'avto':
            buttons = [[KeyboardButton(text = "♻️ Avtomatik 🔵"), KeyboardButton(text = "👊 Qo'lda")],
                       [KeyboardButton(text = "👷🏻‍♂️ Kinolarga ishlov berish")],
                       [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]]
            return buttons
        if mode == 'hend':
            buttons = [[KeyboardButton(text = "♻️ Avtomatik"), KeyboardButton(text = "👊 Qo'lda 🔵")],
                       [KeyboardButton(text = "👷🏻‍♂️ Kinolarga ishlov berish")],
                       [KeyboardButton(text = "⬅️ Orqaga"), KeyboardButton(text = "🏠 Bosh sahifa")]]
            return buttons 
        