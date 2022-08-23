import telebot
from telebot import types

bot = telebot.TeleBot('5716044974:AAGzEpuCO2exGD9fEslokg2PKmZCsRCzr6Q')
candys = 2021
user_1 = 1
user_1_candy = 0
candy = 0

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, "Привет, Игра 2021 конфета")
        bot.send_message(message.from_user.id, "Готов играть? напиши старт")
        bot.register_next_step_handler(message,get_mode)
    else:
        bot.send_message(message.from_user.id, 'Напиши Привет')

def get_mode(message):
    if message.text.lower() =='старт': #проверяем что возраст изменился
        keyboard = types.InlineKeyboardMarkup() #наша клавиатура
        key_yes = types.InlineKeyboardButton(text='Игрок против Игрока', callback_data='game_user_vs_user') #кнопка «Игрок против игрока»
        keyboard.add(key_yes) #добавляем кнопку в клавиатуру
        key_no= types.InlineKeyboardButton(text='Игрок против Компьютера', callback_data='game_user_vs_comp') #кнопка «Игрок против компьютера»
        keyboard.add(key_no) #добавляем кнопку в клавиатуру
        bot.send_message(message.from_user.id, text='Выбери режим игры:', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Напиши Cтарт')

@bot.callback_query_handler(func=lambda query: True)
def callback_worker(call):
    if call.data == "game_user_vs_user": 
        bot.answer_callback_query(call.id) 
        get_mode_user_vs_user(call.message)
    elif call.data == "game_user_vs_comp":
        bot.answer_callback_query(call.id) 
        get_mode_comp_vs_user(call.message)

def get_mode_comp_vs_user(message):
    bot.send_message(message.chat.id,'Ваш ход, Введите число конфет от 1 до 28:')
    bot.register_next_step_handler(message,game_comp_vs_user)
    
def get_mode_user_vs_user(message):
    bot.send_message(message.chat.id,'Ходит Игрок 1, Введите число конфет от 1 до 28:')
    bot.register_next_step_handler(message,game_user_vs_user)

def filter(message):
    bot.send_message(message.from_user.id, 'Неверно введено значение')
    bot.send_message(message.chat.id,'Введите число конфет от 1 до 28:')
    bot.register_next_step_handler(message,game_comp_vs_user)

def game_user_vs_user(message):
    global candy
    global candys
    global user_1
    try:
        if int(message.text):
            if (int(message.text)<1 or int(message.text)>28):
                raise Exception       
    except Exception:
        bot.register_next_step_handler(message,filter)
    else:
        if user_1 == 1: 
            user_1 = 0
            candy = int(message.text)
            candys-=candy
            if candys <= 0:
                candys=0
                bot.send_message(message.chat.id,f'Осталось конфет: {candys}')
                bot.send_message(message.chat.id,'Победа Игрока 1!')
                bot.register_next_step_handler(message,start)
            else:
                bot.send_message(message.chat.id,f'Осталось конфет: {candys}')
                bot.send_message(message.chat.id,'Ходит Игрок 2, Введите число конфет от 1 до 28:')
                bot.register_next_step_handler(message,game_user_vs_user)
        elif user_1 == 0:
            user_1 = 1
            candy = int(message.text)
            candys-=candy
            if candys <= 0:
                candys=0
                bot.send_message(message.chat.id,f'Осталось конфет: {candys}')
                bot.send_message(message.chat.id,'Победа Игрока 2!')
                bot.register_next_step_handler(message,start)
            else:
                bot.send_message(message.chat.id,f'Осталось конфет: {candys}')
                bot.send_message(message.chat.id,'Ходит Игрок 1, Введите число конфет от 1 до 28:')
                bot.register_next_step_handler(message,game_user_vs_user)

def game_comp_vs_user(message):
    global candy
    global candys
    global user_1
    try:
        if int(message.text):
            if (int(message.text)<1 or int(message.text)>28):
                raise Exception       
    except Exception:
        bot.register_next_step_handler(message,filter)
    else:
        candy = int(message.text)
        candys-=candy
        user_1_candy=candy
        if candys <= 0:
            candys=0
            bot.send_message(message.chat.id,f'Осталось конфет: {candys}')
            bot.send_message(message.chat.id,'Вы победили!')
            bot.register_next_step_handler(message,start)
        else:
            bot.send_message(message.chat.id,f'Осталось конфет: {candys}')
            candy=29-user_1_candy
            bot.send_message(message.chat.id,f'Компьютер взял {candy} конфет')
            candys-=candy
            if candys <= 0:
                candys=0
                bot.send_message(message.chat.id,f'Осталось конфет: {candys}')
                bot.send_message(message.chat.id,'Победил компрьютер!')
            else:
                bot.send_message(message.chat.id,f'Осталось конфет: {candys}')
                bot.send_message(message.chat.id,'Ваш ход, Введите число конфет от 1 до 28:')
                bot.register_next_step_handler(message,game_comp_vs_user)
    
bot.polling(none_stop=True, interval=0)