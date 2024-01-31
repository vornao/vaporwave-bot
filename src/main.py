#                       ⋆ ˚｡⋆୨୧˚  v a p o r w a v e  b o t  ˚୨୧⋆｡˚ ⋆


# Simple Telegram bot that converts standard unicode chars to  full-width ones
# Unicode full width characters, means that all characters has the size of a chinese character.
# Full width characters goes from 0xFF1 to 0xFFE5
# Japanese hirigana characters go from 0x3040 to 0x309f

# ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚ ⋆ ˚｡⋆୨୧˚
import os
import logging
import random
import utils
import config

from uuid import uuid4

from telegram import (
    Update,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext, InlineQueryHandler



async def start(update: Update, context: CallbackContext):
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

    update.message.reply_text(utils.start_msg)


async def help(update, context):
    update.message.reply_text(utils.help_msg)


async def privacy_message(update, context):
    await update.message.reply_text(utils.privacy_msg)


async def inline_vaporize_query(update: Update, context: CallbackContext):
    query = update.inline_query.query

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
    await update.inline_query.answer(results, cache_time=utils.inline_cache_time)


if __name__ == "__main__":
    try:
        os.mkdir(config.FILES_PATH)
    except:
        print("logging directory already exists")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename=config.FILES_PATH + "vaporwave-bot.log",
        filemode="a+",
    )

    logging.info("Vaporwave Bot Started")

    
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help))
    app.add_handler(CommandHandler("privacy", privacy_message))
    app.add_handler(InlineQueryHandler(inline_vaporize_query))
    app.run_polling()

