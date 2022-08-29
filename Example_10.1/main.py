from credits import *
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *
from model_staff import *

updater = Updater(bot_token)
updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('FIO', FIO_command))
updater.dispatcher.add_handler(CommandHandler('phone', phone_command))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()


