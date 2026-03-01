import json
from pathlib import Path
import streamlit as st

# ========================= CONFIG =========================
st.set_page_config(
    page_title="Safaa Zemmar — CV Cybersécurité",
    page_icon="🛡️",
    layout="centered",          # IMPORTANT pour format A4
    initial_sidebar_state="collapsed"
)

# Chemins (optionnels)
BASE = Path(__file__).parent
ASSETS = BASE / "assets"
PDF_PATH = ASSETS / "CV_Safaa_Zemmar.pdf"   # Mets ton PDF ici si tu veux le bouton download

# ========================= CSS A4 + STYLE BLEU (comme Nissa) =========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    :root {
        --bg: #0a1428;
        --accent: #00b4d8;
        --card: #1e2a44;
        --text: #e0f2fe;
        --light-text: #94a3b8;
    }

    .stApp {
        background: var(--bg);
        color: var(--text);
        font-family: 'Inter', sans-serif;
        max-width: 21cm !important;     /* Largeur A4 */
        margin: 0 auto;
        padding: 0.8cm;
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
    }

    /* En-tête */
    .header {
        background: linear-gradient(90deg, #0a1428, #1e3a5f);
        padding: 1.2rem 1.5rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        border-bottom: 4px solid var(--accent);
    }
    .name {
        font-size: 2.8rem;
        font-weight: 700;
        margin: 0;
        color: white;
    }
    .title {
        font-size: 1.35rem;
        color: var(--accent);
        margin: 0.2rem 0 0 0;
    }

    /* Cartes compétences */
    .skill-card {
        background: var(--card);
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin-bottom: 1rem;
        border-left: 5px solid var(--accent);
        transition: transform 0.2s;
    }
    .skill-card:hover {
        transform: translateY(-3px);
    }
    .skill-card h3 {
        margin: 0 0 0.6rem 0;
        color: var(--accent);
        font-size: 1.1rem;
    }
    .skill-card ul {
        padding-left: 1.2rem;
        margin: 0;
    }
    .skill-card li {
        margin-bottom: 0.35rem;
        color: var(--light-text);
    }

    /* Expériences & Formation */
    .exp-card {
        background: var(--card);
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1.2rem;
    }
    .date {
        color: var(--accent);
        font-weight: 600;
        float: right;
        font-size: 0.95rem;
    }

    /* Boutons & tags */
    .tag {
        display: inline-block;
        background: rgba(0, 180, 216, 0.15);
        color: var(--accent);
        padding: 0.25rem 0.7rem;
        border-radius: 20px;
        font-size: 0.8rem;
        margin-right: 0.4rem;
        margin-bottom: 0.4rem;
    }

    @media print {
        .stApp { box-shadow: none; padding: 0; }
        .streamlit-expanderHeader { display: none; }
        .stDownloadButton, .stSidebar { display: none !important; }
        body { background: white !important; color: black !important; }
        .skill-card, .exp-card { border: 1px solid #ddd; background: white; color: black; }
    }
</style>
""", unsafe_allow_html=True)

# ========================= DONNÉES (ton CV rouge) =========================
NAME = "SAFAA ZEMMAR"
TITLE = "Virtualisation & Cybersécurité"
PROFILE = """
Étudiante en Bachelor Informatique spécialisée en cybersécurité avec une forte appétence pour la virtualisation et les environnements techniques. 
Recherche une alternance en cybersécurité orientée infrastructure, SOC, firewall et virtualisation sécurisée.
"""

CONTACT = {
    "location": "Paris, France",
    "phone": "07 54 58 73 77",
    "email": "safaazemmar@gmail.com",
    "github": "github.com/safaa60",
    "portfolio": "portfoliosafaaazemmar.streamlit.app"
}

# Compétences → cartes comme dans le CV bleu de Nissa
SKILLS_CARDS = [
    {
        "title": "Virtualisation & Infrastructure",
        "items": [
            "VirtualBox",
            "VM Linux / Windows",
            "Segmentation réseau",
            "NAT et réseaux internes",
            "Lab personnel complet"
        ]
    },
    {
        "title": "Administration Linux",
        "items": [
            "Debian / Ubuntu",
            "Apache + Proxy",
            "Gestion utilisateurs & services système",
            "Permissions & processus"
        ]
    },
    {
        "title": "Réseau & Analyse",
        "items": [
            "TCP/IP • VLAN • Routage • Switching",
            "Cisco Packet Tracer",
            "DNS • SSH",
            "Wireshark",
            "Nmap"
        ]
    },
    {
        "title": "Cybersécurité & Firewall",
        "items": [
            "pfSense",
            "Firewall (règles de filtrage)",
            "HTTPS / TLS",
            "Tests en environnement isolé",
            "Sécurisation des communications"
        ]
    }
]

# Expériences
EXPERIENCES = [
    {
        "date": "Nov. 2025 (2 mois)",
        "title": "Stage IoT & Supervision Sécurisée",
        "company": "Numeryx",
        "items": [
            "Mise en place d’une architecture IoT sécurisée",
            "Déploiement et sécurisation de brokers MQTT",
            "Simulation de capteurs connectés",
            "Analyse de flux réseau dans un environnement OT"
        ]
    },
    {
        "date": "2023",
        "title": "Stage Girls Can Code",
        "company": "École 42 & ECE Paris",
        "items": [
            "Initiation à la programmation et à l’algorithmique",
            "Création de sites web",
            "Découverte de l’environnement Linux",
            "Travail en équipe"
        ]
    }
]

# Formation
EDUCATION = [
    ("2025 – 2026", "Bachelor 2 Informatique — Ynov Campus Paris Est (Spécialisation Cybersécurité)"),
    ("2023", "Baccalauréat Général (spécialités NSI + SES) — Mention Assez Bien"),
    ("2023", "Certification Pix")
]

# Projets & Lab
PROJECTS = [
    "Lab Cybersécurité virtualisée complète (VM Windows/Linux + Apache + Proxy + pfSense + Cisco)",
    "Application web e-commerce sécurisée (PHP / SQL) avec protection SQLi / XSS",
    "Configuration avancée pfSense (règles, segmentation, NAT)",
    "Analyse réseau et cartographie avec Nmap / Wireshark"
]

# Langues
LANGUAGES = "Français (C2) • Anglais (B2) • Arabe (bilingue) • Espagnol (C1)"

# ========================= LAYOUT =========================
# HEADER (exactement comme Nissa)
st.markdown(f"""
<div class="header">
    <h1 class="name">{NAME}</h1>
    <p class="title">{TITLE}</p>
    <div style="margin-top:1rem; display:flex; gap:1.5rem; flex-wrap:wrap;">
        <span>📍 {CONTACT["location"]}</span>
        <span>📱 {CONTACT["phone"]}</span>
        <span>✉️ {CONTACT["email"]}</span>
        <span>🐙 <a href="https://{CONTACT['github']}" target="_blank" style="color:var(--accent);">{CONTACT['github']}</a></span>
    </div>
</div>
""", unsafe_allow_html=True)

# Profil
st.markdown("### 👤 Profil")
st.write(PROFILE)

st.markdown("---")

# Compétences – cartes identiques au style bleu
st.markdown("### 🛠️ Compétences")
cols = st.columns(2)
for i, card in enumerate(SKILLS_CARDS):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="skill-card">
            <h3>{card["title"]}</h3>
            <ul>
                {"".join([f"<li>{item}</li>" for item in card["items"]])}
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Expériences
st.markdown("### 💼 Expériences")
for exp in EXPERIENCES:
    st.markdown(f"""
    <div class="exp-card">
        <span class="date">{exp["date"]}</span>
        <h3>{exp["title"]}</h3>
        <p style="color:#94a3b8; margin:0 0 0.8rem 0;"><strong>{exp["company"]}</strong></p>
        <ul>
            {"".join([f"<li>{item}</li>" for item in exp["items"]])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Formation
st.markdown("### 🎓 Formation")
for date, title in EDUCATION:
    st.markdown(f"""
    <div style="display:flex; justify-content:space-between; margin-bottom:0.8rem;">
        <div><strong>{title}</strong></div>
        <div style="color:var(--accent);">{date}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Projets & Lab
st.markdown("### 🧪 Projets & Laboratoire")
for p in PROJECTS:
    st.markdown(f"• {p}")

st.markdown("---")

# Langues & Divers
col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🌍 Langues")
    st.write(LANGUAGES)
with col2:
    st.markdown("### 📌 Divers")
    st.write("• Service National Universel (SNU)\n• Engagement associatif & citoyen\n• Vendeuse, garde d’enfants, aide aux devoirs")

# Bouton PDF (si tu as le fichier)
if PDF_PATH.exists():
    with open(PDF_PATH, "rb") as f:
        st.download_button(
            label="⬇️ Télécharger le CV PDF (A4)",
            data=f,
            file_name="CV_Safaa_Zemmar.pdf",
            mime="application/pdf",
            use_container_width=True
        )
else:
    st.caption("💡 Ajoute ton PDF dans `assets/CV_Safaa_Zemmar.pdf` pour activer le téléchargement.")

st.caption("© Safaa Zemmar — Version web A4 (inspirée du CV bleu de Nissa Karadag)")