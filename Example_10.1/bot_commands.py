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
import datetime
import model_staff
from spy import *

def start_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Привет, {update.effective_user.first_name}!')
    update.message.reply_text("ИС Сотрудники компании")
    keyboard = [
        [
            InlineKeyboardButton("Добавить", callback_data="1"),
            InlineKeyboardButton("Изменить", callback_data="2"),
        ],
        [InlineKeyboardButton("Удалить", callback_data="3")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Выберите действие с БД:", reply_markup=reply_markup)

def mode_table(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton("Сотрудники", callback_data="staff"),
            InlineKeyboardButton("Должности", callback_data="post"),
        ],
        [
            InlineKeyboardButton("Отделы", callback_data="otdel"),
            InlineKeyboardButton("Сводная", callback_data="master")            
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Выберите таблицу:", reply_markup=reply_markup)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == "1":
        mode_table(query,context)
    if query.data == "staff":
        model_staff.FIO_command(query,context)
    if query.data == "post": query.message.reply_text("Данный раздел находится в разработке!")
    if query.data == "otdel": query.message.reply_text("Данный раздел находится в разработке!")
    if query.data == "master": query.message.reply_text("Данный раздел находится в разработке!")

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/start - Для начала работы с ИС \n/help - Помощь') 

