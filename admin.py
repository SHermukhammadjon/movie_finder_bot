# from main import ram, buttons
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler, CallbackQueryHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup
from picsum import now



def admin_core(update, context, ram = None, buttons = None):
    id = update.message.chat.id
    name = update.message.chat.first_name
    message = update.message.text
    
    admin_data = ram.get_admin(id = id) 
    where = admin_data['where']
    name = admin_data['name']
    date = admin_data['registred']
 
    if where == 'head_menu':
        if message == "🎛 Menu":
            update.message.reply_text(f"Ro'yxatdan o'tilgan vaxt: {date}\n🍿 Menu:",
                                reply_markup = InlineKeyboardMarkup(buttons.get_headin(mode = 'admin')))
        elif message == "📂 Media":
                update.message.reply_text(text = "Media menusi:",
                                          reply_markup = ReplyKeyboardMarkup(buttons.media(),
                                                                             resize_keyboard = True,
                                                                             one_time_keyboard = True))
                admin_data['where'] = 'media'
                ram.update_admin(id = id, admin_data = admin_data)
        
    elif where == 'media':
            
        if message == "⬅️ Orqaga":
            update.message.reply_text('Admin panel:',
                                          reply_markup = ReplyKeyboardMarkup(buttons.get_menu(mode = 'admin'), resize_keyboard = True, one_time_keyboard = True))
            admin_data['where'] = 'head_menu'
            ram.update_admin(id = id, admin_data = admin_data)
                
        elif message == "🎬 Kino qo'shish":

            update.message.reply_text('Kino qo\'shi menyusi:',
                                reply_markup = ReplyKeyboardMarkup(buttons.add_movi(), resize_keyboard = True, one_time_keyboard = True))
            admin_data['where'] = 'add_movi'
            ram.update_admin(id = id, admin_data = admin_data)
                
        
    elif where == 'add_movi':
            
        if message == "⬅️ Orqaga":
            update.message.reply_text(text = "Media menusi:",
                                          reply_markup = ReplyKeyboardMarkup(buttons.media(), resize_keyboard = True, one_time_keyboard = True))
            admin_data['where'] = 'media'
            admin_data['action'] = 'none'
            ram.update_admin(id = id, admin_data = admin_data)
            
            
        elif message == "🏠 Bosh sahifa":
            update.message.reply_text('Admin panel:',
                                reply_markup = ReplyKeyboardMarkup(buttons.get_menu(mode = 'admin'), 
                                  resize_keyboard = True, 
                                  one_time_keyboard = True))
            admin_data['where'] = 'head_menu'
            admin_data['action'] = 'none'
            ram.update_admin(id = id, admin_data = admin_data)
                
        elif message in ["♻️ Avtomatik", "♻️ Avtomatik 🔵"]:
            update.message.reply_text('Avtomatik kino qo\'shish rejimi ishga tushurildi',
                                  reply_markup = ReplyKeyboardMarkup(buttons.add_movi(mode = 'avto'), resize_keyboard = True, one_time_keyboard = True))
            admin_data['action'] = 'avto_add'
            ram.update_admin(id = id, admin_data = admin_data)
                
        elif message in ["👊 Qo'lda", "👊 Qo'lda 🔵"]:
            update.message.reply_text('Qo\'lda kino qo\'shish rejimi ishga tushurildi',
                                  reply_markup = ReplyKeyboardMarkup(buttons.add_movi(mode = 'hend'), resize_keyboard = True, one_time_keyboard = True))
            admin_data['action'] = 'add_hend'
            ram.update_admin(id = id, admin_data = admin_data)
                
        elif message == "👷🏻‍♂️ Kinolarga ishlov berish":
            pass
            
    elif where == 'add_movi':
            
        if message == "⬅️ Orqaga":
            update.message.reply_text(text = "Media menusi:",
                                          reply_markup = ReplyKeyboardMarkup(buttons.media(), resize_keyboard = True, one_time_keyboard = True))
            admin_data['where'] = 'media'
            admin_data['action'] = 'none'
            ram.update_admin(id = id, admin_data = admin_data)
            
            
        elif message == "🏠 Bosh sahifa":
            update.message.reply_text('Admin panel:',
                                  reply_markup = ReplyKeyboardMarkup(buttons.get_menu(mode = 'admin'), 
                                  resize_keyboard = True, 
                                  one_time_keyboard = True))
            admin_data['where'] = 'head_menu'
            admin_data['action'] = 'none'
            ram.update_admin(id = id, admin_data = admin_data)
                
        elif message in ["♻️ Avtomatik", "♻️ Avtomatik 🔵"]:
            update.message.reply_text('Avtomatik kino qo\'shish rejimi ishga tushurildi',
                                  reply_markup = ReplyKeyboardMarkup(buttons.add_movi(mode = 'avto'), resize_keyboard = True, one_time_keyboard = True))
            admin_data['action'] = 'avto_add'
            ram.update_admin(id = id, admin_data = admin_data)
                
        elif message in ["👊 Qo'lda", "👊 Qo'lda 🔵"]:
            update.message.reply_text('Qo\'lda kino qo\'shish rejimi ishga tushurildi',
                                  reply_markup = ReplyKeyboardMarkup(buttons.add_movi(mode = 'hend'), resize_keyboard = True, one_time_keyboard = True))
            admin_data['action'] = 'add_hend'
            ram.update_admin(id = id, admin_data = admin_data)
                
        elif message == "👷🏻‍♂️ Kinolarga ishlov berish":
            pass
            
    elif where == 'none':
        update.message.reply_text('Admin panel:',
                                  reply_markup = ReplyKeyboardMarkup(buttons.get_menu(mode = 'admin'), 
                                  resize_keyboard = True, 
                                  one_time_keyboard = True))
        admin_data['where'] = 'head_menu'
        ram.update_admin(id = id, admin_data = admin_data)
