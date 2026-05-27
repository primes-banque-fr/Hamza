import asyncio
from flask import Flask
from threading import Thread

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from config import (
    BOT_TOKEN,
    BOT_NAME
)

from bot.start import start
from bot.buy import buy
from bot.payment import handle_payment

from bot.voice_handler import (
    handle_text_message,
    handle_voice_message
)

from admin.admin_panel import (
    approve,
    reject
)


# ==========================================
# FLASK SERVER
# ==========================================

flask_app = Flask(__name__)


@flask_app.route("/")
def home():
    return f"{BOT_NAME} is running!"


# ==========================================
# TELEGRAM BOT
# ==========================================

def run_bot():
    # Python 3.14 + thread = event loop manuel obligatoire
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    print("\n==============================")
    print(f"{BOT_NAME} STARTING")
    print("==============================")

    print(
        "BOT TOKEN FOUND:",
        bool(BOT_TOKEN)
    )

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    # =====================================
    # COMMANDES
    # =====================================

    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        CommandHandler(
            "buy",
            buy
        )
    )

    app.add_handler(
        CommandHandler(
            "approve",
            approve
        )
    )

    app.add_handler(
        CommandHandler(
            "reject",
            reject
        )
    )

    # =====================================
    # BOUTONS MENU
    # =====================================

    app.add_handler(
        MessageHandler(
            filters.Regex("^🛒 Acheter$"),
            buy
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex("^💳 Paiement$"),
            buy
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex("^📦 Commandes$"),
            handle_text_message
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Regex("^📞 Support$"),
            handle_text_message
        )
    )

    # =====================================
    # MESSAGE VOCAL
    # =====================================

    app.add_handler(
        MessageHandler(
            filters.VOICE,
            handle_voice_message
        )
    )

    # =====================================
    # CAPTURE DE PAIEMENT
    # =====================================

    app.add_handler(
        MessageHandler(
            filters.PHOTO,
            handle_payment
        )
    )

    # =====================================
    # MESSAGE TEXTE
    # =====================================

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_text_message
        )
    )

    print("\n==============================")
    print(f"{BOT_NAME} RUNNING")
    print("==============================")

    # IMPORTANT :
    # - drop_pending_updates=True nettoie les anciens updates
    # - stop_signals=None évite l'erreur "set_wakeup_fd only works in main thread"
    # - close_loop=False évite de fermer la loop manuellement dans le thread
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
        bot_thread = Thread(target=run_bot, daemon=True)
        bot_thread.start()

        flask_app.run(
            host="0.0.0.0",
            port=10000,
            debug=False,
            use_reloader=False
        )

    except Exception as e:
        print("\n========== CRASH ==========")
        print(str(e))

        import traceback
        traceback.print_exc()
