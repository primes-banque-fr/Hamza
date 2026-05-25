from gtts import gTTS
import uuid

def text_to_voice(text):

    file = f"voice_{uuid.uuid4()}.mp3"

    tts = gTTS(text=text, lang="fr")

    tts.save(file)

    return file
