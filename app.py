import json
from pathlib import Path
import streamlit as st

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(page_title="Safaa Zemmar — CV Cyber", page_icon="🛡️", layout="wide")

BASE = Path(__file__).parent
ASSETS = BASE / "assets"
PDF_PATH = ASSETS / "CV_Safaa_Zemmar.pdf"        # optionnel
PHOTO_PATH = ASSETS / "profile.jpg"             # optionnel
LOTTIE_PATH = ASSETS / "lottie-cyber.json"      # optionnel

# Optional lottie
try:
    from streamlit_lottie import st_lottie
except Exception:
    st_lottie = None


def load_lottie(path: Path):
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


# ----------------------------
# DATA (modifie ici)
# ----------------------------
NAME = "SAFAA ZEMMAR"
TAGLINE = "B2 Informatique (Ynov) — Alternance B3 Cybersécurité"
EMAIL = "safaazemmar@gmail.com"
PHONE = "07 54 58 73 77"

PROFILE = (
    "Étudiante en Bachelor Informatique avec un solide background en développement et une forte appétence "
    "pour la cybersécurité. Profil technique polyvalent : systèmes Linux, réseau, virtualisation, sécurité web. "
    "Lab perso (VM Windows/Linux, Apache, Proxy, pfSense) + Cisco. Objectif : alternance B3 cybersécurité."
)

# Skills (chips)
SKILLS = {
    "Cybersécurité": [
        "SQL Injection", "XSS", "Gestion des sessions", "Validation des entrées",
        "Authentification / Autorisation (principes)", "HTTPS / TLS (principes)", "CTF"
    ],
    "Réseau": [
        "TCP/IP", "HTTP/HTTPS", "DNS", "SSH", "Scan de ports", "Wireshark",
        "Cisco (VLAN, routage, switching)"
    ],
    "Systèmes & Infra": [
        "Linux (permissions, process, services)", "Bases Windows", "Virtualisation (VM)",
        "Apache", "Proxy", "pfSense"
    ],
    "Outils": ["Nmap", "Wireshark", "Cisco Packet Tracer", "Git / GitHub"],
    "Développement": ["Python", "PHP / SQL (phpMyAdmin)", "HTML / CSS", "Java (Swing)", "JavaScript", "Go (notions)"],
}

PROJECTS = [
    {
        "title": "Lab Cybersécurité / Infrastructure virtualisée",
        "subtitle": "VM Windows + Linux • Apache • Proxy • pfSense • Cisco",
        "bullets": [
            "Mise en place d’un environnement virtualisé complet (VM Windows/Linux).",
            "Déploiement d’un serveur Apache + serveur Proxy.",
            "Configuration pfSense : règles de filtrage, segmentation, tests de connectivité.",
            "Analyse de trafic réseau et compréhension des flux."
        ],
        "tags": ["Infra", "Réseau", "Firewall", "Lab"]
    },
    {
        "title": "Application Web E-commerce",
        "subtitle": "PHP • SQL • HTML/CSS",
        "bullets": [
            "Développement complet : utilisateurs, authentification, base SQL.",
            "Gestion des sessions + validation des entrées.",
            "Réflexion sécurité : risques SQLi / XSS et bonnes pratiques."
        ],
        "tags": ["Web", "SQL", "Auth", "Sécurité applicative"]
    },
    {
        "title": "Landing Page SaaS",
        "subtitle": "HTML • CSS",
        "bullets": [
            "Intégration responsive et structuration UI.",
            "Compréhension des interactions côté client (surface d’attaque front)."
        ],
        "tags": ["Front", "UI", "Responsive"]
    },
    {
        "title": "App de réservation",
        "subtitle": "Java • Swing",
        "bullets": [
            "Application desktop avec logique métier et validation des entrées.",
            "Gestion des erreurs et robustesse."
        ],
        "tags": ["Java", "Desktop", "Validation"]
    },
    {
        "title": "Jeu Pierre-Feuille-Ciseaux",
        "subtitle": "Python • Console • Pygame • Web",
        "bullets": [
            "Implémentations console, graphique (Pygame) et web.",
            "Structuration du code + gestion des entrées utilisateur."
        ],
        "tags": ["Python", "Algo", "UI"]
    },
]

