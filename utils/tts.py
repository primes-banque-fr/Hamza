import asyncio
import threading
import uuid

import edge_tts


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

    return text.strip()


# ==========================================
# EDGE TTS ASYNC
# ==========================================

async def generate_voice(text: str, filename: str):
    communicate = edge_tts.Communicate(
        text=text,
        voice="fr-FR-HenriNeural"
    )
    await communicate.save(filename)


# ==========================================
# TEXT → VOICE
# ==========================================

def text_to_voice(text: str) -> str:
    try:
        text = clean_text(text)
        filename = f"voice_{uuid.uuid4().hex}.mp3"

        error_holder = {"error": None}

        def runner():
            try:
                asyncio.run(generate_voice(text, filename))
            except Exception as e:
                error_holder["error"] = e

        thread = threading.Thread(target=runner)
        thread.start()
        thread.join()

        if error_holder["error"]:
            raise error_holder["error"]

        print("\n========== EDGE TTS GENERATED ==========")
        print("FILE:", filename)
        print("TEXT:", text[:120])

        return filename

    except Exception as e:
        print("EDGE TTS ERROR:", str(e))
        return ""
