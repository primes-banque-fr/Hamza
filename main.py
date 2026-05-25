import asyncio
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN

from bot.start import start
from bot.buy import buy
from admin.admin_panel import approve, reject
from bot.voice_handler import handle_text_message, handle_voice_message
from bot.payment import handle_payment


async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("buy", buy))
    app.add_handler(CommandHandler("approve", approve))
    app.add_handler(CommandHandler("reject", reject))

    app.add_handler(MessageHandler(filters.PHOTO, handle_payment))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    app.add_handler(MessageHandler(filters.VOICE, handle_voice_message))

    print("HMB Support AI running...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()
    await app.idle()


if __name__ == "__main__":
    asyncio.run(main())
