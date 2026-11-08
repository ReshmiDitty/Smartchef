"""
=============================================================================
SmartChef: Recipe Suggestion System Using List Processing
Course: Fundamentals of Artificial Intelligence (FAI)
Entry Point: main.py (Interactive Terminal Assistant)
=============================================================================
Run this script in VS Code (click the Play button or run `python main.py`).
It interactively asks you for your pantry ingredients, dietary preference,
and available cooking time, and uses list processing to suggest the best
matching recipes with step-by-step instructions.
=============================================================================
"""

import os
import sys

# Ensure clean UTF-8 printing on Windows cmd / PowerShell without charmap errors
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

import engine_fallback
from app import call_groq_chef

BANNER_WIDTH = 74

def print_header():
    print("\n" + "=" * BANNER_WIDTH)
    print("  SMARTCHEF : RECIPE SUGGESTION SYSTEM (LIST PROCESSING AI)")
    print("  Course : Fundamentals of Artificial Intelligence (FAI)")
    print("=" * BANNER_WIDTH)
    print("  This system uses Symbolic AI & Pure List Processing (CAR / CDR / CONS)")
    print(f"  to match your pantry ingredients against {len(engine_fallback.RECIPES)} curated and community recipes.")
    print("=" * BANNER_WIDTH + "\n")

def ask_ingredients():
    print("[Question 1/3] What ingredients do you have in your kitchen?")
    print("  Tip: Enter items separated by commas.")
    print("  Examples: 'tomato, onion, rice' | 'pasta, garlic, olive-oil' | 'noodles, broccoli, bell pepper'")
    print("  Quick Presets: type 'dal', 'pasta', 'paneer', 'chicken', or 'salad'")
    
    presets = {
        "dal": ["lentils", "rice", "onion", "tomato", "garlic", "cumin"],
        "pasta": ["pasta", "olive-oil", "garlic", "chili", "parmesan"],
        "paneer": ["paneer", "butter", "tomato", "onion", "cream", "garam-masala"],
        "chicken": ["chicken", "butter", "tomato", "onion", "cream", "garam-masala"],
        "salad": ["cucumber", "tomato", "olive-oil", "feta-cheese", "oregano"]
    }

    while True:
        raw = input("\n  Enter your ingredients: ").strip()
        if not raw:
            print("  (!) Please enter at least one ingredient.")
            continue
        
        # Check if user selected a preset
        lower_raw = raw.lower()
        if lower_raw in presets:
            selected = presets[lower_raw]
            print(f"  -> Loaded '{lower_raw.capitalize()}' Preset: {', '.join(selected)}")
            return selected
        
        # Parse comma or space separated
        if "," in raw:
            items = [item.strip().lower().replace(" ", "-") for item in raw.split(",") if item.strip()]
        else:
            items = [item.strip().lower().replace(" ", "-") for item in raw.split() if item.strip()]
        
        if items:
            return items
        print("  (!) Please enter valid ingredients.")

def ask_diet():
    print("\n[Question 2/3] What is your dietary preference?")
    print("  [1] All Recipes (Vegetarian & Non-Vegetarian)")
    print("  [2] Vegetarian only [Veg]")
    print("  [3] Non-Vegetarian only [Non-Veg]")
    
    while True:
        choice = input("\n  Enter choice (1, 2, or 3) [Default: 1]: ").strip()
        if not choice or choice == "1":
            return "all"
        elif choice == "2":
            return "veg"
        elif choice == "3":
            return "non-veg"
        else:
            print("  (!) Invalid choice. Please enter 1, 2, or 3.")

def ask_max_time():
    print("\n[Question 3/3] How many minutes do you want to spend cooking?")
    print("  Examples: 15 (quick snacks), 30 (regular meal), 60 (elaborate dish)")
    
    while True:
        raw = input("\n  Enter maximum cooking time in minutes [Default: 60]: ").strip()
        if not raw:
            return 60
        try:
            val = int(raw)
            if val <= 0:
                print("  (!) Time must be greater than 0.")
                continue
            return val
        except ValueError:
            print("  (!) Please enter a valid number (e.g. 15, 30, 45, 60).")

def render_score_bar(score, width=15):
    filled = int((score / 100.0) * width)
    bar = "=" * filled + " " * (width - filled)
    return f"[{bar}] {score}% Match"

