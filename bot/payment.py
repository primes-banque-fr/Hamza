from telegram import Update
from telegram.ext import ContextTypes

from config import (
    ADMIN_ID,
    PAYMENT_WAIT_TEXT,
    ADMIN_PAYMENT_ALERT
)


# ==========================================
# HANDLE PAYMENT (PHOTO)
# ==========================================

async def handle_payment(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.message.from_user

    print("\n========== PAYMENT RECEIVED ==========")
    print("USER:", user.username)
    print("ID:", user.id)

    try:

        # =====================================
        # SEND TO ADMIN
        # =====================================

        caption = ADMIN_PAYMENT_ALERT.format(
            username=user.username,
            user_id=user.id,
            full_name=user.full_name
        )

        # récupère la photo la plus grande
        photo = update.message.photo[-1]

        file_id = photo.file_id

        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=file_id,
            caption=caption
        )

        print("PAYMENT SENT TO ADMIN")

        # =====================================
        # USER RESPONSE
        # =====================================

        await update.message.reply_text(
            PAYMENT_WAIT_TEXT
        )

        print("USER NOTIFIED: WAITING VERIFICATION")

    except Exception as e:

        print("PAYMENT ERROR:", str(e))

        await update.message.reply_text(
            "❌ Erreur lors du traitement du paiement. "
            "Veuillez contacter le support."
        )
