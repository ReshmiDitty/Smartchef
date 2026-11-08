"""
=============================================================================
SmartChef: Intelligent Recipe Suggestion Engine
Course: Fundamentals of Artificial Intelligence (FAI)
Topic: Recipe Suggestion System Using List Processing
=============================================================================
This module provides the core list-processing and pattern-matching reasoning
engine. It models recipes as symbolic list frames and implements functional
McCarthy list primitives (CAR, CDR, CONS, NULL, MEMBER) to perform set
matching, relative complement (missing ingredients), and rule-based substitutions.
=============================================================================
"""

import os
import json
from typing import List, Dict, Any, Tuple, Optional

# ---------------------------------------------------------------------------
# 1. FUNCTIONAL LIST PROCESSING PRIMITIVES
# ---------------------------------------------------------------------------

def car(lst: list) -> Any:
    """Returns the head (first element) of a list: (car '(a b c)) -> a."""
    if not lst:
        return None
    return lst[0]

def cdr(lst: list) -> list:
    """Returns the tail (remainder) of a list: (cdr '(a b c)) -> '(b c)."""
    if not lst or len(lst) <= 1:
        return []
    return lst[1:]

def cons(x: Any, lst: list) -> list:
    """Constructs a new list with x as head: (cons 'a '(b c)) -> '(a b c)."""
    return [x] + list(lst)

def null(lst: list) -> bool:
    """Tests if a list is empty: (null '()) -> T."""
    return lst is None or len(lst) == 0

def member(item: Any, lst: list) -> bool:
    """Recursive membership test: (member 'item '(a b c))."""
    if null(lst):
        return False
    if car(lst) == item:
        return True
    return member(item, cdr(lst))

# ---------------------------------------------------------------------------
# 2. ENRICHED KNOWLEDGE BASE: Base Curated Recipes with Images & Rich Ingredients
# ---------------------------------------------------------------------------
# Schema:
# [id, name, ingredients_list, diet, cooking_time, cuisine, image_url, description, instructions]

