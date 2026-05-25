import wave
import json
import os
from vosk import Model, KaldiRecognizer

MODEL_PATH = "models/vosk"

model = None

if os.path.exists(MODEL_PATH):
    try:
        model = Model(MODEL_PATH)
        print("Vosk model loaded")
    except Exception as e:
        print("Vosk error:", e)
        model = None
else:
    print("Vosk model not found, voice disabled")


def voice_to_text(path):

    if model is None:
        return ""

    wf = wave.open(path, "rb")

    rec = KaldiRecognizer(model, wf.getframerate())

    text = ""

    while True:

        data = wf.readframes(4000)

        if len(data) == 0:
            break

        if rec.AcceptWaveform(data):
            text += json.loads(rec.Result()).get("text", "") + " "

    text += json.loads(rec.FinalResult()).get("text", "")

    return text
