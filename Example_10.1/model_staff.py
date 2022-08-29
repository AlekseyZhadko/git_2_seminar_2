from telegram import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Update
)
from telegram.ext import (
    MessageHandler,
    Filters,
    Updater, 
    CommandHandler, 
    CallbackContext, 
    CallbackQueryHandler, 
    ContextTypes
)
import json
import os
from spy import log
FIO = ''
phone = ''

def AddStaff(update: Update, context: CallbackContext):
    data = {}
    data['staff'] = []
    with open('Example_10.1/Staff.json','r', encoding='utf-8') as fh:            
        if os.stat('Example_10.1/Staff.json').st_size == 0:
            data['staff'].append({
                'ID': '0',
                'FIO': FIO,
                'phone': phone
            })
        else:
            data = json.load(fh)
            data['staff'].append({
                'ID': str(int(data['staff'][len(data['staff'])-1]['ID'])+1),
                'FIO': FIO,
                'phone': phone
            })
    with open('Example_10.1/Staff.json','w', encoding='utf-8') as fh:
        fh.write(json.dumps(data,indent=4,ensure_ascii=False))

def FIO_command(query: Update, context: CallbackContext):
    global FIO
    query.message.reply_text("Введите ФИО:")
    log(query, context)
    msg = query.message.text
    print(msg)
    query.message.reply_text(f'Вы ввели? {msg}')
    FIO = msg
    phone_command(query,context)

def phone_command(update: Update, context: CallbackContext):
    global phone
    update.message.reply_text("Введите телефон:")
    log(update, context)
    msg = update.message.text
    print(msg)
    update.message.reply_text(f'Вы ввели? {msg}')
    phone = msg
    AddStaff(update,context)