EDUCATION = [
    ("2025 – 2026", "Bachelor 2 Informatique — Ynov Campus Paris Est"),
    ("2023", "Baccalauréat Général (NSI, SES) — Mention Assez Bien"),
    ("—", "Certification Pix"),
]

EXPERIENCE = [
    ("2025 (3 mois)", "Stage — Numeryk", ["Découverte environnement pro", "Participation activités techniques", "Adaptation aux processus"]),
    ("Oct. 2023", "Stage — Girls Can Code (École 42 Paris)", ["Initiation programmation/algorithmique", "Travail en équipe"]),
    ("Sept. 2023", "Stage — Girls Can Code (ECE Paris)", ["Création de sites web", "Découverte environnement Linux"]),
    ("—", "Expériences complémentaires", ["Vendeuse au marché", "Garde d’enfants", "Aide aux devoirs"]),
]

ASSOCIATIVE = [
    "Présentation spécialité NSI",
    "Service National Universel (SNU)",
    "Engagement actions citoyennes",
    "Déléguée de classe",
    "Projet Erasmus / échange linguistique",
]

LANGUAGES = ["Français : C2", "Anglais : B2", "Arabe : C1", "Espagnol : C1"]
INTERESTS = ["Cybersécurité", "Technologies", "Jeux vidéo", "Séries / Cinéma", "Voyage"]


