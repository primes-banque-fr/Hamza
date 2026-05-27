from gtts import gTTS
import uuid
import os


# ==========================================
# CLEAN TEXT FOR VOICE
# ==========================================

def clean_text(text: str) -> str:

    if not text:
        return " "

    # Nettoyage basique pour gTTS
    text = text.replace("*", "")
    text = text.replace("#", "")
    text = text.replace("`", "")
    text = text.replace("\n", " ")

    return text


# ==========================================
# TEXT → VOICE (HMB SUPPORT AI)
# ==========================================

def text_to_voice(text: str) -> str:

    try:

        text = clean_text(text)

        filename = f"voice_{uuid.uuid4().hex}.mp3"

        tts = gTTS(
            text=text,
            lang="fr",
            slow=False
        )

        tts.save(filename)

        print("\n========== TTS GENERATED ==========")
        print("FILE:", filename)
        print("TEXT:", text[:120])

        return filename

    except Exception as e:

        print("TTS ERROR:", str(e))

        # fallback audio minimal
        fallback_file = f"voice_fallback_{uuid.uuid4().hex}.mp3"

        try:

            tts = gTTS(
                text="Service vocal indisponible",
                lang="fr"
            )

            tts.save(fallback_file)

            return fallback_file

        except:

            return ""
