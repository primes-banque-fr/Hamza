import edge_tts
import asyncio
import uuid
import os


# ==========================================
# CLEAN TEXT FOR VOICE
# ==========================================

def clean_text(text: str) -> str:

    if not text:
        return " "

    text = text.replace("*", "")
    text = text.replace("#", "")
    text = text.replace("`", "")
    text = text.replace("\n", " ")

    return text


# ==========================================
# EDGE TTS ASYNC
# ==========================================

async def generate_voice(text: str, filename: str):

    communicate = edge_tts.Communicate(
        text=text,
        voice="fr-FR-HenriNeural"   # voix garçon français
    )

    await communicate.save(filename)


# ==========================================
# TEXT → VOICE
# ==========================================

def text_to_voice(text: str) -> str:

    try:

        text = clean_text(text)

        filename = f"voice_{uuid.uuid4().hex}.mp3"

        asyncio.run(
            generate_voice(
                text,
                filename
            )
        )

        print("\n========== EDGE TTS GENERATED ==========")
        print("FILE:", filename)
        print("TEXT:", text[:120])

        return filename

    except Exception as e:

        print("EDGE TTS ERROR:", str(e))

        return ""