# ----------------------------
# STYLES (animations + glass)
# ----------------------------
st.markdown(
    """
<style>
/* Layout */
.block-container { max-width: 1200px; padding-top: 1.2rem; padding-bottom: 3rem; }

/* Animated background glow */
.bg {
  position: fixed; inset: 0; z-index: -1;
  background: radial-gradient(800px 500px at 20% 10%, rgba(99,102,241,.22), transparent 60%),
              radial-gradient(700px 500px at 80% 20%, rgba(16,185,129,.18), transparent 60%),
              radial-gradient(900px 600px at 55% 85%, rgba(236,72,153,.16), transparent 55%),
              linear-gradient(180deg, #070a12 0%, #070a12 100%);
  animation: floatbg 10s ease-in-out infinite alternate;
}
@keyframes floatbg { from { filter: hue-rotate(0deg); } to { filter: hue-rotate(18deg); } }

/* Typography */
h1,h2,h3,h4 { letter-spacing: -0.02em; }
.smallmuted { color: rgba(255,255,255,.70); font-size: .95rem; }
.muted { color: rgba(255,255,255,.72); }

/* Hero card */
.hero {
  border: 1px solid rgba(255,255,255,.10);
  background: rgba(255,255,255,.06);
  backdrop-filter: blur(10px);
  border-radius: 18px;
  padding: 20px 18px;
  box-shadow: 0 10px 30px rgba(0,0,0,.35);
  position: relative;
  overflow: hidden;
}
.hero:before{
  content:"";
  position:absolute; inset:-2px;
  background: linear-gradient(90deg, rgba(99,102,241,.55), rgba(16,185,129,.40), rgba(236,72,153,.35));
  opacity:.35;
  filter: blur(22px);
  animation: glow 4s ease-in-out infinite alternate;
}
@keyframes glow { from { transform: translateX(-8px); } to { transform: translateX(8px); } }
.hero-inner { position: relative; }

/* Chips */
.chip {
  display:inline-block;
  padding: .32rem .62rem;
  border-radius: 999px;
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.12);
  color: rgba(255,255,255,.88);
  font-size: .88rem;
  margin: .18rem .25rem 0 0;
  transition: transform .15s ease, background .15s ease, border .15s ease;
}
.chip:hover { transform: translateY(-2px); background: rgba(255,255,255,.12); border: 1px solid rgba(255,255,255,.20); }

/* Section title */
.section-title {
  font-size: 1.05rem;
  font-weight: 800;
  margin: 1.1rem 0 .55rem 0;
  color: rgba(255,255,255,.92);
}

/* Cards */
.card {
  border: 1px solid rgba(255,255,255,.10);
  background: rgba(255,255,255,.05);
  backdrop-filter: blur(10px);
  border-radius: 16px;
  padding: 14px 14px;
  box-shadow: 0 10px 22px rgba(0,0,0,.26);
  transition: transform .18s ease, border .18s ease, background .18s ease;
}
.card:hover {
  transform: translateY(-4px);
  border: 1px solid rgba(255,255,255,.18);
  background: rgba(255,255,255,.07);
}
.card h3 { margin: 0 0 .15rem 0; font-size: 1.02rem; }
.card .sub { color: rgba(255,255,255,.70); margin: 0 0 .45rem 0; }
.card ul { margin: .35rem 0 0 1.1rem; color: rgba(255,255,255,.82); }

/* Timeline */
.timeline {
  border-left: 2px solid rgba(255,255,255,.14);
  padding-left: 14px;
}
.titem {
  position: relative;
  margin-bottom: 14px;
  padding: 10px 12px;
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,.10);
  background: rgba(255,255,255,.05);
  backdrop-filter: blur(10px);
}
.titem:before{
  content:"";
  position:absolute;
  left:-22px; top: 16px;
  width: 10px; height: 10px;
  border-radius: 999px;
  background: rgba(99,102,241,.8);
  box-shadow: 0 0 0 4px rgba(99,102,241,.12);
}
.titem .tdate { font-size: .85rem; color: rgba(255,255,255,.65); }
.titem .ttitle { font-weight: 750; color: rgba(255,255,255,.90); margin-top: 2px; }

/* Reveal on load (simple) */
.reveal { animation: reveal .7s ease both; }
@keyframes reveal { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

/* Streamlit default tweaks */
div[data-testid="stSidebarContent"] {
  background: rgba(255,255,255,.04);
  border-right: 1px solid rgba(255,255,255,.08);
}
a { color: rgba(99,102,241,.95) !important; }
</style>
<div class="bg"></div>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# SIDEBAR (Glass)
# ----------------------------
with st.sidebar:
    st.markdown(f"## 🛡️ {NAME}")
    st.markdown(f"<div class='smallmuted'>{TAGLINE}</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Contact")
    st.write(f"📧 {EMAIL}")
    st.write(f"📞 {PHONE}")

    # Download CV (PDF)
    if PDF_PATH.exists():
        st.markdown("### CV PDF")
        st.download_button(
            label="⬇️ Télécharger le CV",
            data=PDF_PATH.read_bytes(),
            file_name="CV_Safaa_Zemmar.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.caption("Astuce : mets ton PDF dans `assets/CV_Safaa_Zemmar.pdf` pour activer le bouton Download.")

    st.markdown("---")
    st.markdown("### Navigation")
    section = st.radio(
        "Aller à :",
        ["Accueil", "Compétences", "Projets", "Expériences", "Formation", "Associatif", "Langues & intérêts"],
        label_visibility="collapsed",
    )

# ----------------------------
# MAIN
# ----------------------------
# Header / Hero
colA, colB = st.columns([1.2, 1])

with colA:
    st.markdown(
        f"""
        <div class="hero reveal">
          <div class="hero-inner">
            <div class="smallmuted">CV en ligne</div>
            <h1 style="margin:.2rem 0 0 0;">{NAME}</h1>
            <div class="muted" style="font-size:1.05rem; margin-top:.35rem;">{TAGLINE}</div>
            <div style="height:.65rem;"></div>
            <div class="muted" style="line-height:1.55;">{PROFILE}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with colB:
    # Lottie (optionnel)
    lottie = load_lottie(LOTTIE_PATH)
    if st_lottie and lottie:
        st_lottie(lottie, height=260, key="cyber")
    else:
        # Photo (optionnelle)
        if PHOTO_PATH.exists():
            st.image(str(PHOTO_PATH), use_container_width=True)
        else:
            if PHOTO_PATH.exists():
                st.image(str(PHOTO_PATH), use_container_width=True)


st.markdown("")

def chips(items):
    html = "".join([f"<span class='chip'>{x}</span>" for x in items])
    st.markdown(html, unsafe_allow_html=True)

def project_card(p):
    tags_html = "".join([f"<span class='chip'>{t}</span>" for t in p["tags"]])
    bullets_html = "".join([f"<li>{b}</li>" for b in p["bullets"]])
    st.markdown(
        f"""
        <div class="card reveal">
          <h3>{p["title"]}</h3>
          <div class="sub">{p["subtitle"]}</div>
          <div>{tags_html}</div>
          <ul>{bullets_html}</ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
# Sections (navigation)
# ----------------------------
if section == "Accueil":
    st.markdown("<div class='section-title'>À retenir</div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("<div class='card reveal'><h3>🧠 Profil</h3><div class='sub'>Polyvalent & orienté cyber</div><ul><li>Dev + sécurité web</li><li>Linux + réseau</li><li>Lab infra</li></ul></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card reveal'><h3>🧪 Lab</h3><div class='sub'>VM + pfSense + proxy</div><ul><li>Architecture réseau</li><li>Filtrage & segmentation</li><li>Analyse trafic</li></ul></div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card reveal'><h3>🛠️ Outils</h3><div class='sub'>Prêt(e) pour l’alternance</div><ul><li>Nmap</li><li>Wireshark</li><li>Cisco</li></ul></div>", unsafe_allow_html=True)

elif section == "Compétences":
    st.markdown("<div class='section-title'>Compétences</div>", unsafe_allow_html=True)

    for domain, items in SKILLS.items():
        st.markdown(f"<div class='card reveal'><h3>{domain}</h3>", unsafe_allow_html=True)
        chips(items)
        st.markdown("</div>", unsafe_allow_html=True)

elif section == "Projets":
    st.markdown("<div class='section-title'>Projets</div>", unsafe_allow_html=True)
    for p in PROJECTS:
        project_card(p)

elif section == "Expériences":
    st.markdown("<div class='section-title'>Expériences</div>", unsafe_allow_html=True)
    st.markdown("<div class='timeline reveal'>", unsafe_allow_html=True)
    for date, title, bullets in EXPERIENCE:
        bullets_html = "".join([f"<li>{b}</li>" for b in bullets])
        st.markdown(
            f"""
            <div class="titem">
              <div class="tdate">{date}</div>
              <div class="ttitle">{title}</div>
              <ul>{bullets_html}</ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

elif section == "Formation":
    st.markdown("<div class='section-title'>Formation</div>", unsafe_allow_html=True)
    st.markdown("<div class='timeline reveal'>", unsafe_allow_html=True)
    for date, title in EDUCATION:
        st.markdown(
            f"""
            <div class="titem">
              <div class="tdate">{date}</div>
              <div class="ttitle">{title}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

elif section == "Associatif":
    st.markdown("<div class='section-title'>Projets personnels & associatifs</div>", unsafe_allow_html=True)
    bullets_html = "".join([f"<li>{x}</li>" for x in ASSOCIATIVE])
    st.markdown(
        f"""
        <div class="card reveal">
          <ul>{bullets_html}</ul>
        </div>
        """,
        unsafe_allow_html=True
    )

elif section == "Langues & intérêts":
    st.markdown("<div class='section-title'>Langues</div>", unsafe_allow_html=True)
    st.markdown("<div class='card reveal'>", unsafe_allow_html=True)
    chips(LANGUAGES)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Centres d’intérêt</div>", unsafe_allow_html=True)
    st.markdown("<div class='card reveal'>", unsafe_allow_html=True)
    chips(INTERESTS)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)
st.caption("© Safaa Zemmar — CV web (Streamlit)")
