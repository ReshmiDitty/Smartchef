# 🍳 SmartChef – Intelligent Recipe Suggestion System

> An intelligent recipe recommendation system that matches kitchen pantry ingredients with curated global dishes using smart pattern matching and ingredient substitutions.

---

## 🌟 Features
- **Interactive Recipe Matcher:** Pick available ingredients from categorized chips (*Vegetables, Grains, Dairy & Proteins, Spices*) or enter custom items.
- **Smart Ingredient Substitutions:** Suggests practical pantry swaps (e.g., *olive oil for butter*, *tofu for paneer*, *milk for heavy cream*).
- **Dietary & Time Filters:** Filter by `Vegetarian`, `Non-Vegetarian`, or maximum cooking time ($10\text{–}90\text{ mins}$).
- **Signature Dishes & 24 Curated Recipes:** Every recipe features high-definition photography, complete ingredient checklists, and step-by-step cooking instructions.
- **Dual Deployment Ready:** Runs seamlessly as a **Flask Web App** or directly on **Streamlit Cloud** with the exact same UI and functionality.

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/ReshmiDitty/Smartchef.git
cd Smartchef
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Web Application

#### Option A: Run via Flask
```bash
python app.py
```
Open **`http://127.0.0.1:5000/`** in your browser.

#### Option B: Run via Streamlit
```bash
streamlit run streamlit_app.py
```
Open **`http://localhost:8501/`** in your browser.

---

## ☁️ Deploy to Streamlit Community Cloud

1. Push this repository to your GitHub account (`https://github.com/ReshmiDitty/Smartchef`).
2. Log in to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **"New App"**.
4. Select repository `ReshmiDitty/Smartchef`, branch `main`, and main file path:
   ```
   streamlit_app.py
   ```
5. Click **"Deploy"**!

The exact website with full interactivity, images, modal dialogs, and matching logic will be live on Streamlit!

---

## 🧪 Run Automated Verification Tests

```bash
python test_app.py
```

---

## 📁 Project Structure

```
Smartchef/
├── app.py                # Flask server, subprocess caller, and REST API
├── streamlit_app.py      # Streamlit Cloud deployment entrypoint
├── engine_fallback.py    # List-processing matching & substitution engine
├── lisp/
│   └── recipes.lisp      # Common Lisp (SBCL) knowledge base & algorithms
├── templates/
│   ├── base.html         # Master layout with navbar, footer, and recipe modal
│   └── index.html        # Unified single-page web app
├── static/
│   ├── css/
│   │   └── style.css     # Modern responsive styling (Inter font, cards, modals)
│   └── js/
│       └── main.js       # Client-side matcher, presets, modal controller
├── requirements.txt      # Python dependencies (Flask, Streamlit, Werkzeug)
└── README.md             # Project documentation & deployment guide
```
