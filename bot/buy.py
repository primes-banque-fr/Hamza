from telegram import Update
from telegram.ext import ContextTypes

from utils.tts import text_to_voice
from config import (
    CAMTEL_PLANS,
    MTN_PLANS,
    ORANGE_MONEY_NUMBER,
    MTN_MOMO_NUMBER
)


# ==========================================
# TEXT FOR BUY MENU
# ==========================================

BUY_TEXT = """
📦 FORFAITS DISPONIBLES HMB

🔵 CAMTEL PREMIUM :
- 500F → 1 semaine
- 750F → 2 semaines
- 1500F → 1 mois

🟢 MTN PREMIUM ULTRA RAPIDE :
- 1000F → 5GO / 1 mois
- 1600F → 10GO / 1 mois
- 3600F → 30GO / 1 mois

💳 PAIEMENT :
Orange Money : 692274053
MTN MoMo : 651388771

📌 Envoyez votre preuve de paiement après achat.
"""


BUY_VOICE = """
Voici les forfaits disponibles.

CAMTEL et MTN Premium.

Après votre paiement,
envoyez une capture pour validation.
"""


# ==========================================
# BUY HANDLER
# ==========================================

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    print("\n========== BUY COMMAND ==========")
    print("USER:", user.username)
    print("ID:", user.id)

    # TEXTE
    await update.message.reply_text(BUY_TEXT)

    # VOIX
    try:

        audio = text_to_voice(BUY_VOICE)

        if audio:

            await update.message.reply_voice(
                voice=open(audio, "rb")
            )

            print("BUY VOICE SENT")

    except Exception as e:

        print("BUY VOICE ERROR:", str(e))

        await update.message.reply_text(
            "Forfaits envoyés. Veuillez choisir votre plan."
    )
