import asyncio
import logging
import traceback

from flask import Flask
from threading import Thread

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import (
    BOT_TOKEN,
    BOT_NAME,
)

from bot.start import start
from bot.buy import buy
from bot.payment import handle_payment

from bot.voice_handler import (
    handle_text_message,
    handle_voice_message,
)

from admin.admin_panel import (
    approve,
    reject,
)

# ==========================================
# LOGGING ULTRA DETAILLÉ
# ==========================================

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Réduit spam httpx
logging.getLogger("httpx").setLevel(logging.WARNING)

# ==========================================
# FLASK SERVER
# ==========================================

flask_app = Flask(__name__)


@flask_app.route("/")
def home():

    logger.info("ROOT URL VISITED")

    return f"{BOT_NAME} is running!"


# ==========================================
# ERROR HANDLER
# ==========================================

async def error_handler(update, context):

    logger.error("========== BOT ERROR ==========")

    try:

        logger.error(
            "UPDATE: %s",
            str(update)
        )

        logger.error(
            "ERROR: %s",
            str(context.error)
        )

        traceback.print_exc()

    except Exception as e:

        logger.error(
            "ERROR HANDLER FAILED: %s",
            str(e)
        )


# ==========================================
# LOG UTILISATEUR
# ==========================================

async def log_all_messages(update, context):

    try:

        user = update.effective_user

        logger.info("========== NEW MESSAGE ==========")

        logger.info(
            "USER: %s",
            user.first_name
        )

        logger.info(
            "USER ID: %s",
            user.id
        )

        if update.message:

            if update.message.text:

                logger.info(
                    "TEXT: %s",
                    update.message.text
                )

            if update.message.voice:

                logger.info("VOICE MESSAGE RECEIVED")

            if update.message.photo:

                logger.info("PHOTO RECEIVED")

    except Exception as e:

        logger.error(
            "LOG MESSAGE ERROR: %s",
            str(e)
        )


# ==========================================
# TELEGRAM BOT
# ==========================================

def run_bot():

    # ======================================
    # EVENT LOOP FIX PYTHON 3.14
    # ======================================

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    print("\n===================================")
    print(f"{BOT_NAME} STARTING")
    print("===================================")

    print(
        "BOT TOKEN FOUND:",
        bool(BOT_TOKEN)
    )

    logger.info("BOT INITIALIZATION STARTED")

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    logger.info("APPLICATION CREATED")

    # =====================================
    # LOG TOUS LES MESSAGES
    # =====================================

    app.add_handler(
        MessageHandler(
            filters.ALL,
            log_all_messages
        ),
        group=-1
    )

    logger.info("GLOBAL LOGGER ADDED")

    # =====================================
    # ERROR HANDLER
    # =====================================

    app.add_error_handler(
        error_handler
    )

    logger.info("ERROR HANDLER ADDED")

    # =====================================
    # COMMANDES
    # =====================================

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    logger.info("/start COMMAND ADDED")

    app.add_handler(
        CommandHandler(
            "buy",
            buy
        )
    )

    logger.info("/buy COMMAND ADDED")

    app.add_handler(
        CommandHandler(
            "approve",
            approve
        )
    )

    logger.info("/approve COMMAND ADDED")

    app.add_handler(
        CommandHandler(
            "reject",
            reject
        )
    )

    logger.info("/reject COMMAND ADDED")

    # =====================================
    # BOUTONS MENU
    # =====================================

    app.add_handler(
        MessageHandler(
            filters.Regex("^🛒 Acheter$"),
            buy
        )
    )

    logger.info("BUY BUTTON ADDED")

    app.add_handler(
        MessageHandler(
            filters.Regex("^💳 Paiement$"),
            buy
        )
    )

    logger.info("PAYMENT BUTTON ADDED")

    app.add_handler(
        MessageHandler(
            filters.Regex("^📦 Commandes$"),
            handle_text_message
        )
    )

    logger.info("ORDERS BUTTON ADDED")

    app.add_handler(
        MessageHandler(
            filters.Regex("^📞 Support$"),
            handle_text_message
        )
    )

    logger.info("SUPPORT BUTTON ADDED")

    # =====================================
    # MESSAGE VOCAL
    # =====================================

    app.add_handler(
        MessageHandler(
            filters.VOICE,
            handle_voice_message
        )
    )

    logger.info("VOICE HANDLER ADDED")

    # =====================================
    # CAPTURE DE PAIEMENT
    # =====================================

    app.add_handler(
        MessageHandler(
            filters.PHOTO,
            handle_payment
        )
    )

    logger.info("PHOTO PAYMENT HANDLER ADDED")

    # =====================================
    # MESSAGE TEXTE
    # =====================================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_text_message
        )
    )

    logger.info("TEXT MESSAGE HANDLER ADDED")

    print("\n===================================")
    print(f"{BOT_NAME} RUNNING")
    print("===================================")

    logger.info("BOT IS NOW RUNNING")

    # =====================================
    # RUN BOT
    # =====================================

    app.run_polling(
        drop_pending_updates=True,
        stop_signals=None,
        close_loop=False
    )


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    try:

        logger.info("STARTING BOT THREAD")

        bot_thread = Thread(
            target=run_bot,
            daemon=True
        )

        bot_thread.start()

        logger.info("STARTING FLASK SERVER")

        flask_app.run(
            host="0.0.0.0",
            port=10000,
            debug=False,
            use_reloader=False
        )

    except Exception as e:

        print("\n========== CRASH ==========")
        print(str(e))

        traceback.print_exc()
