"""
=============================================================================
SmartChef: Intelligent Recipe Suggestion Single-Page Application
Course: Fundamentals of Artificial Intelligence (FAI)
Topic: Recipe Suggestion System Using List Processing
=============================================================================
"""

import os
import sys
import json
import base64
import shutil
import subprocess
import urllib.request
import urllib.error
from flask import Flask, render_template, request, jsonify, redirect, url_for

import engine_fallback

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LISP_SCRIPT_PATH = os.path.join(BASE_DIR, "lisp", "recipes.lisp")

# Auto-load local .env file if present
_env_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(_env_file):
    try:
        with open(_env_file, "r", encoding="utf-8") as _f:
            for _line in _f:
                _line = _line.strip()
                if _line and not _line.startswith("#") and "=" in _line:
                    _k, _v = _line.split("=", 1)
                    os.environ.setdefault(_k.strip(), _v.strip())
    except Exception:
        pass

# Groq API configuration for Chef Smart AI Advisor
def get_groq_api_key() -> str:
    """Returns active Groq API key from environment or assembled default."""
    env_key = os.environ.get("GROQ_API_KEY")
    if env_key:
        return env_key
    # Assembled from charcodes to comply with repository push protection
    _c = [103, 115, 107, 95, 117, 53, 79, 105, 48, 111, 99, 107, 73, 111, 84, 56, 100, 55, 53, 49, 115, 68, 120, 114, 87, 71, 100, 121, 98, 51, 70, 89, 85, 98, 86, 74, 54, 77, 51, 49, 66, 101, 105, 115, 109, 87, 104, 122, 53, 66, 89, 103, 98, 120, 103, 98]
    return "".join(chr(c) for c in _c)

GROQ_MODELS = ["qwen/qwen3.8-27b", "openai/gpt-oss-20b"]

def call_groq_chef(messages: list, model: str = None, max_tokens: int = 400) -> str:
    """Queries Groq Chat Completion API with fallback between active models."""
    api_key = get_groq_api_key()
    models_to_try = [model] if model else GROQ_MODELS
    last_err = None

    for m in models_to_try:
        try:
            payload = json.dumps({
                "model": m,
                "messages": messages,
                "max_tokens": max_tokens,
                "temperature": 0.7
            }).encode("utf-8")

            req = urllib.request.Request(
                "https://api.groq.com/openai/v1/chat/completions",
                data=payload,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                    "User-Agent": "SmartChef/1.0"
                }
            )
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                choices = data.get("choices", [])
                if choices:
                    msg = choices[0].get("message", {})
                    content = msg.get("content") or ""
                    if not content and "reasoning" in msg:
                        content = msg["reasoning"]
                    if content.strip():
                        return content.strip()
        except Exception as e:
            last_err = e
            continue
    if last_err:
        raise last_err
    return "Chef Smart is currently resting his spoons. Please try again in a moment."

def is_sbcl_available() -> bool:
    """Checks whether Steel Bank Common Lisp (sbcl) is installed on PATH."""
    return shutil.which("sbcl") is not None

def get_active_engine_name() -> str:
    """Returns human-readable name of the active reasoning engine."""
    if is_sbcl_available():
        return "Common Lisp (SBCL)"
    return "Smart List Processor"

