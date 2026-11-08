# 🍳 SmartChef – Intelligent Recipe Suggestion System

> A modern, responsive recipe discovery platform that turns the ingredients in your kitchen into delicious meals using smart pattern matching, ingredient substitution logic, and step-by-step cooking guides.

---

## 📖 About SmartChef

**SmartChef** is an interactive web application designed to eliminate the daily question: *"What should I cook with what I have?"* Instead of requiring grocery trips for missing items, SmartChef analyzes whatever ingredients are available in your fridge or pantry, computes matching recipe percentages, suggests clever ingredient substitutions, and guides you through tested, easy-to-follow cooking methods.

The application features a single-page design, responsive across mobile, tablet, and desktop screens.

---

## 🌐 Website Features & User Experience

### 1. Hero Spotlight
* **Culinary Showcase:** An interactive spotlight card featuring popular dishes with match rates, cooking timings, and dietary badges.
* **Instant Action:** One-click navigation to the interactive recipe matching tool.

### 2. Interactive Recipe Matcher
* **Categorized Pantry Chips:** Browse and toggle ingredients across 4 organized culinary groups:
  * *Vegetables & Greens* (Tomato, onion, garlic, ginger, potato, spinach, broccoli, bell pepper, etc.)
  * *Grains & Staples* (Basmati rice, pasta, noodles, lentils, chickpeas, kidney beans, flour, etc.)
  * *Dairy & Proteins* (Paneer, butter, cream, ghee, yogurt, eggs, chicken, mutton, fish, salmon, tofu, etc.)
  * *Spices, Herbs & Oils* (Olive oil, garam masala, cumin, turmeric, coriander, curry leaves, oregano, basil, etc.)
* **Custom Ingredient Input:** Type any ingredient not in the chips to add it instantly to your pantry tray.
* **Instant Kitchen Presets:** Pre-configured baskets (*Dal & Rice, Quick Pasta, Paneer Feast, Weekend Chicken, Fresh Salad*) for instant one-click testing.
* **Dietary & Time Filters:**
  * Strict dietary separation: `All`, `🟢 Vegetarian`, or `🔴 Non-Vegetarian`.
  * Time-budget slider: Filter recipes from $10$ to $90$ minutes.
  * Sorting: Rank by Highest Match %, Fastest Cooking Time, or Fewest Missing Ingredients.

### 3. Real-Time Recipe Match Cards
* **Visual Match Score:** Dynamic color-coded progress bars (Emerald $\ge 70\%$, Indigo $40\text{–}69\%$, Amber $< 40\%$).
* **Ingredient Breakdown:** Two-column split checklist displaying:
  * **Ingredients You Have** (Green tags with $✓$).
  * **To Buy / Missing** (Red tags with $✕$).
* **Smart Substitution Alerts:** Clear notices when a recipe can be made using a pantry swap (e.g., *"Used olive oil in place of butter"*).

### 4. Signature Dishes Showcase
* Four featured culinary classics with high-resolution photography, detailed descriptions, preparation timings, and full lists of 8–12 authentic ingredients.
* Interactive cards that open full step-by-step cooking directions on click.

### 5. All 24 Curated Recipes Directory
* A comprehensive recipe catalog spanning Indian, Asian, Mediterranean, and Continental cuisines.
* Every recipe card displays cover photography, cuisine origin, dietary labels, total ingredient count, and brief recipe descriptions.

### 6. Recipe Detail Modal
* Full-bleed cover photo with high-contrast badge overlays.
* Complete ingredient checklist highlighting what you already have vs. what you need.
* Numbered, step-by-step cooking instructions with preparation timings.
* **✨ In-Modal AI Chef Advice:** Ask dish-specific questions (*"Make it spicier"*, *"Best side pairings"*, *"Texture secrets"*, *"Reheating tips"*) and receive instant culinary suggestions directly inside the modal.

### 7. ✨ Chef Smart – AI Culinary Advisor (Powered by Groq API)
* **Instant Culinary Consultation:** Click the floating "Ask AI Chef" button or header link to open Chef Smart, an on-demand AI culinary expert.
* **Pantry Inspiration:** Pick any set of ingredients in your pantry tray and click *"✨ Ask AI Chef For Ideas With These"* to receive customized meal suggestions, cooking methods, and flavor pairings.
* **Ultra-Fast AI Inference:** Powered by Groq Cloud models (`qwen/qwen3.8-27b` and `openai/gpt-oss-20b`) for lightning-fast responses.
* **Environment Configuration:** Pre-configured to run out of the box; supports custom API keys via the `GROQ_API_KEY` environment variable or Streamlit Secrets.

