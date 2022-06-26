import os
import logging

import keyboard as keyboard
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Bot
import re
# re.match(r"\w\d[-: ]\w\d", "B3 B4")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


class MainBot:
    def __init__(self):
        load_dotenv()
        self.updater = Updater(os.getenv('TOKEN'))
        self.dp = self.updater.dispatcher
        self.bot = Bot(token=os.getenv('TOKEN'))

    def start(self, update, context):
        keyboard_start = [['Начать новую игру'], ['Помощь', 'Статистика']]
        markup = ReplyKeyboardMarkup(keyboard=keyboard_start, resize_keyboard=False, one_time_keyboard=False)
        update.message.reply_text(text='Выберете раздел, нажав на кнопку', reply_markup=markup)
        print(update)

    def help(self, update, context):
        self.bot.send_message(chat_id=update.message.chat.id, text='Это раздел "Помощь"')

    def statistic(self, update, context):
        self.bot.send_message(chat_id=update.message.chat.id, text='Это раздел "Статистика"')

    def back_func(self, update, context):
        self.start(update, context)

    def create_game(self, update, context):
        self.bot.send_message(chat_id=update.message.chat.id, text='Создать игру')

    def connect_game(self, update, context):
        self.bot.send_message(chat_id=update.message.chat.id, text='Присоединиться к игре')

    def new_game(self, update, context):
        keyboard_new_game = [['Создать комнату'], ['Присоединиться к комнате'], ['Назад']]
        markup = ReplyKeyboardMarkup(keyboard=keyboard_new_game, one_time_keyboard=False)
        self.bot.send_message(chat_id=update.message.chat.id, text='test', reply_markup=markup)
        self.dp.add_handler(MessageHandler(Filters.regex('^Создать комнату$'), self.create_game))
        self.dp.add_handler(MessageHandler(Filters.regex('^Присоединиться к комнате$'), self.connect_game))
        self.dp.add_handler(MessageHandler(Filters.regex('^Назад$'), self.back_func))

    def main(self):
        self.dp.add_handler(MessageHandler(Filters.regex('^Начать новую игру$'), self.new_game))
        self.dp.add_handler(MessageHandler(Filters.regex('^Помощь$'), self.help))
        self.dp.add_handler(MessageHandler(Filters.regex('^Статистика$'), self.statistic))
        self.dp.add_handler(CommandHandler(command='start', callback=self.start))
        self.updater.start_polling()
        self.updater.idle()


if __name__ == '__main__':
    work_bot = MainBot()
    work_bot.main()
