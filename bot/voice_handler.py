from telegram import Update
from telegram.ext import ContextTypes

from ai.hmb_support_ai import ask_ai
from utils.tts import text_to_voice
from utils.speech_to_text import voice_to_text


# ==========================================
# TEXT MESSAGE HANDLER
# ==========================================

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user
    user_text = update.message.text

    print("\n========== TEXT MESSAGE ==========")
    print("USER:", user.username)
    print("TEXT:", user_text)

    try:

        response = ask_ai(user_text)

        print("AI RESPONSE:", response)

        audio = text_to_voice(response)

        print("VOICE FILE:", audio)

        if audio:

            await update.message.reply_voice(
                voice=open(audio, "rb")
            )

        else:

            await update.message.reply_text(response)

    except Exception as e:

        print("TEXT HANDLER ERROR:", str(e))

        await update.message.reply_text(
            "Je suis HMB Support AI. Erreur temporaire."
        )


# ==========================================
# VOICE MESSAGE HANDLER (VOSK DISABLED)
# ==========================================

async def handle_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    print("\n========== VOICE MESSAGE ==========")
    print("USER:", user.username)

    try:

        file = await context.bot.get_file(
            update.message.voice.file_id
        )

        path = "voice.ogg"

        await file.download_to_drive(path)

        # VOSK SUPPRIMÉ → fallback direct
        text = voice_to_text(path)

        print("VOICE CONVERTED TEXT:", text)

        response = ask_ai(text)

        print("AI RESPONSE:", response)

        audio = text_to_voice(response)

        print("VOICE FILE:", audio)

        if audio:

            await update.message.reply_voice(
                voice=open(audio, "rb")
            )

        else:

            await update.message.reply_text(response)

    except Exception as e:

        print("VOICE HANDLER ERROR:", str(e))

        await update.message.reply_text(
            "Erreur vocale temporaire. Réessayez."
        )
