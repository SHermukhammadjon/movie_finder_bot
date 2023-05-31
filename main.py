from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup
from db import Database
import time
from random import randint
from Google import search_movi
from PyMemory import load_movi_data, RAM
from login import BOT_API_TOKEN, CHANEL_ID, ADMIN_ID, DEFOLT_CODE
from buttons import Buttons
from picsum import now
# from extractor import video_extractor
from admin import admin_core
import asyncio

database = Database('database.db')
database.conect()
ram = RAM(db = database)
ram.load_data()

buttons = Buttons()

def admin(update, context):
    id = update.message.chat.id
    name = update.message.chat.first_name

    if ram.check_admin(id = id) :
        update.message.reply_text(f"{name} sizda adminlik huquqi bor")
    elif ram.check_user(user_id = id):
        count = ram.block_user(user_id = id, count = True)
        if count <= 3:
            update.message.reply_text(f"{name} sizda adminlik huquqi yo'q. Ilimos paro'lni kiriting.")
            ram.update_user_action(user_id = id, action = 'admin_login')
        else:
            update.message.reply_text(f"{name} keyinroq urinib ko'ring !")
    else:
        date = now()
        update.message.reply_text(text = f"Ro'yxatdan o'tilgan vaxt: {date}\nAssalomu alaykum{name} xush kelibsi!",
                                  reply_markup = InlineKeyboardMarkup(buttons.get_headin(mode='user')))
        
        database.add_user(user_id = id, user_name = name, registr_time = date)
        ram.add_user(id = id, name=name, registred_time = date)


    

def start_function(update, context):
    id = update.message.chat.id
    name = update.message.chat.first_name
    print(update.message)
    if ram.check_user(user_id = id):
        user_data = ram.get_user(user_id = id)
        update.message.reply_text(
                                  text = "Bosh menu:", 
                                  reply_markup = ReplyKeyboardMarkup(buttons.get_menu(mode = 'user'), 
                                  resize_keyboard = True, 
                                  one_time_keyboard = True)
                                  )
        update.message.reply_text(text = f"Ro'yxatdan o'tilgan vaxt : {user_data['registred']}\n🍿 {user_data['name']} siz bosh menyudasiz. \n\n🔍 Men sizga kino topishga yordam beraman.", 
                                  reply_markup = InlineKeyboardMarkup(buttons.get_headin(mode = 'user')))
                                 
    elif ram.check_admin(id = id):
        admin_data = ram.get_admin(id = id)
        update.message.reply_text(f"Ro'yxatdan o'tilgan vaxt: {admin_data['registred']}\n🍿 Assalomu alaykum {admin_data['name']}, siz adminsiz!",
                                  reply_markup = ReplyKeyboardMarkup(buttons.get_menu(mode = 'admin'), 
                                  resize_keyboard = True, 
                                  one_time_keyboard = True))
        
    else:
        date = now()
        update.message.reply_text(text = f"Ro'yxatdan o'tilgan vaxt: {date}\nAssalomu alaykum{name} xush kelibsi!",
                                  reply_markup = InlineKeyboardMarkup(buttons.get_headin(mode='user')))
        
        database.add_user(user_id = id, user_name = name, registr_time = date)
        ram.add_user(id = id, name=name, registred_time = date)

