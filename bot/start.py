from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from utils.tts import text_to_voice
from config import WELCOME_TEXT, WELCOME_VOICE, BOT_NAME


# ==========================================
# MENU BUTTONS
# ==========================================

MENU = [
    ["🛒 Acheter", "💳 Paiement"],
    ["📦 Commandes", "📞 Support"]
]


# ==========================================
# START COMMAND
# ==========================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    print("\n========== START COMMAND ==========")
    print("USER:", user.username)
    print("ID:", user.id)

    # Message texte UI
    await update.message.reply_text(
        f"🔥 {BOT_NAME}",
        reply_markup=ReplyKeyboardMarkup(
            MENU,
            resize_keyboard=True
        )
    )

    # Message vocal
    try:

        audio_file = text_to_voice(WELCOME_VOICE)

        if audio_file:

            await update.message.reply_voice(
                voice=open(audio_file, "rb")
            )

            print("WELCOME VOICE SENT")

    except Exception as e:

        print("START VOICE ERROR:", str(e))

        await update.message.reply_text(
            WELCOME_TEXT
    )
