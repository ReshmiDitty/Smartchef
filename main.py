"""
=============================================================================
SmartChef: Recipe Suggestion System Using List Processing
Course: Fundamentals of Artificial Intelligence (FAI)
Entry Point: main.py
=============================================================================
Run this file directly in VS Code (click the Play button or run `python main.py`).
It displays the topic overview, tests the list-processing AI engine, and starts
the web application, printing the clickable website link to the terminal.
=============================================================================
"""

import sys
import time
import threading
import webbrowser

# Ensure clean UTF-8 printing on Windows cmd / PowerShell without charmap errors
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from app import app, suggest, get_active_engine_name, is_sbcl_available
import engine_fallback

def print_topic_overview():
    banner = "=" * 74
    print("\n" + banner)
    print("  [SMARTCHEF] RECIPE SUGGESTION SYSTEM USING LIST PROCESSING")
    print("  Topic : Fundamentals of Artificial Intelligence (FAI)")
    print(banner)
    print("  * Core AI Paradigm : Symbolic Knowledge Representation & List Processing")
    print("  * Reasoning Engine : CAR / CDR / CONS Recursion + Set Partitioning")
    print("  * Knowledge Base   : 24 Curated Recipes (Indian & Global Cuisines)")
    print("  * Expert Rules     : 14 Smart Ingredient Substitution Association Rules")
    print(f"  * Active Engine    : {get_active_engine_name()}")
    print("  * AI Culinary Guru : Chef Smart (Groq Cloud LLM Active)")
    print(banner)

def run_quick_demo():
    print("\n  [DEMO] Testing List-Processing Engine on Sample Pantry Input:")
    sample_ingredients = ["tomato", "onion", "rice"]
    print(f"  --> User Pantry Ingredients : {sample_ingredients}")
    
    # Run suggestion engine
    res = suggest(sample_ingredients, diet="veg", max_time=60, sort_by="score")
    top_matches = res.get("results", [])
    
    if top_matches:
        top = top_matches[0]
        matched = top.get("matched_ingredients", [])
        score = top.get("score", 0)
        print(f"  --> Top Matched Dish        : {top.get('name')}")
        print(f"  --> Match Confidence        : {score}% ({len(matched)} ingredients matched)")
        print(f"  --> You Have in Pantry      : {', '.join(matched)}")
        print(f"  --> Cooking Duration        : {top.get('time')} minutes")
        print(f"  --> Total Recipes Evaluated : {res.get('total_evaluated', 24)}")
    print("-" * 74)

def print_server_links(host="127.0.0.1", port=5000):
    url = f"http://{host}:{port}"
    alt_url = f"http://localhost:{port}"
    banner = "=" * 74
    print("\n" + banner)
    print("  >>> SMARTCHEF WEBSITE IS LIVE AND READY! <<<")
    print(banner)
    print(f"  [+] Primary Web Link : {url}")
    print(f"  [+] Alternative Link : {alt_url}")
    print("  (Tip: Hold Ctrl and click the link above in VS Code to open)")
    print(banner + "\n")

def open_browser_delayed(url, delay=1.2):
    """Automatically launches the user's default browser after server starts."""
    def _open():
        time.sleep(delay)
        try:
            webbrowser.open(url)
        except Exception:
            pass
    threading.Thread(target=_open, daemon=True).start()

def main():
    print_topic_overview()
    run_quick_demo()
    
    host = "127.0.0.1"
    port = 5000
    url = f"http://{host}:{port}"
    
    print_server_links(host=host, port=port)
    open_browser_delayed(url, delay=1.0)
    
    # Start the Flask web server
    # debug=False here prevents double-printing banner in reloader subprocess
    app.run(host=host, port=port, debug=False)

if __name__ == "__main__":
    main()