BASE_RECIPES: List[list] = [
    [
        "paneer-butter-masala",
        "Paneer Butter Masala",
        ["paneer", "butter", "tomato", "onion", "cream", "ginger", "garlic", "garam-masala", "cashews", "kasuri-methi", "cumin", "turmeric"],
        "veg",
        30,
        "North Indian",
        "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=800&q=80",
        "Tender cubes of cottage cheese simmered in a silky, mildly sweet and velvety tomato-butter gravy scented with kasuri methi.",
        [
            "Soak cashews in warm water for 15 minutes, then blend into a smooth cream paste.",
            "Sauté finely chopped onions, minced ginger, and garlic in butter until soft and golden.",
            "Add pureed vine-ripened tomatoes, turmeric, and cumin; cook on medium until oil separates from the masala.",
            "Stir in cashew paste, garam masala, crushed kasuri methi, and fresh heavy cream.",
            "Gently fold in fresh paneer cubes and simmer on low heat for 5 minutes before serving with hot naan."
        ]
    ],
    [
        "dal-tadka",
        "Restaurant-Style Dal Tadka",
        ["lentils", "onion", "tomato", "garlic", "ginger", "cumin", "ghee", "chili", "turmeric", "coriander", "mustard-seeds"],
        "veg",
        25,
        "Indian Comfort",
        "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=800&q=80",
        "Creamy yellow toor lentils tempered with sizzling ghee, crackling cumin seeds, fried garlic, and fresh green chilies.",
        [
            "Rinse yellow toor lentils and pressure cook with turmeric, salt, and water until soft and creamy.",
            "In a heavy tempering pan, heat pure ghee until shimmering.",
            "Add mustard seeds, cumin seeds, and finely chopped garlic; fry until the garlic turns golden brown.",
            "Stir in chopped ginger, green chilies, onions, and diced tomatoes, cooking until soft.",
            "Pour sizzling tadka over the hot cooked lentils and finish with a handful of chopped coriander."
        ]
    ],
    [
        "vegetable-biryani",
        "Royal Hyderabadi Veg Biryani",
        ["rice", "onion", "carrot", "peas", "potato", "yogurt", "biryani-masala", "mint", "ghee", "cardamom", "ginger", "garlic"],
        "veg",
        45,
        "Hyderabadi",
        "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80",
        "Aromatic long-grain basmati rice layered with spiced garden vegetables, saffron milk, fresh mint, and slow dum-cooked to perfection.",
        [
            "Parboil aged basmati rice with whole green cardamom and cloves until 70% cooked; drain.",
            "Sauté sliced onions in ghee until deeply caramelized (birista) and set half aside for garnishing.",
            "Toss carrots, peas, and potatoes with whisked yogurt, ginger-garlic paste, and biryani masala.",
            "In a heavy Dutch oven, layer spiced vegetable curry, parboiled rice, fresh mint, and fried onions.",
            "Seal tightly with foil and cook on gentle dum heat for 20 minutes to infuse the aromas."
        ]
    ],
    [
        "palak-paneer",
        "Creamy Palak Paneer",
        ["spinach", "paneer", "garlic", "onion", "tomato", "cream", "cumin", "ginger", "chili", "butter", "garam-masala"],
        "veg",
        30,
        "North Indian",
        "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=800&q=80",
        "Vibrant blanched spinach leaves puréed and simmered with fragrant garlic, butter, warming spices, and soft paneer.",
        [
            "Blanch fresh washed spinach leaves in salted boiling water for 2 minutes, then plunge into ice water to preserve green color.",
            "Blend cooled spinach into a silky vibrant green puree with one green chili.",
            "Melt butter in a pan, bloom cumin seeds, then sauté onions, minced garlic, and ginger until aromatic.",
            "Stir in finely diced tomatoes, garam masala, and salt until cooked through.",
            "Pour in the spinach puree, add paneer cubes, and finish with a swirl of fresh heavy cream."
        ]
    ],
    [
        "chana-masala",
        "Amritsari Chana Masala",
        ["chickpeas", "onion", "tomato", "ginger", "garlic", "coriander", "garam-masala", "cumin", "chili", "turmeric", "bay-leaf"],
        "veg",
        35,
        "Punjabi",
        "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=800&q=80",
        "Hearty chickpeas slow-cooked in a robust, tangy, and dark onion-tomato gravy infused with roasted cumin and coriander.",
        [
            "Pressure-cook soaked chickpeas with a bay leaf and salt until melt-in-the-mouth tender.",
            "Heat oil in a kadai, crackle cumin seeds, and brown finely grated onions until deep golden.",
            "Add ginger-garlic paste, green chilies, turmeric, coriander powder, and tomato puree; fry until oil separates.",
            "Stir in the boiled chickpeas along with their flavorful cooking broth and simmer for 15 minutes.",
            "Lightly mash a ladleful of chickpeas against the pan wall to thicken the gravy and finish with garam masala."
        ]
    ],
    [
        "aloo-gobi",
        "Homestyle Aloo Gobi",
        ["potato", "cauliflower", "onion", "tomato", "turmeric", "cumin", "coriander", "ginger", "garlic", "chili", "oil"],
        "veg",
        25,
        "North Indian",
        "https://images.unsplash.com/photo-1645177628172-a94c1f96e6db?auto=format&fit=crop&w=800&q=80",
        "Tender potatoes and crisp-tender cauliflower florets dry-tossed in roasted cumin, ginger juliennes, and fragrant spices.",
        [
            "Cut potatoes into wedges and cauliflower into equal medium-sized florets.",
            "Heat mustard oil or vegetable oil, add cumin seeds and sliced ginger juliennes.",
            "Sauté onions and garlic until fragrant, then add turmeric, coriander powder, and chopped tomatoes.",
            "Add the potato cubes and cauliflower florets; toss well until each vegetable is coated in masala.",
            "Cover tightly and steam-cook on low heat for 15 minutes until vegetables are tender with crisp caramelized edges."
        ]
    ],
    [
        "masala-dosa",
        "Crispy South Indian Masala Dosa",
        ["rice", "potato", "onion", "mustard-seeds", "curry-leaves", "turmeric", "chili", "ginger", "ghee", "oil"],
        "veg",
        20,
        "South Indian",
        "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?auto=format&fit=crop&w=800&q=80",
        "Golden crispy fermented rice crepe stuffed with a spiced turmeric mashed potato filling, served with coconut chutney.",
        [
            "Boil potatoes until soft, peel, and coarsely mash with fingers.",
            "Heat oil in a skillet, splutter black mustard seeds, curry leaves, and minced ginger.",
            "Sauté sliced onions and green chilies with turmeric powder until translucent.",
            "Stir in the mashed potatoes, splash 3 tablespoons of water, and simmer for 3 minutes to make the stuffing.",
            "Spread fermented rice batter in concentric circles on a sizzling hot tawa, drizzle ghee, cook golden, add filling and roll."
        ]
    ],
    [
        "rajma-chawal",
        "Delhi Style Rajma Masala",
        ["kidney-beans", "onion", "tomato", "ginger", "garlic", "rice", "cumin", "coriander", "garam-masala", "butter", "bay-leaf"],
        "veg",
        40,
        "North Indian",
        "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80",
        "Plump red kidney beans slow-simmered in a rich tomato, ginger, and onion gravy served over fluffy basmati cumin rice.",
        [
            "Soak red kidney beans overnight, then pressure cook with a bay leaf and salt until thoroughly soft.",
            "In a Dutch oven, heat butter and oil, bloom cumin seeds, and fry minced onions until deeply caramelized.",
            "Add freshly grated ginger, garlic, ground coriander, and pureed tomatoes; roast until fragrant.",
            "Combine the tender kidney beans and their cooking liquid; simmer on medium-low for 25 minutes.",
            "Mash some beans to build a thick, velvety gravy and serve steaming over fragrant steamed basmati rice."
        ]
    ],
    [
        "butter-chicken",
        "Classic Old Delhi Butter Chicken",
        ["chicken", "butter", "tomato", "cream", "ginger", "garlic", "garam-masala", "yogurt", "kasuri-methi", "chili", "cashews"],
        "non-veg",
        40,
        "Mughlai",
        "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=800&q=80",
        "Smoky tandoori chicken pieces simmered in an indulgent, creamy makhani gravy enriched with butter, honey, and kasuri methi.",
        [
            "Marinate chicken cubes in yogurt, ginger-garlic paste, Kashmiri chili, and salt for 1 hour.",
            "Sear chicken in a smoking hot grill pan until charred and 80% cooked.",
            "Simmer pureed plum tomatoes with ginger, garlic, soaked cashew paste, and butter for 20 minutes.",
            "Strain the tomato sauce to ensure silkiness, then fold in grilled chicken pieces.",
            "Finish with generous butter, heavy cream, crushed kasuri methi, and a pinch of garam masala."
        ]
    ],
    [
        "chicken-tikka",
        "Charred Tandoori Chicken Tikka",
        ["chicken", "yogurt", "lemon", "ginger", "garlic", "chili", "garam-masala", "cumin", "coriander", "mustard-oil"],
        "non-veg",
        35,
        "Tandoori",
        "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?auto=format&fit=crop&w=800&q=80",
        "Succulent boneless chicken skewers bathed in a vibrant spiced yogurt marinade, charred to juicy perfection.",
        [
            "Cut chicken breast or boneless thighs into uniform 1.5-inch bite-sized cubes.",
            "Whisk thick Greek hung yogurt with lemon juice, mustard oil, ginger-garlic paste, and red chili powder.",
            "Stir in garam masala, roasted cumin powder, and coriander powder; toss chicken evenly.",
            "Thread chicken cubes onto skewers and rest for 30 minutes for flavors to penetrate.",
            "Roast in a blazing 220°C oven or open grill for 15 minutes, basting with butter until gorgeously charred."
        ]
    ],
    [
        "egg-curry",
        "Spiced Dhaba Egg Curry",
        ["egg", "onion", "tomato", "garlic", "ginger", "turmeric", "coriander", "cumin", "garam-masala", "chili", "oil"],
        "non-veg",
        25,
        "Indian",
        "https://images.unsplash.com/photo-1505253758473-96b3015f27eb?auto=format&fit=crop&w=800&q=80",
        "Crispy pan-fried hard-boiled eggs steeped in an aromatic, homestyle onion and tomato gravy with warming spices.",
        [
            "Hard-boil 4 eggs, peel, prick lightly with a fork, and toss with turmeric and chili powder.",
            "Flash-fry eggs in hot oil for 2 minutes until blistered and golden; remove and set aside.",
            "In the remaining spiced oil, sizzle cumin seeds, then sauté minced onions until caramelized.",
            "Add ginger-garlic paste, pureed tomatoes, and ground spices; simmer until oil glistens on top.",
            "Slice boiled eggs in halves or leave whole, immerse in the bubbling sauce, and simmer for 5 minutes."
        ]
    ],
    [
        "mutton-rogan-josh",
        "Authentic Kashmiri Mutton Rogan Josh",
        ["mutton", "yogurt", "onion", "garlic", "ginger", "fennel", "cardamom", "chili", "cloves", "cinnamon", "mustard-oil"],
        "non-veg",
        60,
        "Kashmiri",
        "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
        "Tender bone-in mutton pieces slow-braised in mustard oil with Kashmiri chilies, ground fennel, and whole fragrant spices.",
        [
            "Heat authentic mustard oil until smoking, let it cool slightly, then sear mutton pieces until browned.",
            "Add cracked black cardamoms, cinnamon stick, cloves, and asafoetida into the pot.",
            "In a bowl, whisk fresh curd with Kashmiri chili powder, ground ginger (sonth), and fennel seed powder (saunf).",
            "Pour yogurt mixture into the mutton, stirring continuously over low heat so the curd doesn't curdle.",
            "Cover tightly and slow-cook on low heat for 50 minutes until meat becomes fork-tender and pulls away from bone."
        ]
    ],
    [
        "fish-curry",
        "Goan Coconut Fish Curry",
        ["fish", "coconut-milk", "tomato", "onion", "curry-leaves", "mustard-seeds", "chili", "turmeric", "garlic", "oil"],
        "non-veg",
        30,
        "Goan Coastal",
        "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=800&q=80",
        "Fresh tender fish fillets gently poached in a creamy, tangy coconut milk sauce infused with curry leaves and mustard seeds.",
        [
            "Season fresh fish fillets (kingfish, cod, or salmon) with sea salt and turmeric powder.",
            "Heat coconut oil in an earthenware pot; temper mustard seeds, sliced green chilies, and fresh curry leaves.",
            "Sauté finely diced onions and garlic until soft, then stir in chopped tomatoes and turmeric.",
            "Pour in freshly pressed thick coconut milk and bring to a gentle, fragrant simmer.",
            "Slide fish fillets gently into the sauce and simmer for 7 minutes without stirring vigorously until cooked."
        ]
    ],
    [
        "pasta-aglio-e-olio",
        "Classic Italian Pasta Aglio e Olio",
        ["pasta", "olive-oil", "garlic", "chili", "parsley", "parmesan", "black-pepper", "sea-salt", "lemon"],
        "veg",
        15,
        "Italian",
        "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=800&q=80",
        "Spaghetti tossed with golden toasted garlic slices, crushed red chili flakes, extra virgin olive oil, and fresh Italian parsley.",
        [
            "Boil spaghetti in generously salted water until 1 minute before al dente; reserve 1 cup of pasta cooking water.",
            "In a wide skillet, heat extra virgin olive oil over gentle medium-low heat with thinly sliced garlic cloves.",
            "Allow garlic to slowly turn golden-straw colored (do not burn), then toss in red chili flakes.",
            "Transfer hot spaghetti straight into the garlic oil and pour in 1/2 cup of starchy pasta water.",
            "Swirl and toss vigorously over heat to form a glossy emulsified sauce; finish with fresh parsley and parmesan."
        ]
    ],
    [
        "margherita-pizza",
        "Neapolitan Pizza Margherita",
        ["flour", "tomato", "mozzarella", "basil", "olive-oil", "yeast", "sea-salt", "garlic", "oregano"],
        "veg",
        25,
        "Italian",
        "https://images.unsplash.com/photo-1604382355076-af4b0eb60143?auto=format&fit=crop&w=800&q=80",
        "Artisanal wood-fired style pizza with a blistered crust, sweet San Marzano tomato sauce, milky fresh mozzarella, and sweet basil.",
        [
            "Stretch proofed fermented dough ball by hand on a floured surface to form a 10-inch round crust with a raised border.",
            "Crush whole San Marzano canned tomatoes with salt, oregano, and olive oil; spread lightly across crust.",
            "Tear fresh whole-milk mozzarella balls into chunks and scatter evenly over the sauce.",
            "Slide pizza onto a pre-heated baking stone or steel at maximum oven temperature (250°C+) for 7-9 minutes.",
            "Remove blistered pizza and immediately crown with fresh sweet basil leaves and a stream of extra virgin olive oil."
        ]
    ],
    [
        "greek-salad",
        "Authentic Mediterranean Greek Salad",
        ["cucumber", "tomato", "olive-oil", "feta-cheese", "olives", "onion", "oregano", "lemon", "sea-salt"],
        "veg",
        10,
        "Mediterranean",
        "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80",
        "Crisp Persian cucumbers, vine-ripened tomatoes, pungent Kalamata olives, and a slab of Greek feta dressed in olive oil and wild oregano.",
        [
            "Chop sweet ripe tomatoes into wedges and Persian cucumbers into thick half-moon rounds.",
            "Thinly shave crisp red onion and toss gently in a large salad bowl with whole pitted Kalamata olives.",
            "Whisk extra virgin olive oil with lemon juice, sea salt, and dried Mediterranean oregano for the dressing.",
            "Drizzle dressing over the crisp vegetable mix and toss gently to coat.",
            "Top with a generous whole slab of Greek sheep's milk feta cheese and dust with extra crushed oregano."
        ]
    ],
    [
        "vegetable-stir-fry",
        "Crisp Asian Vegetable Stir-Fry",
        ["noodles", "broccoli", "soy-sauce", "carrot", "garlic", "sesame-oil", "ginger", "bell-pepper", "chili", "oil"],
        "veg",
        20,
        "Asian",
        "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=800&q=80",
        "Crunchy broccoli florets, carrots, and sweet bell peppers wok-tossed with egg noodles in an umami garlic-ginger soy glaze.",
        [
            "Cook egg noodles or wheat noodles in boiling water for 3 minutes; rinse with cold water and toss with sesame oil.",
            "Whisk light soy sauce, minced ginger, garlic, a splash of water, and chili flakes in a small bowl.",
            "Heat a wok over high flame until smoking; add 1 tablespoon vegetable oil.",
            "Flash-fry broccoli florets, julienned carrots, and bell pepper strips for 2 minutes until tender-crisp.",
            "Add noodles and sauce; toss continuously with tongs over high heat for 2 minutes until thoroughly glazed."
        ]
    ],
    [
        "minestrone-soup",
        "Tuscan Vegetable Minestrone",
        ["pasta", "beans", "tomato", "carrot", "celery", "onion", "garlic", "olive-oil", "parmesan", "basil", "oregano"],
        "veg",
        30,
        "Italian",
        "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80",
        "A nourishing Italian rustic soup loaded with cannellini white beans, garden vegetables, pasta, and fragrant fresh herbs.",
        [
            "Warm extra virgin olive oil in a soup pot and sweat diced yellow onion, celery, and carrots with garlic.",
            "Add crushed canned tomatoes, dried oregano, and vegetable stock; bring to a lively boil.",
            "Stir in drained white cannellini beans and simmer gently on medium-low heat for 15 minutes.",
            "Add small ditalini or macaroni pasta and cook until pasta is al dente (approx 8 minutes).",
            "Ladle into soup bowls, finish with torn basil leaves, and grate fresh Parmigiano-Reggiano over the top."
        ]
    ],
    [
        "mushroom-risotto",
        "Creamy Wild Mushroom Risotto",
        ["rice", "mushroom", "onion", "garlic", "vegetable-broth", "butter", "parmesan", "olive-oil", "black-pepper", "parsley"],
        "veg",
        35,
        "Italian",
        "https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?auto=format&fit=crop&w=800&q=80",
        "Creamy slow-stirred Arborio rice studded with pan-caramelized wild mushrooms, finished with cold butter and aged parmesan.",
        [
            "Slice cremini or wild mushrooms; sauté in a hot skillet with butter until deeply caramelized and brown; set aside.",
            "In a wide heavy saucepan, sweat finely chopped shallots and minced garlic in olive oil until soft.",
            "Add Arborio rice and toast dry grains for 2 minutes until translucent around the edges.",
            "Ladle in hot vegetable broth one cup at a time, stirring continuously until each addition is absorbed.",
            "When rice is al dente, pull pan off heat and vigorously beat in cold butter cubes, parmesan, and mushrooms."
        ]
    ],
    [
        "guacamole-nachos",
        "Loaded Fresh Guacamole & Nachos",
        ["avocado", "lime", "onion", "tomato", "cilantro", "tortilla-chips", "chili", "garlic", "sea-salt"],
        "veg",
        10,
        "Mexican",
        "https://images.unsplash.com/photo-1541544741938-0af808871cc0?auto=format&fit=crop&w=800&q=80",
        "Creamy ripe Hass avocados hand-mashed with lime juice, minced jalapeño, roma tomatoes, and fresh cilantro, served with tortilla chips.",
        [
            "Slice ripe Hass avocados in half, remove seeds, and scoop flesh into a mortar or shallow bowl.",
            "Coarsely mash avocados with a fork, preserving satisfying chunks for authentic texture.",
            "Fold in finely diced red onions, seeded diced roma tomatoes, minced jalapeño, and garlic.",
            "Squeeze fresh lime juice liberally and season with coarse sea salt and chopped cilantro leaves.",
            "Taste and adjust lime-salt balance, then serve immediately alongside crispy golden corn tortilla chips."
        ]
    ],
    [
        "chicken-alfredo",
        "Fettuccine Chicken Alfredo",
        ["pasta", "chicken", "cream", "butter", "garlic", "parmesan", "black-pepper", "parsley", "olive-oil"],
        "non-veg",
        25,
        "Italian-American",
        "https://images.unsplash.com/photo-1645112411341-6c4fd023714a?auto=format&fit=crop&w=800&q=80",
        "Tender grilled chicken strips nestled over ribbons of fettuccine pasta in a rich, velvety garlic parmesan cream sauce.",
        [
            "Boil fettuccine pasta in salted water until al dente; drain and save 1/2 cup of pasta water.",
            "Season chicken breasts with salt, pepper, and garlic powder; sear in olive oil until golden and fully cooked; slice.",
            "Melt pure butter in the skillet, gently sizzle minced garlic, then pour in heavy whipping cream.",
            "Simmer sauce gently for 4 minutes until thickened, then gradually whisk in freshly grated parmesan cheese.",
            "Toss hot fettuccine and sliced chicken into the sauce until coated; garnish with freshly cracked black pepper."
        ]
    ],
    [
        "classic-burger",
        "Gourmet Cheeseburger Deluxe",
        ["chicken-patty", "bun", "lettuce", "tomato", "cheese", "onion", "mayo", "butter", "pickles", "oil"],
        "non-veg",
        20,
        "American",
        "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=800&q=80",
        "Juicy seared seasoned patty topped with melted aged cheddar, crisp lettuce, tomato, pickles, and burger sauce in a brioche bun.",
        [
            "Preheat a cast iron skillet or flat griddle until searing hot.",
            "Season the patty generously on both sides with sea salt and cracked black pepper.",
            "Sear patty for 4 minutes, flip, and immediately drape with a thick slice of cheddar cheese to melt.",
            "Slice brioche buns, spread butter, and toast on the griddle until golden and crisp.",
            "Build burger: spread mayo on bottom bun, add crisp romaine lettuce, sliced ripe tomato, patty, pickles, and top bun."
        ]
    ],
    [
        "grilled-salmon",
        "Pan-Seared Salmon with Lemon Herb Butter",
        ["salmon", "lemon", "olive-oil", "garlic", "black-pepper", "rosemary", "butter", "sea-salt", "parsley"],
        "non-veg",
        20,
        "Continental",
        "https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=800&q=80",
        "Crispy skin salmon fillet seared in extra virgin olive oil, basted with bubbling garlic-rosemary butter and fresh lemon.",
        [
            "Pat fresh salmon fillets completely dry with paper towels; season skin and flesh with salt and black pepper.",
            "Heat extra virgin olive oil in a heavy stainless or cast-iron skillet over medium-high heat until shimmering.",
            "Lay salmon skin-side down; press lightly with a spatula for 10 seconds to ensure even skin contact.",
            "Cook undisturbed for 5 minutes until skin is crackling and crisp, then gently flip over.",
            "Add butter cubes, smashed garlic, and rosemary sprigs to the pan; spoon foaming butter over salmon for 2 minutes."
        ]
    ],
    [
        "chicken-katsu-curry",
        "Japanese Crispy Chicken Katsu Curry",
        ["chicken", "egg", "breadcrumbs", "curry-paste", "potato", "carrot", "rice", "onion", "oil", "soy-sauce"],
        "non-veg",
        40,
        "Japanese",
        "https://images.unsplash.com/photo-1606851094655-b2593a9af63f?auto=format&fit=crop&w=800&q=80",
        "Golden crunchy panko-crusted chicken cutlet served over steamed rice with a fragrant, silky Japanese vegetable curry sauce.",
        [
            "Pound chicken breast cutlet to uniform thickness; season with salt and pepper.",
            "Dredge chicken through flour, beaten egg, and firmly press into flaky panko breadcrumbs.",
            "In a saucepan, sauté onions, carrots, and potatoes; add water and simmer until vegetables are fork-tender.",
            "Dissolve Japanese curry roux blocks into the broth, stirring until rich, thick, and fragrant.",
            "Deep-fry panko chicken in 175°C oil until golden brown; slice into strips and plate with hot rice and curry sauce."
        ]
    ]
]

