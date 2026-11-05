"""
=============================================================================
SmartChef – Streamlit Cloud Deployment Runner
This file deploys the exact SmartChef website in Streamlit with zero changes.
=============================================================================
"""

import os
import streamlit as st
import streamlit.components.v1 as components

# Configure Streamlit Cloud secrets if available
try:
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
except Exception:
    pass

from app import app

# Configure Streamlit page
st.set_page_config(
    page_title="SmartChef – Recipe Suggestion System",
    page_icon="🍳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI chrome (menus, padding, header, footer)
st.markdown("""
<style>
    /* 1. Hide all default Streamlit chrome, status, headers, and footers */
    #MainMenu, header, footer, 
    [data-testid="stToolbar"], 
    [data-testid="stHeader"], 
    [data-testid="stDecoration"], 
    [data-testid="stStatusWidget"],
    [data-testid="collapsedControl"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
    }
    
    /* 2. Remove all outer Streamlit margins, scrollbars, and padding */
    html, body, .stApp, 
    [data-testid="stAppViewContainer"], 
    [data-testid="stMain"], 
    .main, .block-container {
        padding: 0 !important;
        margin: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        max-width: 100% !important;
        overflow: hidden !important;
    }

    /* 3. Make iframe full-screen taking the entire browser window (matching localhost 1:1) */
    iframe {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        margin: 0 !important;
        padding: 0 !important;
        z-index: 999999 !important;
    }
</style>
""", unsafe_allow_html=True)

# Render the exact website HTML using Flask
with app.test_client() as client:
    response = client.get("/")
    html_content = response.data.decode("utf-8")

# Read CSS and JS assets to embed them directly for seamless Streamlit hosting
base_dir = os.path.dirname(os.path.abspath(__file__))
css_path = os.path.join(base_dir, "static", "css", "style.css")
js_path = os.path.join(base_dir, "static", "js", "main.js")

with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Inline CSS and JS into the rendered HTML
embedded_html = html_content.replace(
    '<link rel="stylesheet" href="/static/css/style.css">',
    f'<style>\n{css_content}\n</style>'
).replace(
    '<script src="/static/js/main.js"></script>',
    f'<script>\n{js_content}\n</script>'
)

# Render the exact website full-bleed in Streamlit
components.html(embedded_html, height=3800, scrolling=True)

