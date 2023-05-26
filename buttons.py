from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent


class Buttons:
    def __init__(self):
        pass
    def get_head(self, mode = 'admin'):
        if mode == 'admin':
            pass
        elif mode == 'user':
            buttons = [[KeyboardButton(text = "🔍 kino izlash")],
                       [KeyboardButton(text = "🎲 tasodifiy"), KeyboardButton(text = "🏆Top 100")],
                       [KeyboardButton(text = "⭐️ Saqlangan kinolar"), KeyboardButton(text = "🧪Kino qo'shish")],
                       [KeyboardButton(text = "📲 Aloqa"), KeyboardButton(text = "⚙️ Sozlamalar")],
                       [KeyboardButton(text = "📈 statistika")]]
            return buttons
        