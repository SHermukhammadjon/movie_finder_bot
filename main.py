from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultCachedVideo, InlineQueryResultPhoto, InputMessageContent, InputMediaPhoto
from db import Database
import time
from random import randint
from Google import search_movi
from PyMemory import load_movi_data, RAM
from login import BOT_API_TOKEN, CHANEL_ID, ADMIN_ID, DEFOLT_CODE
from buttons import Buttons

database = Database('database.db')
database.conect()
ram = RAM(db = database)
ram.load_users()

buttons = Buttons()

def admin(update, context):
    id = update.message.chat.id
    name = update.message.chat.first_name
    if ram.check_admin(id = id):
        update.message.reply_text(f"{name} siz adminsiz!")
    else:
        update.message.reply_text(f"{name} sizda adminlik huquqi yo'q. Ilimos paro'lni kiriting.")
        ram.update_action(user_id = id, action = 'admin_login')
    # code = ram.random_code(user_id = user_id)
    # context.bot.send_message(chat_id = ADMIN_ID, text = f"Yangi admin {name}ning")

def start_function(update, context):
    id = update.message.chat.id
    name = update.message.chat.first_name
    if ram.check_user(user_id = id):
        update.message.reply_text(text = "Bosh menu:", 
                                  reply_markup = ReplyKeyboardMarkup(buttons.get_head(mode='user'), resize_keyboard = True, one_time_keyboard = True))
    elif ram.check_admin(id = id):
        update.message.reply_text(f"{name} siz adminsiz!")
    else:
        update.message.reply_text(f"Assalomu alaykum{name} xush kelibsi!")
        database.add_user(user_id = id, user_name = name)

def core_function(update, context):
    id = update.message.chat.id
    name = update.message.chat.first_name
    message = update.message.text
    if ram.check_user(user_id = id):
        where = ram.wher_user(user_id = id)
        action = ram.get_action(user_id = id)
        if where == 'head_menu':
            if action == 'admin_login':
                count = ram.block_user(user_id = id, count = True)
                if message == DEFOLT_CODE and count < 3:
                    update.message.reply_text(f"{name} xush kelibsiz! Siz endi adminsiz.")
                    ram.update_action(user_id=id, action = 'none')
                elif count > 3:
                    update.message.reply_text(f"{name} siz blo'klandingiz, keyinroq urinib ko'ring.")
                    ram.update_action(user_id=id, action = 'none')
                else:
                    update.message.reply_text("Notog'ri paro'l !")
                    ram.block_user(user_id = id)
            
            else:
                pass

        # update.message.reply_text(f"{name} is user !")
    elif ram.check_admin(id = id):
        update.message.reply_text(f"{name} is admin !")
    else:
        update.message.reply_text(f"Assalomu alaykum{name} xush kelibsi!")
        database.add_user(user_id = id, user_name = name)

n = 0
def video_handler(update, context):
    pass

#AAMCAQADGQEAAg7hZGS6qOSrBko3wcVvJ2KEGrqE-LMAApkCAAIhxDlH6O_gdxKk1vkBAAdtAAMvBA

titles, movies_dataset, line_count = load_movi_data()
# response = requests.get('https://picsum.photos/100/100')
# response = response.url

def query(update, context):
    query = update.inline_query.query
    if len(query) > 3:
        global movies_dataset, titles
        indexs = search_movi(query, titles = titles, limt = 30)

        answers = []
        n = 0
        for index in indexs:
            # response = requests.get('https://picsum.photos/100/100')
            # response = response.url
            movie = movies_dataset[index]
            answers.append(InlineQueryResultArticle(id = str(n), 
                                        title = movie['title'],
                                        description = movie['caption'],
                                        input_message_content = InputTextMessageContent(f"/get {index}"),
                                        thumb_url = f'https://picsum.photos/id/{randint(10, 500)}/100/100',
                                        # thumb_url = f'127.0.0.1:8000/get',
                                        thumb_height = 100,
                                        thumb_width = 200))
            n+=1
        #     print(n)
        # print("answer")
        update.inline_query.answer(answers)

def get_movie(update, context):
    global movies_dataset
    id = update.message.chat.id
    message_id = update.message.message_id
    message = update.message.text
    index = message[5:]

    context.bot.delete_message(chat_id = id, message_id = message_id)
    if index.isdigit():
        movie = movies_dataset[int(index)]
        context.bot.send_video(chat_id = id, video = movie['file_id'], caption = movie['caption'])

        

    
def main():
    updater = Updater(token = BOT_API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('admin', admin))
    dispatcher.add_handler(CommandHandler('start', start_function))
    dispatcher.add_handler(CommandHandler('get', get_movie))

    dispatcher.add_handler(MessageHandler(Filters.text, core_function))
    dispatcher.add_handler(MessageHandler(Filters.video, video_handler))

    dispatcher.add_handler(InlineQueryHandler(query))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    print("Starting bot ...")