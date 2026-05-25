import wave
import json

try:
    from vosk import Model, KaldiRecognizer

    MODEL_PATH = "models/vosk"

    try:
        model = Model(MODEL_PATH)
        VOSK_READY = True

    except Exception:
        model = None
        VOSK_READY = False

except Exception:
    Model = None
    KaldiRecognizer = None
    model = None
    VOSK_READY = False


def voice_to_text(path):

    if not VOSK_READY:
        return "support vocal indisponible"

    try:

        wf = wave.open(path, "rb")

        rec = KaldiRecognizer(
            model,
            wf.getframerate()
        )

        text = ""

        while True:

            data = wf.readframes(4000)

            if len(data) == 0:
                break

            if rec.AcceptWaveform(data):

                result = json.loads(
                    rec.Result()
                )

                text += (
                    result.get("text", "")
                    + " "
                )

        final = json.loads(
            rec.FinalResult()
        )

        text += final.get(
            "text",
            ""
        )

        return text.strip()

    except Exception:
        return "message vocal reçu"
