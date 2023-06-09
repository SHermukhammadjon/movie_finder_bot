from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultCachedVideo
from movie_finder_bot.db import Database
import time
from random import randint
from movie_finder_bot.Google import search_movi
from movie_finder_bot.PyMemory import load_movi_data

API_TOKEN = "6080581500:AAHnIOY5m2wjqjE_uQUDMFAvLBC0L97eo20"
CHANEL_ID = '-1001942672781'
ADMINS = [1661189380]

database = Database('dataset/database.db')
database.conect()

def start_function(update, context):
    user_name = update.message.chat.first_name
    update.message.reply_text(f"Salom {user_name}!")

n = 0
def video_handler(update, context):
    global n
    n+=1
    user_id = update.message.chat.id
    if n == 20:
        n = 0
        sleep = randint(40, 120)
        
        print(f"sleep {sleep} second...")
        time.sleep(sleep)
    if user_id in ADMINS:
        try:
            video = update.message.video
            if int(video.file_size / (1024*1024)) > 100:
                caption = update.message.caption
                vm_info = context.bot.send_video(CHANEL_ID, video, caption = caption)

                message_id = vm_info.message_id
                file_size = vm_info.video.file_size
                file_id = vm_info.video.file_id
                database.add_movi(caption, file_id = file_id, size = file_size, message_id = message_id)
                thumb_file = context.bot.get_file(video.thumb.file_id)
                thumb_file.download(f"photos/{message_id}.jpg")
                print(video.thumb.file_id)
                # update.message.reply_photo(open('thumbnail.jpg', 'rb'))
                # print(vm_info)
            else:
                update.message.reply_text("The video size is smoller then 100 Mb")
                print("! The video size is smoller then 100 Mb ")
        except:
            print('Video handler EROR ...')


    # print(update.message)
    # chat_id = update.message.chat.id
    # message_id = update.message.message_id
    # video = update.message.video
    # print(video)
    
    # message_info = context.bot.send_video(chat_id, video)
    # print(message_info)

def cleaner(update, context):
    print("All data cleaned! ")
    decison = input("Is your decision certain?\n>>>")
    
def main():
    updater = Updater(token = API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_function))
    dispatcher.add_handler(CommandHandler('clear', cleaner))
    dispatcher.add_handler(MessageHandler(Filters.video, video_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    print("Starting bot ...")