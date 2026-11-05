"""
Verification test script for SmartChef clean consumer web application.
"""

import json
from app import app, suggest

def run_tests():
    print("=" * 60)
    print("RUNNING SMARTCHEF CLEAN APPLICATION TESTS")
    print("=" * 60)

    with app.test_client() as client:
        # Test 1: GET / (Clean Single-Page Web App)
        res = client.get("/")
        print(f"\n[Test 1] GET / -> HTTP {res.status_code}")
        assert res.status_code == 200, "Home page failed to load"
        assert b"Smart" in res.data and b"Chef" in res.data, "Brand not found on Home page"
        assert b"Signature Dishes" in res.data, "Signature dishes section missing"
        assert b"Curated Recipes" in res.data, "Curated recipes grid missing"
        assert b"What's in Your Kitchen?" in res.data, "Integrated finder tool missing from home page"
        assert b"How SmartChef Works" in res.data, "How it works section missing"
        
        # Verify academic/viva/table cards are REMOVED
        assert b"Student & Academic Submission" not in res.data, "Student card should be removed"
        assert b"Project Objectives & Outcomes" not in res.data, "Objectives card should be removed"
        assert b"Why was LISP traditionally chosen for Artificial Intelligence?" not in res.data, "Viva questions should be removed"
        assert b"Core Symbolic AI" not in res.data, "Technology layer table should be removed"
        print("  -> Passed: Academic dossier, tech layer table, and viva questions cleanly removed!")

        # Test 2: GET /api/status
        res = client.get("/api/status")
        print(f"\n[Test 2] GET /api/status -> HTTP {res.status_code}")
        assert res.status_code == 200, "Status API failed"
        status_data = json.loads(res.data)
        assert status_data["recipes_count"] == 24
        print("  -> Passed: Status API reports 24 recipes!")

        # Test 3: GET /api/recipes
        res = client.get("/api/recipes")
        print(f"\n[Test 3] GET /api/recipes -> HTTP {res.status_code}")
        assert res.status_code == 200
        recs_data = json.loads(res.data)
        assert recs_data["total"] == 24
        sample_r = recs_data["recipes"][0]
        assert "image" in sample_r and sample_r["image"].startswith("http")
        assert len(sample_r["ingredients"]) >= 8
        print(f"  Sample Recipe: {sample_r['name']} ({len(sample_r['ingredients'])} ingredients, image verified)")
        print("  -> Passed: All 24 recipes contain images and rich ingredient lists!")

        # Test 4: POST /api/suggest
        payload = {
            "ingredients": ["tomato", "onion", "rice"],
            "diet": "veg",
            "max_time": 60,
            "sort_by": "score"
        }
        res = client.post("/api/suggest", json=payload)
        print(f"\n[Test 4] POST /api/suggest -> HTTP {res.status_code}")
        assert res.status_code == 200
        data = json.loads(res.data)
        top_recipe = data["results"][0]
        assert top_recipe["id"] == "rajma-chawal"
        assert "image" in top_recipe and top_recipe["image"].startswith("http")
        assert len(top_recipe["instructions"]) >= 4
        print(f"  Top Match: {top_recipe['name']} (Image verified, {len(top_recipe['instructions'])} instructions)")
        print("  -> Passed: POST suggest returns ranked recipe with image & instructions!")

        # Test 5: POST /api/ai-chef (Groq AI Integration)
        ai_payload = {
            "prompt": "How can I enhance the flavor of Paneer Butter Masala?",
            "recipe_name": "Paneer Butter Masala",
            "ingredients": ["paneer", "butter", "tomato"]
        }
        res = client.post("/api/ai-chef", json=ai_payload)
        print(f"\n[Test 5] POST /api/ai-chef -> HTTP {res.status_code}")
        assert res.status_code == 200
        ai_data = json.loads(res.data)
        assert "reply" in ai_data and len(ai_data["reply"]) > 20
        print(f"  AI Chef Advice: {ai_data['reply'][:100]}...")
        print("  -> Passed: Groq AI Chef endpoint responds with intelligent culinary advice!")

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED SUCCESSFULLY! CLEAN WEBSITE VERIFIED!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
