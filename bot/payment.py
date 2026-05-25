from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID

async def handle_payment(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"""
📢 PAIEMENT REÇU

User: @{user.username}
ID: {user.id}

Status: EN ATTENTE
"""
    )

    await update.message.reply_text(
        "📥 Paiement reçu, en cours de vérification."
    )