### 8. The 4-Step Matching Workflow
1. **Select Ingredients:** Pick what is currently in your kitchen.
2. **Pantry Matching:** Real-time evaluation against 24 curated recipe profiles.
3. **Smart Substitutions:** Automatic inference of acceptable culinary swaps.
4. **Cook & Enjoy:** Follow clear, foolproof instructions to prepare your meal.

---

## 📂 Repository & Codebase Structure

```
Smartchef/
│
├── main.py                     # Primary VS Code entry point
│                               # Prints topic overview, tests list engine, outputs live website link.
│
├── app.py                      # Flask web application & REST API microservice
│                               # Handles routing, JSON API endpoints, and template rendering.
│
├── streamlit_app.py            # Streamlit deployment entrypoint
│                               # Renders the full website seamlessly on Streamlit Cloud.
│
├── engine_fallback.py          # Core list-processing matching & substitution engine
│                               # Implements CAR, CDR, CONS, MEMBER, set difference,
│                               # and heuristic scoring for all 24 recipes.
│
├── lisp/
│   └── recipes.lisp            # Common Lisp (SBCL) knowledge base & algorithms
│                               # S-expression recipe frames, associative substitution rules,
│                               # and CLI JSON serialization.
│
├── templates/
│   ├── base.html               # Master layout containing sticky navigation,
│   │                           # recipe detail modal dialog, toast alerts, and footer.
│   │
│   └── index.html              # Unified single-page web template containing the Hero,
│                               # Recipe Finder, Signature Dishes, All 24 Recipes,
│                               # and How It Works sections.
│
├── static/
│   ├── css/
│   │   └── style.css           # Modern stylesheet (Inter typography, responsive grids,
│   │                           # dish cards, progress bars, animations, mobile drawer).
│   │
│   └── js/
│       └── main.js             # Client-side controller (chip selector, filter state,
│                               # dual-engine client-side/API matcher, modal manager).
│
├── test_app.py                 # Automated integration test suite
│                               # Verifies routes, API endpoints, and recipe matching.
│
├── requirements.txt            # Python dependencies (Flask, Streamlit, Werkzeug)
│
└── .gitignore                  # Git ignore rules for clean repository management
```

---

## 🧠 Smart Ingredient Substitution Table

The system includes an expert knowledge base of culinary substitution rules so recipes still qualify even if you lack the exact primary ingredient:

| User Has (Substitute) | Recipe Calls For (Target) | Culinary Role |
| :--- | :--- | :--- |
| **Olive Oil / Vegetable Oil** | Butter | Fat medium for cooking and sautéing |
| **Cooking Oil** | Pure Ghee | Tempering and shallow frying |
| **Tofu** | Fresh Paneer | Vegetarian protein alternative |
| **Milk / Plain Yogurt** | Heavy Cream | Gravy base & sauce enrichment |
| **Cheddar Cheese** | Parmesan / Mozzarella | Melting and savory cheese topping |
| **Mushrooms** | Chicken | Vegetarian savory umami substitute |
| **Chia Seeds (Hydrated)** | Egg | Binding agent in baking and batters |
| **Honey** | Granulated Sugar | Natural sweetener |
| **Tomato Paste** | Fresh Tomatoes | Concentrated tomato flavor base |
| **Fresh Lemon Juice** | Fresh Lime Juice | Acidic balance & citrus flavoring |

---

## 🍽️ Recipe Catalog Overview

The knowledge base contains 24 diverse recipes, each with 8 to 12 realistic culinary ingredients and tested preparation steps:

