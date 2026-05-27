import os
from dotenv import load_dotenv

# ==========================================
# LOAD ENV
# ==========================================

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

ADMIN_ID = int(
    os.getenv(
        "ADMIN_ID",
        "0"
    )
)

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY",
    ""
)

# ==========================================
# IDENTITÉ BOT
# ==========================================

BOT_NAME = "HMB Support AI"

BOT_USERNAME = "@Hmb_paiement_freesurf_bot"

CREATOR_NAME = "Le Roy HMB"

CREATOR_USERNAME = "@LeRoy_HMB"

# ==========================================
# STYLE IA
# ==========================================

VOICE_DEFAULT = "garcon"

VOICE_RATIO = 0.85
TEXT_RATIO = 0.15

AI_PERSONALITY = """
Tu es HMB Support AI.

Tu es un assistant vocal et commercial
professionnel créé uniquement
pour les ventes Free Surf HMB.

Ton créateur est Le Roy HMB.

Tu réponds seulement aux sujets suivants :

- achat
- paiement
- dépôt Orange Money
- dépôt MTN Mobile Money
- forfaits CAMTEL
- forfaits MTN Premium ultra rapide
- livraison des fichiers
- support client
- fichiers .hat
- fichiers .hc
- fichiers .ehi
- VPN Http Injector
- ZIV VPN
- HTTP Custom
- état de commande
- validation paiement
- assistance client

Tu ne réponds JAMAIS
aux sujets hors service.

Si quelqu'un demande autre chose,
tu réponds poliment :

"Je suis HMB Support AI,
développé par Le Roy HMB
uniquement pour la vente
des fichiers Free Surf
et l'assistance liée
à ce service."

Ton style :

- chaleureux
- humain
- réaliste
- professionnel
- commercial
- rassurant

Tu dois éviter les réponses
de boutique e-commerce classique :

INTERDIT :
- panier
- site web
- Gmail
- checkout
- catalogue e-commerce
- livraison Amazon
- création de compte client
- boutique en ligne générique

Tu expliques uniquement
comment fonctionne
le service HMB Free Surf.
"""

# ==========================================
# NUMÉROS PAIEMENT
# ==========================================

ORANGE_MONEY_NUMBER = "692274053"
ORANGE_MONEY_NAME = "IKATIRMEY"

MTN_MOMO_NUMBER = "651388771"
MTN_MOMO_NAME = "N A MALLAMA SPAWA"

# ==========================================
# FORFAITS CAMTEL
# ==========================================

CAMTEL_PLANS = {
    "500": {
        "price": "500F",
        "duration": "1 semaine"
    },
    "750": {
        "price": "750F",
        "duration": "2 semaines"
    },
    "1500": {
        "price": "1500F",
        "duration": "1 mois"
    }
}

# ==========================================
# FORFAITS MTN PREMIUM
# ==========================================

MTN_PLANS = {
    "1000": {
        "price": "1000F",
        "data": "5GO",
        "duration": "1 mois"
    },
    "1600": {
        "price": "1600F",
        "data": "10GO",
        "duration": "1 mois"
    },
    "3600": {
        "price": "3600F",
        "data": "30GO",
        "duration": "1 mois"
    }
}

# ==========================================
# TEXTES
# ==========================================

WELCOME_TEXT = """
🔥 Bienvenue sur HMB Support AI

Je suis votre assistant spécialisé
dans la vente des fichiers Free Surf.

Je peux vous aider pour :

🛒 Achat des forfaits
💳 Paiement
📦 Commandes
📞 Support

Choisissez une option ci-dessous.
"""

WELCOME_VOICE = """
Bonjour cher client.
Bienvenue sur HMB Support AI.

Nous sommes spécialisés
dans la vente des fichiers Free Surf.

Je peux vous assister
concernant les achats,
paiements, forfaits,
livraison et support client.
"""

PAYMENT_WAIT_TEXT = """
📥 Paiement reçu.

Votre capture est actuellement
en cours d'analyse.

Veuillez patienter pendant
la vérification du dépôt.
"""

ADMIN_PAYMENT_ALERT = """
📢 Nouveau paiement reçu

Utilisateur : @{username}

ID : {user_id}

Nom : {full_name}

Le client a envoyé
une capture de paiement.

Veuillez confirmer
la réception du dépôt.
"""
