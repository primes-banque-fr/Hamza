from telegram import Update
from telegram.ext import ContextTypes

from utils.tts import text_to_voice

TEXT = """
📦 FORFAITS

CAMTEL:
500 - 1 semaine
750 - 2 semaines
1500 - 1 mois

MTN:
1000 - 5GO
1600 - 10GO
3600 - 30GO

PAYMENT:
OM: 692274053
MTN: 651388771
"""

VOICE = "Voici les forfaits disponibles. Choisissez votre plan puis envoyez le paiement."

async def buy(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(TEXT)

    audio = text_to_voice(VOICE)

    await update.message.reply_voice(open(audio, "rb"))
