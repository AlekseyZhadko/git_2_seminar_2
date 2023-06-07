import telebot
import model_staff
from telebot import types

bot = telebot.TeleBot('5716044974:AAGzEpuCO2exGD9fEslokg2PKmZCsRCzr6Q')

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == "/start":
        bot.send_message(message.from_user.id, "Привет! ИС Сотрудники компании")
        get_mode(message)
    elif message.text.lower() == "/help":
        bot.send_message(message.from_user.id, "Для начала работы напиши /start")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def get_mode(message):
    keyboard = types.InlineKeyboardMarkup() #наша клавиатура
    key_add = types.InlineKeyboardButton(text='Добавить данные в БД', callback_data='add') 
    keyboard.add(key_add) #добавляем кнопку в клавиатуру
    key_remove= types.InlineKeyboardButton(text='Изменить данные в БД', callback_data='remove') 
    keyboard.add(key_remove) #добавляем кнопку в клавиатуру
    key_del= types.InlineKeyboardButton(text='Удалить данные в БД', callback_data='del') 
    keyboard.add(key_del) #добавляем кнопку в клавиатуру
    bot.send_message(message.from_user.id, text='Выбери действие:', reply_markup=keyboard)

def mode_add(message):
    keyboard2 = types.InlineKeyboardMarkup() #наша клавиатура
    key_staff = types.InlineKeyboardButton(text='Сотрудники', callback_data='staff') 
    keyboard2.add(key_staff) #добавляем кнопку в клавиатуру
    key_otdel= types.InlineKeyboardButton(text='Отделы', callback_data='otdel') 
    keyboard2.add(key_otdel) #добавляем кнопку в клавиатуру
    key_post= types.InlineKeyboardButton(text='Должности', callback_data='post') 
    keyboard2.add(key_post) #добавляем кнопку в клавиатуру
    key_master= types.InlineKeyboardButton(text='Сводная', callback_data='master') 
    keyboard2.add(key_master) #добавляем кнопку в клавиатуру
    bot.send_message(message.chat.id, text='Выберите таблицу:', reply_markup=keyboard2)

@bot.callback_query_handler(func=lambda query: True)
def callback_worker(call):
    if call.data == 'add': 
        bot.answer_callback_query(call.id)     
        mode_add(call.message)
    elif call.data == "remove":
        bot.answer_callback_query(call.id) 
    elif call.data == 'del':
        bot.answer_callback_query(call.id) 
    elif call.data == 'staff':
        model_staff.AddStaff(call.message)


bot.polling(none_stop=True, interval=0)