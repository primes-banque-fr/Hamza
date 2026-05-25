import wave
import json
from vosk import Model, KaldiRecognizer

model = Model("models/vosk")

def voice_to_text(path):

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
