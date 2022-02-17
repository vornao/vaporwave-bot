#                       ⋆ ˚｡⋆୨୧˚  v a p o r w a v e  b o t  ˚୨୧⋆｡˚ ⋆


# Simple Telegram bot that converts standard unicode chars to  full-width ones
# Unicode full width characters, means that all characters has the size of a chinese character.
# Full width characters goes from 0xFF1 to 0xFFE5
# Japanese hirigana characters go from 0x3040 to 0x309f

# ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚
import os

from telegram.inline.inlinequery import InlineQuery
from telegram.inline.inlinequeryresult import InlineQueryResult
from uuid import uuid4
from telegram import (
    Update,
    ParseMode,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
    InlineQueryHandler,
)

import logging
import random
import utils
import config
import threading
import userutils


# initialize lists with characters
def main():
    # enable logging
    try:
        os.mkdir(config.FILES_PATH)
    except:
        print("directory already exists")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename=config.FILES_PATH + "vaporwave-bot.log",
        filemode="a+",
    )

    logging.info("VPRWV BOT STARTED")

    userutils.init_cache()
    ucheck = threading.Thread(target=userutils.usercheck, daemon=True)
    ucheck.start()

    updater = Updater(config.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("privacy", privacy_message))
    dispatcher.add_handler(InlineQueryHandler(inline_vaporize_query))

    updater.start_polling()
    updater.idle()


def start(update: Update, context: CallbackContext):
    try:
        log = (
            "User started bot. id : "
            + str(update.message.from_user.id)
            + " - username: "
            + update.message.from_user.username
        )
        logging.info(log)
    except:
        logging.exception("exception start method", exc_info=True)

    update.message.reply_text(utils.start_msg, parse_mode=ParseMode.MARKDOWN)


def help(update, context):
    update.message.reply_text(utils.help_msg, parse_mode=ParseMode.MARKDOWN)


def privacy_message(update, context):
    update.message.reply_text(utils.privacy_msg, parse_mode=ParseMode.MARKDOWN)


def inline_vaporize_query(update: Update, context: CallbackContext):
    query = update.inline_query.query
    try:
        userutils.queue.put(update.inline_query.from_user.username)
    except:
        logging.exception("Exception!", exc_info=True)

    if query == "":
        return

    ans = [utils.hiramize(query), utils.emojize(query), utils.sparkleize(query)]

    results = [
        InlineQueryResultArticle(
            id=str(uuid4()),
            input_message_content=InputTextMessageContent(x),
            title=x,
            description=random.choice(utils.sparkles),
        )
        for x in ans
    ]
    update.inline_query.answer(results, cache_time=utils.inline_cache_time)


if __name__ == "__main__":
    main()
