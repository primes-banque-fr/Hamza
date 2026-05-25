from telegram import Update
from telegram.ext import ContextTypes

from ai.hmb_support_ai import ask_ai
from utils.tts import text_to_voice
from utils.speech_to_text import voice_to_text


async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    response = ask_ai(update.message.text)

    audio = text_to_voice(response)

    await update.message.reply_voice(open(audio, "rb"))


async def handle_voice_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    file = await context.bot.get_file(update.message.voice.file_id)

    path = "voice.ogg"

    await file.download_to_drive(path)

    text = voice_to_text(path)

    response = ask_ai(text)

    audio = text_to_voice(response)

    await update.message.reply_voice(open(audio, "rb"))
