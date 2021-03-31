#                       ⋆ ˚｡⋆୨୧˚  v a p o r w a v e  b o t  ˚୨୧⋆｡˚ ⋆


#Simple Telegram bot that converts standard unicode chars to  full-width ones
#Unicode full width characters, means that all characters has the size of a chinese character.
#Full width characters goes from 0xFF1 to 0xFFE5
#Japanese hirigana characters goes from 0x3040 to 0x309f

#⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ 

import logging
from telegram.inline.inlinequery import InlineQuery

from telegram.inline.inlinequeryresult import InlineQueryResult
import utils
import config

from uuid import uuid4
from telegram import Update, ParseMode, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, InlineQueryHandler

#enable logging 
logging.basicConfig(level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    filename='files/vaporwave-bot.log', 
    filemode='a')

#initialize lists with characters 

def main():
    print("Welcome to vprwv-bot")
    updater = Updater(config.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(InlineQueryHandler(inline_vaporize_query))

    updater.start_polling()
    updater.idle()

def start(update: Update, context: CallbackContext):
    try:
        log = 'User started bot. id : ' + update.message.from_user.id + ' - username: ' + update.message.from_user.username
        logging.info(log)
    except:
        logging.error(exc_info=True)

    update.message.reply_text(
        utils.start_msg,
        parse_mode=ParseMode.MARKDOWN
    )

def help(update, context):
    update.message.reply_text(
        utils.help_msg,
        parse_mode=ParseMode.MARKDOWN
    )

def inline_vaporize_query(update: Update, context: CallbackContext):
    query = update.inline_query.query
    try:
        log = 'New usage from id : ' + update.inline_query.from_user.id + ' - username: ' + update.inline_query.from_user.username
        logging.info(log)
    except:
        logging.error(exc_info=True)
    if query == '':
        return

    ans = [utils.hiramize(query), utils.emojize(query), utils.sparkleize(query) ]

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()), 
            input_message_content=InputTextMessageContent(x),
            title = x)
            for x in ans
        ]
    update.inline_query.answer(results)


if __name__ == '__main__':
    main()