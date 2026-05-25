import requests
from config import OPENROUTER_API_KEY, BOT_NAME, CREATOR

SYSTEM = f"""
Tu es {BOT_NAME}, assistant HMB.

Créateur: {CREATOR}

Tu réponds uniquement sur :
- achat
- paiement
- support
- livraison
- forfaits

Refus hors sujet.
"""


def ask_ai(text):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": text}
        ]
    }

    r = requests.post(url, json=data, headers=headers)

    return r.json()["choices"][0]["message"]["content"]