def core_function(update, context):
    id = update.message.chat.id
    name = update.message.chat.first_name
    message = update.message.text

    if ram.check_user(user_id = id):
        where = ram.wher_user(user_id = id)
        action = ram.get_action(user_id = id)
        if where == 'head_menu':
            if action == 'admin_login':
                # print(message)
                count = ram.block_user(user_id = id, count = True)
                if message == DEFOLT_CODE and count <= 3:
                    update.message.reply_text(f"{name} siz endi adminsiz.")
                    
                    ram.remove_user(id = id)
                    ram.add_admin(name = name, id = id, registred_time = now())
                    
                    database.remove_user(user_id = id)
                    database.add_admin(id = id, name = name, registred_time = now())
                    
                elif count > 3:
                    update.message.reply_text(f"{name} siz blo'klandingiz, keyinroq urinib ko'ring.")
                    ram.update_user_action(user_id=id, action = 'none')
                else:
                    update.message.reply_text("Notog'ri paro'l !")
                    ram.block_user(user_id = id)
            
            if message == "🔍 Kino izlash":
                update.message.reply_text(text = "Kino izlash")
        elif where == 'none':
            update.message.reply_text(text = 'Bosh menu', reply_markup = ReplyKeyboardMarkup(buttons.get_headin(mode='user')))
            admin_data['where'] = 'head_menu'
            ram.update_admin(id = id, admin_data = admin_data)

        # update.message.reply_text(f"{name} is user !")
    
    elif ram.check_admin(id = id):
        admin_core(update, context, ram = ram, buttons=buttons)
    
    else:
        update.message.reply_text(f"Assalomu alaykum{name} xush kelibsi!")
        database.add_user(user_id = id, user_name = name)
        ram.add_user(id = id, name=name)

async def video_adder(update, contex):
    print(10)

n = 0
def video_handler(update, context):
    # id = update.message.chat.id
    # if ram.check_admin(id = id):
    #     admin_data = ram.get_admin(id = id) 
    #     where = admin_data['where']
    #     action = admin_data['action']
    #     name = admin_data['name']
    #     date = admin_data['registred']
    #     global n
    #     # print(where)
    #     # print(action)
    #     if where == 'add_movi':
    #         if action == 'avto_add':
    print('working...')
    asyncio.create_task(video_adder)
                


         
        
    # global n
    # n+=1
    # user_id = update.message.chat.id
    # if n == 20:
    #     n = 0
    #     sleep = randint(40, 120)
        
    #     print(f"sleep {sleep} second...")
    #     time.sleep(sleep)
    # if user_id in ADMINS:
    #     try:
    #         video = update.message.video
    #         if int(video.file_size / (1024*1024)) > 100:
    #             caption = update.message.caption
    #             vm_info = context.bot.send_video(CHANEL_ID, video, caption = caption)

    #             message_id = vm_info.message_id
    #             file_size = vm_info.video.file_size
    #             file_id = vm_info.video.file_id
    #             database.add_movi(caption, file_id = file_id, size = file_size, message_id = message_id)
    #             thumb_file = context.bot.get_file(video.thumb.file_id)
    #             thumb_file.download(f"photos/{message_id}.jpg")
    #             print(video.thumb.file_id)
    #             # update.message.reply_photo(open('thumbnail.jpg', 'rb'))
    #             # print(vm_info)
    #         else:
    #             update.message.reply_text("The video size is smoller then 100 Mb")
    #             print("! The video size is smoller then 100 Mb ")
    #     except:
    #         print('Video handler EROR ...')

titles, movies_dataset, line_count = load_movi_data()

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
                                        #thumb_url = f'https://picsum.photos/id/{randint(10, 500)}/100/100',#https://telegra.ph/file/62785ec3c606da79ad966.jpg
                                        thumb_url = f'https://telegra.ph/file/62785ec3c606da79ad966.jpg',
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


def inlen_core(update, context):
    data = update.callback_query.data
    query = update.callback_query
    id = query.message.chat.id
    if ram.check_user(user_id = id):
        if data == 'more':
            query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup(buttons.get_headin_more(mode='user')))
        elif data == 'less':
            query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup(buttons.get_headin(mode='user')))
    elif ram.check_admin(id = id):
        if data == 'more':
            query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup(buttons.get_headin_more(mode='admin')))
        elif data == 'less':
            query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup(buttons.get_headin(mode='admin')))
   
def main():
    updater = Updater(token = BOT_API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('admin', admin))
    dispatcher.add_handler(CommandHandler('start', start_function))
    dispatcher.add_handler(CommandHandler('get', get_movie))

    dispatcher.add_handler(MessageHandler(Filters.text, core_function))
    dispatcher.add_handler(MessageHandler(Filters.video, video_handler))

    dispatcher.add_handler(InlineQueryHandler(query))
    dispatcher.add_handler(CallbackQueryHandler(inlen_core))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    print("Starting bot ...")