| Dish Name | Cuisine | Diet | Cooking Time | Key Ingredients |
| :--- | :--- | :--- | :--- | :--- |
| **Paneer Butter Masala** | North Indian | 🟢 Veg | 30 mins | Paneer, butter, tomato, onion, cream, cashews, kasuri methi |
| **Restaurant-Style Dal Tadka** | Indian Comfort | 🟢 Veg | 25 mins | Yellow lentils, ghee, cumin, garlic, chili, tomato, coriander |
| **Royal Hyderabadi Veg Biryani** | Hyderabadi | 🟢 Veg | 45 mins | Basmati rice, yogurt, carrots, peas, potatoes, mint, cardamom |
| **Creamy Palak Paneer** | North Indian | 🟢 Veg | 30 mins | Fresh spinach, paneer, garlic, butter, cream, cumin, ginger |
| **Amritsari Chana Masala** | Punjabi | 🟢 Veg | 35 mins | Chickpeas, onion, tomato, ginger, garlic, garam masala, cumin |
| **Homestyle Aloo Gobi** | North Indian | 🟢 Veg | 25 mins | Potatoes, cauliflower, turmeric, cumin, ginger juliennes, tomato |
| **Crispy Masala Dosa** | South Indian | 🟢 Veg | 20 mins | Fermented rice batter, spiced mashed potatoes, mustard seeds |
| **Delhi Style Rajma Masala** | North Indian | 🟢 Veg | 40 mins | Red kidney beans, basmati rice, onion, tomato, ginger, garlic |
| **Classic Butter Chicken** | Mughlai | 🔴 Non-Veg | 40 mins | Tender chicken, butter, tomato cream gravy, kasuri methi |
| **Tandoori Chicken Tikka** | Tandoori | 🔴 Non-Veg | 35 mins | Chicken cubes, Greek yogurt, lemon, Kashmiri chili, mustard oil |
| **Spiced Dhaba Egg Curry** | Indian | 🔴 Non-Veg | 25 mins | Pan-fried boiled eggs, rich onion-tomato gravy, cumin, coriander |
| **Kashmiri Mutton Rogan Josh** | Kashmiri | 🔴 Non-Veg | 60 mins | Tender mutton, mustard oil, yogurt, Kashmiri chili, fennel, cloves |
| **Goan Coconut Fish Curry** | Goan Coastal | 🔴 Non-Veg | 30 mins | Fresh fish fillets, coconut milk, curry leaves, mustard seeds |
| **Pasta Aglio e Olio** | Italian | 🟢 Veg | 15 mins | Spaghetti, extra virgin olive oil, sliced garlic, chili flakes, parsley |
| **Neapolitan Pizza Margherita** | Italian | 🟢 Veg | 25 mins | Hand-stretched dough, San Marzano tomatoes, fresh mozzarella, basil |
| **Mediterranean Greek Salad** | Mediterranean | 🟢 Veg | 10 mins | Persian cucumber, ripe tomatoes, Kalamata olives, feta, olive oil |
| **Crisp Asian Vegetable Stir-Fry** | Asian | 🟢 Veg | 20 mins | Noodles, broccoli florets, carrots, bell peppers, soy sauce, sesame oil |
| **Tuscan Vegetable Minestrone** | Italian | 🟢 Veg | 30 mins | Cannellini white beans, pasta, carrots, celery, crushed tomatoes |
| **Creamy Wild Mushroom Risotto** | Italian | 🟢 Veg | 35 mins | Arborio rice, wild mushrooms, butter, parmesan, vegetable broth |
| **Loaded Guacamole & Nachos** | Mexican | 🟢 Veg | 10 mins | Ripe Hass avocados, lime juice, jalapeño, roma tomatoes, cilantro |
| **Fettuccine Chicken Alfredo** | Italian-American | 🔴 Non-Veg | 25 mins | Fettuccine pasta, seared chicken breast, heavy cream, parmesan |
| **Gourmet Cheeseburger Deluxe** | American | 🔴 Non-Veg | 20 mins | Seasoned patty, brioche bun, aged cheddar, lettuce, tomato, pickles |
| **Pan-Seared Salmon** | Continental | 🔴 Non-Veg | 20 mins | Fresh salmon fillet, lemon herb butter, smashed garlic, rosemary |
| **Japanese Chicken Katsu Curry** | Japanese | 🔴 Non-Veg | 40 mins | Panko-crusted chicken cutlet, Japanese curry sauce, short-grain rice |

---

## 🚀 How to Run in VS Code

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run in VS Code:**
   Open `main.py` in VS Code and click the **Run / Play** button, or execute in terminal:
   ```bash
   python main.py
   ```

3. **Output in Terminal:**
   Running `main.py` will print:
   - Topic overview and list-processing reasoning architecture.
   - Quick live test result of the recipe suggestion engine.
   - Clickable website link: **`http://127.0.0.1:5000`**
   - Automatically opens the website in your default browser!
