import asyncio

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


def main():

    print("\n==============================")
    print(f"{BOT_NAME} STARTING")
    print("==============================")

    print(
        "BOT TOKEN FOUND:",
        bool(BOT_TOKEN)
    )

    # Fix Render / Python 3.14 event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

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
            filters.TEXT
            & ~filters.COMMAND,
            handle_text_message
        )
    )

    print("\n==============================")
print(f"{BOT_NAME} RUNNING")
print("==============================")

app.bot.delete_webhook(drop_pending_updates=True)

app.run_polling(
    drop_pending_updates=True
    )


if __name__ == "__main__":

    try:
        main()

    except Exception as e:

        print("\n========== CRASH ==========")
        print(str(e))

        import traceback
        traceback.print_exc()