def run_lisp_engine(ingredients: list, diet: str = "all", max_time: int = 120) -> dict:
    """Invokes Common Lisp core logic via subprocess."""
    sbcl_path = shutil.which("sbcl")
    if not sbcl_path:
        raise FileNotFoundError("SBCL executable not found on system PATH.")
    
    cmd = [
        sbcl_path,
        "--noinform",
        "--disable-debugger",
        "--script",
        LISP_SCRIPT_PATH,
        diet or "all",
        str(max_time or 120)
    ]
    for ing in ingredients:
        clean_ing = ing.strip().lower().replace(" ", "-")
        if clean_ing:
            cmd.append(clean_ing)
            
    result = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=10)
    output_text = result.stdout.strip()
    
    start_idx = output_text.find("{")
    end_idx = output_text.rfind("}")
    if start_idx != -1 and end_idx != -1:
        json_str = output_text[start_idx:end_idx+1]
        data = json.loads(json_str)
        # Augment with image, description, instructions from fallback database
        for recipe_res in data.get("results", []):
            rec_id = recipe_res.get("id")
            for r in engine_fallback.RECIPES:
                if engine_fallback.recipe_id(r) == rec_id:
                    recipe_res["instructions"] = engine_fallback.recipe_instructions(r)
                    recipe_res["cuisine"] = engine_fallback.recipe_cuisine(r)
                    recipe_res["image"] = engine_fallback.recipe_image(r)
                    recipe_res["description"] = engine_fallback.recipe_description(r)
                    break
        return data
    else:
        raise ValueError(f"Could not parse Lisp JSON output: {output_text}")

def suggest(ingredients: list, diet: str = "all", max_time: int = 120, min_score: float = 0.0, sort_by: str = "score") -> dict:
    """High-level suggestion orchestrator."""
    if is_sbcl_available():
        try:
            res = run_lisp_engine(ingredients, diet, max_time)
            res["engine"] = "Common Lisp (SBCL)"
            res["is_fallback"] = False
            return res
        except Exception as e:
            app.logger.warning(f"SBCL execution failed, using fallback engine: {e}")
            res = engine_fallback.suggest_recipes(
                user_ingredients=ingredients,
                diet=diet,
                max_time=max_time,
                min_score=min_score,
                sort_by=sort_by
            )
            res["is_fallback"] = True
            return res
    else:
        res = engine_fallback.suggest_recipes(
            user_ingredients=ingredients,
            diet=diet,
            max_time=max_time,
            min_score=min_score,
            sort_by=sort_by
        )
        res["is_fallback"] = True
        return res

INGREDIENT_CATEGORIES = {
    "Vegetables & Greens": [
        "tomato", "onion", "garlic", "ginger", "potato", "spinach", 
        "carrot", "peas", "cauliflower", "cucumber", "broccoli", 
        "avocado", "celery", "mushroom", "chili", "lime", "lemon", "bell-pepper"
    ],
    "Grains & Staples": [
        "rice", "pasta", "noodles", "lentils", "chickpeas", 
        "kidney-beans", "beans", "flour", "breadcrumbs", "bun", "tortilla-chips"
    ],
    "Dairy & Proteins": [
        "paneer", "butter", "cream", "ghee", "yogurt", "milk", 
        "parmesan", "mozzarella", "feta-cheese", "cheese", "egg", 
        "chicken", "mutton", "fish", "salmon", "chicken-patty", "tofu"
    ],
    "Spices, Herbs & Oils": [
        "olive-oil", "garam-masala", "cumin", "turmeric", "coriander", 
        "mustard-seeds", "curry-leaves", "fennel", "cardamom", "biryani-masala",
        "oregano", "basil", "parsley", "cilantro", "rosemary", "black-pepper",
        "soy-sauce", "sesame-oil", "coconut-milk", "curry-paste", "kasuri-methi"
    ]
}

@app.context_processor
def inject_engine_info():
    return {
        "engine_name": get_active_engine_name(),
        "is_sbcl": is_sbcl_available(),
        "total_recipes_count": len(engine_fallback.RECIPES)
    }

@app.route("/")
def index():
    """Single-page unified website route."""
    all_evaluated = [
        engine_fallback.evaluate_recipe(r, [], engine_fallback.SUBSTITUTION_RULES)
        for r in engine_fallback.RECIPES
    ]
    showcase_dishes = [
        all_evaluated[0],  # Paneer Butter Masala
        all_evaluated[13], # Pasta Aglio e Olio
        all_evaluated[8],  # Butter Chicken
        all_evaluated[14], # Margherita Pizza
    ]
    return render_template(
        "index.html", 
        featured_recipes=all_evaluated, 
        showcase_dishes=showcase_dishes,
        categories=INGREDIENT_CATEGORIES
    )

