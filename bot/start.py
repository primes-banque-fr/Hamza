from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

from utils.tts import text_to_voice

menu = [
    ["🛒 Acheter", "💳 Paiement"],
    ["📦 Commandes", "📞 Support"]
]

WELCOME = (
    "Bienvenue sur HMB Support AI. "
    "Je suis votre assistant pour les fichiers Free Surf."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🔥 HMB SUPPORT AI",
        reply_markup=ReplyKeyboardMarkup(menu, resize_keyboard=True)
    )

    audio = text_to_voice(WELCOME)

    await update.message.reply_voice(open(audio, "rb"))
