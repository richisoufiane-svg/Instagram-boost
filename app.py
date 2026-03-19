import streamlit as st
import random
import pandas as pd
import altair as alt
import json
from datetime import datetime
from typing import List

# Configuration de la page
st.set_page_config(page_title="InstaBoost Morocco", page_icon="📈", layout="wide")

# Initialisation de l'historique
if "hooks_history" not in st.session_state:
    st.session_state["hooks_history"] = []

if "last_generated" not in st.session_state:
    st.session_state["last_generated"] = []

# Style CSS pour l'interface
st.markdown(
    """
    <style>
    .main { background-color: #fafafa; padding-top: 10px; }
    .stButton>button { width: 100%; border-radius: 12px; background-color: #E1306C; color: white; }
    .hook-box { 
        background: white;
        border-radius: 8px; padding: 12px; margin-bottom: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.1);
        border-left: 5px solid #E1306C;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("📸 InstaBoost : Objectif 10k")

# --- SECTION 1 : CHECKLIST & STATS ---
col_a, col_b = st.columns([2, 1])
with col_a:
    st.subheader("✅ Ta Checklist de Croissance")
    c1, c2 = st.columns(2)
    with c1:
        st.checkbox("Publier 1 Reel (Format 9:16)")
        st.checkbox("Répondre aux DMs")
    with c2:
        st.checkbox("15 min d'interaction (Explore)")
        st.checkbox("Partager en Story (Engagement)")

with col_b:
    st.subheader("🔎 Quick Metrics")
    followers_actuels = st.number_input("Nombre d'abonnés", min_value=0, value=0)
    if followers_actuels > 0:
        st.write(f"Prochain palier : **{int(followers_actuels * 1.2)}** (+20%)")

st.divider()

# --- SECTION 2 : GÉNÉRATEUR D'ACCROCHES ---
st.subheader("✍️ Générateur d'Accroches Virales")
subject = st.text_input("Sujet de ton Reel (ex: Montage, Sport, Cuisine)", placeholder="Tape ici...")
tone = st.selectbox("Ton de l'accroche", ["Direct / Choc", "Curiosité", "Éducatif", "Humour"])

base_templates = {
    "Direct / Choc": ["L'erreur que 90% des gens font en {sujet}...", "Arrête tout : tu fais mal {sujet} !"],
    "Curiosité": ["Voici le secret pour {sujet} que personne ne dit.", "Ce petit détail en {sujet} change tout..."],
    "Éducatif": ["3 étapes pour progresser en {sujet}.", "Comment j'ai maîtrisé {sujet} en 7 jours."],
    "Humour": ["Moi essayant de faire {sujet} sans café...", "Pourquoi {sujet} est ma thérapie."]
}

if st.button("Générer des accroches"):
    if not subject:
        st.warning("Entre un sujet !")
    else:
        templates = base_templates.get(tone, ["{sujet} : Le guide complet."])
        new_hooks = [random.choice(templates).format(sujet=subject) for _ in range(3)]
        st.session_state["last_generated"] = new_hooks
        st.success("Accroches générées !")

if st.session_state["last_generated"]:
    for h in st.session_state["last_generated"]:
        st.markdown(f"<div class='hook-box'><strong>{h}</strong></div>", unsafe_allow_html=True)

st.divider()

# --- SECTION 3 : CONSEILS TECHNIQUES ---
st.subheader("⚙")