def display_results(results, user_ingredients, diet, max_time):
    print("\n" + "=" * BANNER_WIDTH)
    print(f"  RECIPE MATCH RESULTS : Found {len(results)} matching recipe(s)")
    print(f"  Filters Applied : Diet = {diet.upper()} | Max Time = {max_time} mins")
    print(f"  Your Pantry     : {', '.join(user_ingredients)}")
    print("=" * BANNER_WIDTH)

    if not results:
        print("\n  [!] No matching recipes found for your ingredients and time limit.")
        print("  Suggestions:")
        print("    * Try increasing your maximum cooking time.")
        print("    * Add common kitchen staples like onion, garlic, tomato, or oil.")
        print("    * Change dietary preference to 'All'.")
        print("=" * BANNER_WIDTH)
        return

    for idx, r in enumerate(results, 1):
        diet_tag = "[VEG]" if r["diet"] == "veg" else "[NON-VEG]"
        print(f"\n  #{idx}. {r['name'].upper()} {diet_tag}")
        print(f"      Cuisine     : {r['cuisine']} | Cooking Time: {r['time']} mins")
        print(f"      Match Score : {render_score_bar(r['score'])} ({r['matched_count']} of {r['total_count']} ingredients)")
        
        # Matched ingredients
        have_str = ", ".join(r["matched_ingredients"]) if r["matched_ingredients"] else "None"
        print(f"      [+] You Have in Pantry : {have_str}")
        
        # Missing ingredients
        missing_str = ", ".join(r["missing_ingredients"]) if r["missing_ingredients"] else "None (You have everything!)"
        print(f"      [-] To Buy / Missing   : {missing_str}")

        # Smart Substitutions
        if r["substitutions_applied"]:
            subs = [f"used {s['user_has']} for {s['replaces']}" for s in r["substitutions_applied"]]
            print(f"      [*] Smart Substitutions: {'; '.join(subs)}")

        # Description
        print(f"\n      Description : {r['description']}")

        # Instructions
        print("      Step-by-Step Cooking Instructions:")
        instructions = r.get("instructions") or []
        for s_idx, step in enumerate(instructions, 1):
            print(f"        {s_idx}. {step}")
        
        print("  " + "-" * (BANNER_WIDTH - 2))

def ask_ai_chef_interactive(top_recipe, user_ingredients):
    """Allows user to ask AI Chef Smart questions about the recipe."""
    recipe_name = top_recipe.get("name", "this dish") if top_recipe else "cooking"
    print("\n" + "=" * BANNER_WIDTH)
    print("  [AI CHEF CONSULTANT] Chef Smart (Powered by Groq Cloud AI)")
    print("=" * BANNER_WIDTH)
    print(f"  Ask Chef Smart anything about {recipe_name}!")
    print("  Example questions:")
    print("    - How can I make this dish spicier and richer?")
    print("    - What are the best side dishes or breads to serve with this?")
    print("    - What is a good substitute if I don't have heavy cream?")
    print("    - (Or press Enter to skip)")
    
    q = input("\n  Your culinary question : ").strip()
    if not q:
        return
    
    print("\n  [Chef Smart is thinking...]")
    try:
        system_prompt = (
            "You are Chef Smart, an encouraging, Michelin-caliber expert chef "
            "inside the SmartChef application. Provide practical, appetizing, concise culinary advice "
            "(2 to 3 paragraphs or bullet points). Help the home cook with cooking techniques, flavor "
            "enhancements, spice balance, or ingredient substitutions."
        )
        user_context = [
            f"Recipe Context: {recipe_name}",
            f"User Available Ingredients: {', '.join(user_ingredients)}",
            f"User Question: {q}"
        ]
        reply = call_groq_chef([
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "\n".join(user_context)}
        ])
        print("\n  " + "-" * (BANNER_WIDTH - 2))
        print("  CHEF SMART SAYS:")
        print("  " + "-" * (BANNER_WIDTH - 2))
        for line in reply.split("\n"):
            print(f"  {line}")
        print("  " + "-" * (BANNER_WIDTH - 2))
    except Exception as e:
        print(f"\n  Chef Smart advice: Season in layers, saut aromatics until fragrant, and finish with fresh herbs or lemon juice!")

def main():
    print_header()
    
    while True:
        # Step 1: Ask ingredients
        ingredients = ask_ingredients()
        
        # Step 2: Ask dietary preference
        diet = ask_diet()
        
        # Step 3: Ask cooking time
        max_time = ask_max_time()
        
        # Run list-processing AI matching engine
        print("\n  [Running List-Processing Matching Engine...]")
        res = engine_fallback.suggest_recipes(
            user_ingredients=ingredients,
            diet=diet,
            max_time=max_time,
            min_score=1.0,
            sort_by="score"
        )
        
        results = res.get("results", [])
        display_results(results, ingredients, diet, max_time)
        
        # Ask AI Chef advice on the top recipe if results exist
        if results:
            ask_ai_chef_interactive(results[0], ingredients)
        
        # Search again?
        print("\n" + "=" * BANNER_WIDTH)
        again = input("  Would you like to search with different ingredients? (y/n) [Default: n]: ").strip().lower()
        if again not in ["y", "yes"]:
            print("\n  Thank you for using SmartChef! Happy cooking!\n" + "=" * BANNER_WIDTH + "\n")
            break

if __name__ == "__main__":
    main()