# ---------------------------------------------------------------------------
# DYNAMIC KNOWLEDGE BASE & USER CONTRIBUTIONS
# ---------------------------------------------------------------------------
CUSTOM_RECIPES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "custom_recipes.json")

def load_custom_recipes() -> List[list]:
    """Loads user-added recipes from persistent JSON file and converts to list format."""
    if not os.path.exists(CUSTOM_RECIPES_FILE):
        return []
    try:
        with open(CUSTOM_RECIPES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            custom_list = []
            for item in data:
                custom_list.append([
                    item.get("id"),
                    item.get("name"),
                    item.get("ingredients", []),
                    item.get("diet", "veg"),
                    int(item.get("time", 30)),
                    item.get("cuisine", "Custom"),
                    item.get("image", "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80"),
                    item.get("description", ""),
                    item.get("instructions", [])
                ])
            return custom_list
    except Exception:
        return []

# Dynamic full recipe list (Base Curated + User Contributed)
RECIPES: List[list] = list(BASE_RECIPES) + load_custom_recipes()

def reload_all_recipes() -> List[list]:
    """Reloads recipes combining base curated recipes and custom user additions."""
    global RECIPES
    RECIPES = list(BASE_RECIPES) + load_custom_recipes()
    return RECIPES

def save_custom_recipe(recipe_dict: dict) -> list:
    """Validates and appends a new user recipe to custom_recipes.json, returning the recipe list."""
    name = str(recipe_dict.get("name", "Custom Recipe")).strip()
    raw_id = recipe_dict.get("id") or name.lower().replace(" ", "-")
    rec_id = "".join(c for c in raw_id if c.isalnum() or c in "-_")
    
    # Process ingredients
    raw_ings = recipe_dict.get("ingredients", [])
    if isinstance(raw_ings, str):
        ings = [i.strip().lower().replace(" ", "-") for i in raw_ings.split(",") if i.strip()]
    else:
        ings = [str(i).strip().lower().replace(" ", "-") for i in raw_ings if str(i).strip()]
        
    diet = "non-veg" if str(recipe_dict.get("diet")).lower() in ["non-veg", "nonveg", "non_veg"] else "veg"
    time_val = int(recipe_dict.get("time") or 30)
    cuisine = str(recipe_dict.get("cuisine") or "Global").strip()
    
    # Fallback image if blank
    image = str(recipe_dict.get("image") or "").strip()
    if not image or not image.startswith("http"):
        if diet == "veg":
            image = "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=800&q=80"
        else:
            image = "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80"
            
    desc = str(recipe_dict.get("description") or f"A delicious creation of {name} prepared with fresh ingredients.").strip()
    
    raw_instructions = recipe_dict.get("instructions", [])
    if isinstance(raw_instructions, str):
        instructions = [s.strip() for s in raw_instructions.split("\n") if s.strip()]
    else:
        instructions = [str(s).strip() for s in raw_instructions if str(s).strip()]
    if not instructions:
        instructions = [
            "Prepare, clean, and measure all fresh ingredients according to list.",
            "Sauté aromatics and combine with main components on medium heat.",
            "Simmer until flavors are rich and fully melded, then garnish and serve hot."
        ]
        
    recipe_entry = {
        "id": rec_id,
        "name": name,
        "ingredients": ings,
        "diet": diet,
        "time": time_val,
        "cuisine": cuisine,
        "image": image,
        "description": desc,
        "instructions": instructions
    }
    
    existing = []
    if os.path.exists(CUSTOM_RECIPES_FILE):
        try:
            with open(CUSTOM_RECIPES_FILE, "r", encoding="utf-8") as f:
                existing = json.load(f)
        except Exception:
            existing = []
            
    existing = [e for e in existing if e.get("id") != rec_id]
    existing.append(recipe_entry)
    
    with open(CUSTOM_RECIPES_FILE, "w", encoding="utf-8") as f:
        json.dump(existing, f, indent=2)
        
    reload_all_recipes()
    return [rec_id, name, ings, diet, time_val, cuisine, image, desc, instructions]

# Substitution Rules: (substitute_symbol, standard_recipe_ingredient_symbol)
SUBSTITUTION_RULES: List[Tuple[str, str]] = [
    ("olive-oil", "butter"),
    ("oil", "butter"),
    ("oil", "ghee"),
    ("tofu", "paneer"),
    ("milk", "cream"),
    ("yogurt", "cream"),
    ("cheddar", "parmesan"),
    ("cheddar", "mozzarella"),
    ("cheese", "feta-cheese"),
    ("mushroom", "chicken"),
    ("chia-seeds", "egg"),
    ("honey", "sugar"),
    ("tomato-paste", "tomato"),
    ("lemon", "lime")
]

# ---------------------------------------------------------------------------
# 3. RECIPE ACCESSORS (Selectors)
# ---------------------------------------------------------------------------

def recipe_id(recipe: list) -> str:
    """Returns recipe ID: car(recipe)."""
    return car(recipe)

def recipe_name(recipe: list) -> str:
    """Returns recipe formatted title: car(cdr(recipe))."""
    return car(cdr(recipe))

def recipe_ingredients(recipe: list) -> list:
    """Returns recipe ingredients list: car(cdr(cdr(recipe)))."""
    return car(cdr(cdr(recipe)))

def recipe_diet(recipe: list) -> str:
    """Returns recipe diet: car(cdr(cdr(cdr(recipe))))."""
    return car(cdr(cdr(cdr(recipe))))

def recipe_time(recipe: list) -> int:
    """Returns cooking time in minutes: car(cdr(cdr(cdr(cdr(recipe)))))."""
    return car(cdr(cdr(cdr(cdr(recipe)))))

def recipe_cuisine(recipe: list) -> str:
    """Returns cuisine: car(cdr(cdr(cdr(cdr(cdr(recipe))))))."""
    return car(cdr(cdr(cdr(cdr(cdr(recipe))))))

def recipe_image(recipe: list) -> str:
    """Returns image URL: car(cdr(cdr(cdr(cdr(cdr(cdr(recipe)))))))."""
    return car(cdr(cdr(cdr(cdr(cdr(cdr(recipe)))))))

def recipe_description(recipe: list) -> str:
    """Returns description: car(cdr(cdr(cdr(cdr(cdr(cdr(cdr(recipe))))))))."""
    return car(cdr(cdr(cdr(cdr(cdr(cdr(cdr(recipe))))))))

def recipe_instructions(recipe: list) -> list:
    """Returns step-by-step instructions list."""
    # 9th element: car(cdr(cdr(cdr(cdr(cdr(cdr(cdr(cdr(recipe)))))))))
    val = car(cdr(cdr(cdr(cdr(cdr(cdr(cdr(cdr(recipe)))))))))
    return val if val is not None else []

# ---------------------------------------------------------------------------
# 4. RECURSIVE LIST PROCESSING ALGORITHMS
# ---------------------------------------------------------------------------

def get_substitutes_for(item: str, sub_list: list) -> list:
    """Recursively finds all candidate items that can substitute for ITEM."""
    if null(sub_list):
        return []
    head_pair = car(sub_list)
    substitute_candidate = head_pair[0]
    needed_target = head_pair[1]
    
    rest = get_substitutes_for(item, cdr(sub_list))
    if needed_target == item:
        return cons(substitute_candidate, rest)
    return rest

def find_first_available(candidates: list, user_items: list) -> Tuple[bool, Optional[str]]:
    """Recursively checks candidates to find the first one present in USER_ITEMS."""
    if null(candidates):
        return (False, None)
    head_candidate = car(candidates)
    if member(head_candidate, user_items):
        return (True, head_candidate)
    return find_first_available(cdr(candidates), user_items)

def has_ingredient_or_substitute(needed_item: str, user_items: list, sub_list: list) -> Tuple[bool, Optional[str], bool]:
    """Tests if user has needed_item directly or via an acceptable substitute."""
    if member(needed_item, user_items):
        return (True, needed_item, False)
    
    candidates = get_substitutes_for(needed_item, sub_list)
    found, sub_used = find_first_available(candidates, user_items)
    if found:
        return (True, sub_used, True)
    
    return (False, None, False)

def get_matched_and_missing(user_ingredients: list, recipe_ingredients_list: list, sub_list: list) -> Tuple[list, list, list]:
    """
    Recursive set partitioning:
    Splits recipe_ingredients_list into (matched_list, missing_list, substitutions_applied).
    Pure list traversal using car and cdr recursion.
    """
    def traverse(remaining_needed: list, matched: list, missing: list, subs: list):
        if null(remaining_needed):
            return (matched, missing, subs)
        
        item = car(remaining_needed)
        has_it, matched_as, is_sub = has_ingredient_or_substitute(item, user_ingredients, sub_list)
        
        if has_it:
            if is_sub:
                return traverse(
                    cdr(remaining_needed),
                    cons(matched_as, matched),
                    missing,
                    cons({"user_has": matched_as, "replaces": item}, subs)
                )
            else:
                return traverse(
                    cdr(remaining_needed),
                    cons(item, matched),
                    missing,
                    subs
                )
        else:
            return traverse(
                cdr(remaining_needed),
                matched,
                cons(item, missing),
                subs
            )

    return traverse(recipe_ingredients_list, [], [], [])

def count_matches(user_ingredients: list, recipe_ingredients_list: list, sub_list: list) -> int:
    """Counts how many ingredients are satisfied by the user using recursion."""
    if null(recipe_ingredients_list):
        return 0
    item = car(recipe_ingredients_list)
    has_it, _, _ = has_ingredient_or_substitute(item, user_ingredients, sub_list)
    score_increment = 1 if has_it else 0
    return score_increment + count_matches(user_ingredients, cdr(recipe_ingredients_list), sub_list)

def missing_ingredients(user_ingredients: list, recipe_ingredients_list: list, sub_list: list) -> list:
    """Returns missing ingredients as set difference via recursive partitioning."""
    _, missing, _ = get_matched_and_missing(user_ingredients, recipe_ingredients_list, sub_list)
    return missing

def match_score(matches: int, total: int) -> float:
    """Calculates percentage score: (matches / total) * 100."""
    if total == 0:
        return 0.0
    return round((matches / total) * 100.0, 2)

# ---------------------------------------------------------------------------
# 5. FILTERING, RANKING & SUGGESTION
# ---------------------------------------------------------------------------

def filter_by_diet(recipe_list: list, desired_diet: str) -> list:
    """Filters recipes by dietary requirement: 'veg', 'non-veg', or 'all'."""
    if not desired_diet or desired_diet.lower() == "all":
        return recipe_list
    target = desired_diet.lower()
    return [r for r in recipe_list if recipe_diet(r) == target]

def filter_by_time(recipe_list: list, max_time: Optional[int]) -> list:
    """Filters recipes by maximum cooking time."""
    if not max_time or max_time <= 0:
        return recipe_list
    return [r for r in recipe_list if recipe_time(r) <= max_time]

def evaluate_recipe(recipe: list, user_ingredients: list, sub_list: list) -> Dict[str, Any]:
    """Evaluates a recipe against user ingredients and produces a comprehensive presentation object."""
    rec_ings = recipe_ingredients(recipe)
    total_count = len(rec_ings)
    matched, missing, subs = get_matched_and_missing(user_ingredients, rec_ings, sub_list)
    matches_count = len(matched)
    score = match_score(matches_count, total_count)

    return {
        "id": recipe_id(recipe),
        "name": recipe_name(recipe),
        "ingredients": rec_ings,
        "diet": recipe_diet(recipe),
        "time": recipe_time(recipe),
        "cuisine": recipe_cuisine(recipe),
        "image": recipe_image(recipe),
        "description": recipe_description(recipe),
        "score": score,
        "matched_count": matches_count,
        "total_count": total_count,
        "matched_ingredients": matched,
        "missing_ingredients": missing,
        "substitutions_applied": subs,
        "instructions": recipe_instructions(recipe)
    }

def suggest_recipes(
    recipes: list = None,
    user_ingredients: list = None,
    diet: str = "all",
    max_time: int = 120,
    min_score: float = 1.0,
    sort_by: str = "score"
) -> Dict[str, Any]:
    """
    Main recommendation entrypoint.
    Applies filters, computes list-matching scores, and sorts ranked results.
    Strictly filters out recipes that do not contain user's selected ingredients.
    """
    if recipes is None:
        recipes = RECIPES
    if user_ingredients is None:
        user_ingredients = []
    
    # Normalize user ingredients (lowercase, hyphenated)
    norm_user = [ing.strip().lower().replace(" ", "-") for ing in user_ingredients if ing.strip()]
    
    diet_filtered = filter_by_diet(recipes, diet)
    time_filtered = filter_by_time(diet_filtered, max_time)
    
    evaluated = [evaluate_recipe(r, norm_user, SUBSTITUTION_RULES) for r in time_filtered]
    
    if norm_user:
        # Strictly require recipes to contain user's selected ingredients
        has_matches = [ev for ev in evaluated if ev["matched_count"] > 0 and ev["score"] > 0]
        
        if not has_matches:
            qualified = []
        else:
            max_matched = max(ev["matched_count"] for ev in has_matches)
            # If user selected multiple ingredients and strong multi-match recipes exist,
            # require at least 2 matched ingredients to exclude weak 1-ingredient noise
            if len(norm_user) >= 2 and max_matched >= 2:
                qualified = [ev for ev in has_matches if ev["matched_count"] >= 2]
            else:
                qualified = [ev for ev in has_matches if ev["matched_count"] >= 1]
    else:
        qualified = evaluated

    # Sort results: primary by matched_count desc, then score desc, then time asc
    if sort_by == "time":
        ranked = sorted(qualified, key=lambda x: (x["time"], -x["matched_count"], -x["score"]))
    elif sort_by == "missing":
        ranked = sorted(qualified, key=lambda x: (len(x["missing_ingredients"]), -x["matched_count"], -x["score"]))
    else: # default: matched_count descending, then score descending, then time ascending
        ranked = sorted(qualified, key=lambda x: (-x["matched_count"], -x["score"], x["time"]))

    return {
        "engine": "Smart List-Processing Engine",
        "total_evaluated": len(recipes),
        "total_matches": len(ranked),
        "user_ingredients": norm_user,
        "diet_filter": diet,
        "max_time_filter": max_time,
        "results": ranked
    }

def get_all_ingredients(recipes: list = None) -> List[str]:
    """Extracts all unique ingredients sorted alphabetically."""
    if recipes is None:
        recipes = RECIPES
    all_ings = set()
    for r in recipes:
        for ing in recipe_ingredients(r):
            all_ings.add(ing)
    return sorted(list(all_ings))

if __name__ == "__main__":
    print("Testing SmartChef List-Processing Engine...")
    test_res = suggest_recipes(RECIPES, ["tomato", "onion", "rice"], diet="veg", max_time=60)
    print("Top Match:", test_res["results"][0]["name"], f"({test_res['results'][0]['score']}%)")
    assert test_res["results"][0]["id"] == "rajma-chawal"
    print("Test passed successfully!")
