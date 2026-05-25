from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.from_user.id != ADMIN_ID:
        return

    await update.message.reply_text("✅ Paiement approuvé")


async def reject(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.from_user.id != ADMIN_ID:
        return

    await update.message.reply_text("❌ Paiement rejeté")
