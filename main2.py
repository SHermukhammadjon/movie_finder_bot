import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import time
import asyncio

from login import BOT_API_TOKEN
from PyMemory import RAM, load_movi_data
from db import Database
from buttons import Buttons
from admin import admin_core

from Google import search_movi

database = Database('database.db')
database.conect()
ram = RAM(db = database)
ram.load_data()

buttons = Buttons()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token = BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    id = message.chat.id
    name = message.chat.first_name
    if ram.check_admin(id = id):
        data = ram.get_admin(id = id) 
        # where = data['where']
        # name = data['name']
        date = data['registred']
        await message.answer(f"Ro'yxatdan o'tilgan vaxt2: {date}", reply_markup = buttons.get_menu(mode = 'admin'))
        data['where'] = 'head_menu'
        ram.update_admin(id = id, admin_data = data)

@dp.message_handler(commands = ['get'])
async def get_command(message: types.Message):
    global movies_dataset
    id = message.chat.id
    text = message.text
    message_id = message.message_id
    index = text[5:]
    if index.isdigit():
        movie = movies_dataset[int(index)]
        await bot.delete_message(chat_id = id, message_id = message_id)
        await bot.send_video(chat_id = id, video = movie['file_id'], caption = movie['caption'])
        # context.bot.send_video(chat_id = id, video = movie['file_id'], caption = movie['caption'])
    
      
# def get_movie(update, context):
#     global movies_dataset
#     id = update.message.chat.id
#     message_id = update.message.message_id
#     message = update.message.text
#     index = message[5:]

#     context.bot.delete_message(chat_id = id, message_id = message_id)
#     if index.isdigit():
#         movie = movies_dataset[int(index)]
#         context.bot.send_video(chat_id = id, video = movie['file_id'], caption = movie['caption'])


@dp.message_handler()
async def message_handler(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    id = message.chat.id
    name = message.chat.first_name
    text = message.text
    
    if ram.check_admin(id = id):
        data = ram.get_admin(id = id) 
        where = data['where']
        # name = data['name']
        date = data['registred']
        
        if where == 'head_menu':
            if text == "📂 Media":
                await message.answer("Media menyusi:", reply_markup = buttons.get_media())
                data['where'] = 'media'
                ram.update_admin(id = id, admin_data = data)
            elif text == "🎛 Menu":
                await message.answer("Menyu: ", reply_markup = buttons.get_headin(mode = 'admin'))

        if where == 'media':
            if text == "⬅️ Orqaga":
                await message.answer(f"Bosh menyu:", reply_markup = buttons.get_menu(mode = 'admin'))
                data['where'] = 'head_menu'
                ram.update_admin(id = id, admin_data = data)
        
        elif where == 'none':
            await message.answer(f"Ro'yxatdan o'tilgan vaxt: {date}", reply_markup = buttons.get_menu(mode = 'admin'))
            data['where'] = 'head_menu'
            ram.update_admin(id = id, admin_data = data)
        
            
        
        
        
    
    # await message.answer(message.text)

# @dp.message_handler(content_types = types.ContentType.VIDEO)
# async def video_handler(message: types.Message):
#     print(message)
#     await asyncio.sleep(10)

    
    
#     await message.reply("Video yuklandi !")


titles, movies_dataset, line_count = load_movi_data()
@dp.inline_handler()
async def inline_search(query: types.InlineQuery):
    text = query.query
    if len(text) > 3:
        global movies_dataset, titles
        indexs = search_movi(text, titles = titles, limt = 30)
        answers = []
        n = 0

        for index in indexs:
            movie = movies_dataset[index]
            answers.append(types.InlineQueryResultArticle(id = str(n), 
                                                              title = movie['title'],
                                                              thumb_url = f'https://telegra.ph/file/62785ec3c606da79ad966.jpg',
                                                              input_message_content = types.InputTextMessageContent(message_text = f"/get {index}")))
            n+=1
 
        await query.answer(answers)



    
    
    


    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)