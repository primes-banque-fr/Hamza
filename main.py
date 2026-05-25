from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters
)

from config import BOT_TOKEN

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

    print("=== HMB SUPPORT AI STARTING ===")
    print("BOT TOKEN FOUND:", bool(BOT_TOKEN))

    app = Application.builder().token(
        BOT_TOKEN
    ).build()

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

    app.add_handler(
        MessageHandler(
            filters.PHOTO,
            handle_payment
        )
    )

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_text_message
        )
    )

    app.add_handler(
        MessageHandler(
            filters.VOICE,
            handle_voice_message
        )
    )

    print("=== BOT RUNNING ===")

    app.run_polling()


if __name__ == "__main__":

    try:
        main()

    except Exception as e:

        print("===== CRASH =====")
        print(str(e))

        import traceback
        traceback.print_exc()
