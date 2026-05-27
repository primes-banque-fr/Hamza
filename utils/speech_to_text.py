import wave
import json
import os

from vosk import Model, KaldiRecognizer


# ==========================================
# VOSK MODEL PATH
# ==========================================

MODEL_PATH = "models/vosk-model-small-fr"

model = None


# ==========================================
# LOAD MODEL SAFE
# ==========================================

if os.path.exists(MODEL_PATH):

    try:

        model = Model(MODEL_PATH)

        print("\n========== VOSK LOADED ==========")
        print("MODEL:", MODEL_PATH)

    except Exception as e:

        print("VOSK ERROR:", str(e))

        model = None

else:

    print("\n========== VOSK DISABLED ==========")
    print("MODEL NOT FOUND:", MODEL_PATH)


# ==========================================
# VOICE → TEXT
# ==========================================

def voice_to_text(file_path: str) -> str:

    if model is None:

        print("VOICE RECOGNITION DISABLED")

        return ""


    try:

        wf = wave.open(file_path, "rb")

        rec = KaldiRecognizer(
            model,
            wf.getframerate()
        )

        result_text = ""

        while True:

            data = wf.readframes(4000)

            if len(data) == 0:
                break

            if rec.AcceptWaveform(data):

                part = json.loads(
                    rec.Result()
                ).get("text", "")

                result_text += part + " "

        final_part = json.loads(
            rec.FinalResult()
        ).get("text", "")

        result_text += final_part

        result_text = result_text.strip()

        print("\n========== VOICE TO TEXT ==========")
        print("RESULT:", result_text)

        return result_text

    except Exception as e:

        print("STT ERROR:", str(e))

        return ""
