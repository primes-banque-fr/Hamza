from telegram import Update
from telegram.ext import ContextTypes

from ai.hmb_support_ai import ask_ai
from utils.tts import text_to_voice
from utils.speech_to_text import voice_to_text


# ==========================================
# TEXT MESSAGE HANDLER
# ==========================================

async def handle_text_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.message.from_user
    user_text = update.message.text

    print("\n========== TEXT MESSAGE ==========")
    print("USER:", user.username)
    print("TEXT:", user_text)

    try:

        # IA RESPONSE
        response = ask_ai(user_text)

        print("AI RESPONSE:", response)

        # VOICE GENERATION
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
            "Je suis HMB Support AI. "
            "Erreur temporaire."
        )


# ==========================================
# VOICE MESSAGE HANDLER
# ==========================================

async def handle_voice_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    user = update.message.from_user

    print("\n========== VOICE MESSAGE ==========")
    print("USER:", user.username)

    try:

        file = await context.bot.get_file(
            update.message.voice.file_id
        )

        path = "voice.ogg"

        await file.download_to_drive(path)

        # VOICE → TEXT
        text = voice_to_text(path)

        print("VOICE TO TEXT:", text)

        if not text:

            await update.message.reply_text(
                "Je n'ai pas compris votre message vocal."
            )
            return

        # IA RESPONSE
        response = ask_ai(text)

        print("AI RESPONSE:", response)

        # TEXT → VOICE
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
            "Erreur vocale temporaire. "
            "Veuillez réessayer."
    )
