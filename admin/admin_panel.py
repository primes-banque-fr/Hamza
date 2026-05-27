from telegram import Update
from telegram.ext import ContextTypes

from config import ADMIN_ID


# ==========================================
# APPROVE PAYMENT
# ==========================================

async def approve(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.message.from_user

    print("\n========== ADMIN APPROVE ==========")
    print("USER:", user.username)

    # sécurité admin
    if user.id != ADMIN_ID:

        print("UNAUTHORIZED APPROVE ATTEMPT")

        return

    try:

        await update.message.reply_text(
            "✅ Paiement approuvé avec succès.\n"
            "📦 Livraison en cours..."
        )

        print("PAYMENT APPROVED")

        # FUTUR : ici livraison fichier automatique
        # ex: send_file_to_user()

    except Exception as e:

        print("APPROVE ERROR:", str(e))


# ==========================================
# REJECT PAYMENT
# ==========================================

async def reject(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.message.from_user

    print("\n========== ADMIN REJECT ==========")
    print("USER:", user.username)

    # sécurité admin
    if user.id != ADMIN_ID:

        print("UNAUTHORIZED REJECT ATTEMPT")

        return

    try:

        await update.message.reply_text(
            "❌ Paiement rejeté.\n"
            "📞 Contactez le support."
        )

        print("PAYMENT REJECTED")

    except Exception as e:

        print("REJECT ERROR:", str(e))