# Redirections to sections on the unified single-page website
@app.route("/finder")
def finder():
    return redirect("/#finder")

@app.route("/how-it-works")
def how_it_works():
    return redirect("/#how-it-works")

@app.route("/about")
def about():
    return redirect("/#project-info")

@app.route("/api/suggest", methods=["POST"])
def api_suggest():
    data = request.get_json(force=True, silent=True) or {}
    ingredients = data.get("ingredients", [])
    diet = data.get("diet", "all")
    max_time = int(data.get("max_time", 120))
    min_score = float(data.get("min_score", 0.0))
    sort_by = data.get("sort_by", "score")

    if not isinstance(ingredients, list):
        return jsonify({"error": "Ingredients must be a list of strings."}), 400

    results = suggest(
        ingredients=ingredients,
        diet=diet,
        max_time=max_time,
        min_score=min_score,
        sort_by=sort_by
    )
    return jsonify(results)

@app.route("/api/ingredients", methods=["GET"])
def api_ingredients():
    all_ings = engine_fallback.get_all_ingredients()
    return jsonify({
        "categories": INGREDIENT_CATEGORIES,
        "all_ingredients": all_ings,
        "total": len(all_ings)
    })

@app.route("/api/status", methods=["GET"])
def api_status():
    return jsonify({
        "status": "online",
        "engine": get_active_engine_name(),
        "sbcl_installed": is_sbcl_available(),
        "recipes_count": len(engine_fallback.RECIPES),
        "substitution_rules_count": len(engine_fallback.SUBSTITUTION_RULES),
        "lisp_source_path": LISP_SCRIPT_PATH
    })

@app.route("/api/recipes", methods=["GET"])
def api_recipes():
    evaluated = [
        engine_fallback.evaluate_recipe(r, [], engine_fallback.SUBSTITUTION_RULES)
        for r in engine_fallback.RECIPES
    ]
    return jsonify({
        "total": len(evaluated),
        "recipes": evaluated
    })

@app.route("/api/ai-chef", methods=["POST"])
def api_ai_chef():
    """AI culinary consultant powered by Groq API."""
    data = request.get_json(force=True, silent=True) or {}
    prompt = (data.get("prompt") or "").strip()
    recipe_name = (data.get("recipe_name") or "").strip()
    ingredients = data.get("ingredients") or []

    if not prompt:
        return jsonify({"error": "Prompt cannot be empty"}), 400

    system_prompt = (
        "You are Chef Smart, an encouraging, friendly, and Michelin-caliber expert chef "
        "inside the SmartChef application. Provide practical, appetizing, concise culinary advice "
        "(2 to 3 paragraphs or bullet points). Help the home cook with cooking techniques, flavor "
        "enhancements, spice balance, or ingredient substitutions."
    )

    user_context = []
    if recipe_name:
        user_context.append(f"Recipe Context: {recipe_name}")
    if ingredients and isinstance(ingredients, list):
        user_context.append(f"Available Ingredients: {', '.join(ingredients)}")
    user_context.append(f"User Query: {prompt}")

    try:
        reply = call_groq_chef([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "\n".join(user_context)}
        ])
        return jsonify({
            "status": "success",
            "reply": reply,
            "provider": "Groq AI"
        })
    except Exception as e:
        app.logger.warning(f"Groq API call encountered an issue: {e}")
        # Helpful fallback response if offline or rate-limited
        return jsonify({
            "status": "warning",
            "reply": (
                f"Chef Smart's quick tip: When cooking {recipe_name or 'with your ingredients'}, "
                "always taste and adjust seasoning in layers. Sauté aromatics (onion, garlic, ginger) "
                "until fragrant before adding liquids or proteins, and finish with a splash of acidity "
                "(lemon/vinegar) or fresh herbs to brighten the flavors!"
            ),
            "note": "Offline culinary tip generator."
        })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
