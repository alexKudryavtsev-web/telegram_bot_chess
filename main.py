import os
import logging
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters
import re
# re.match(r"\w\d[-: ]\w\d", "B3 B4")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

load_dotenv()


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    load_dotenv()
    updater = Updater(os.getenv('TOKEN'))
    dp = updater.dispatcher

    test = MessageHandler(Filters.text, echo)
    dp.add_handler(test)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
