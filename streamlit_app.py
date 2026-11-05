"""
=============================================================================
SmartChef – Streamlit Cloud Deployment Runner
This file deploys the exact SmartChef website in Streamlit with zero changes.
=============================================================================
"""

import os
import streamlit as st
import streamlit.components.v1 as components
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
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stToolbar"] {display: none;}
    [data-testid="stHeader"] {display: none;}
    [data-testid="stDecoration"] {display: none;}
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
        width: 100% !important;
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

