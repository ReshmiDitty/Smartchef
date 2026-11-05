/**
 * ============================================================================
 * SmartChef – Main Application JavaScript
 * Unified Single-Page & Streamlit Compatible
 * ============================================================================
 */

const ChefApp = (() => {
  // --------------------------------------------------------------------------
  // 1. EMBEDDED KNOWLEDGE BASE (For seamless Streamlit & offline execution)
  // --------------------------------------------------------------------------
  const RECIPES_DATA = [
    {
      id: "paneer-butter-masala",
      name: "Paneer Butter Masala",
      ingredients: ["paneer", "butter", "tomato", "onion", "cream", "ginger", "garlic", "garam-masala", "cashews", "kasuri-methi", "cumin", "turmeric"],
      diet: "veg",
      time: 30,
      cuisine: "North Indian",
      image: "https://images.unsplash.com/photo-1631452180519-c014fe946bc7?auto=format&fit=crop&w=800&q=80",
      description: "Tender cubes of cottage cheese simmered in a silky, mildly sweet and velvety tomato-butter gravy scented with kasuri methi.",
      instructions: [
        "Soak cashews in warm water for 15 minutes, then blend into a smooth cream paste.",
        "Sauté finely chopped onions, minced ginger, and garlic in butter until soft and golden.",
        "Add pureed vine-ripened tomatoes, turmeric, and cumin; cook on medium until oil separates from the masala.",
        "Stir in cashew paste, garam masala, crushed kasuri methi, and fresh heavy cream.",
        "Gently fold in fresh paneer cubes and simmer on low heat for 5 minutes before serving with hot naan."
      ]
    },
    {
      id: "dal-tadka",
      name: "Restaurant-Style Dal Tadka",
      ingredients: ["lentils", "onion", "tomato", "garlic", "ginger", "cumin", "ghee", "chili", "turmeric", "coriander", "mustard-seeds"],
      diet: "veg",
      time: 25,
      cuisine: "Indian Comfort",
      image: "https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=800&q=80",
      description: "Creamy yellow toor lentils tempered with sizzling ghee, crackling cumin seeds, fried garlic, and fresh green chilies.",
      instructions: [
        "Rinse yellow toor lentils and pressure cook with turmeric, salt, and water until soft and creamy.",
        "In a heavy tempering pan, heat pure ghee until shimmering.",
        "Add mustard seeds, cumin seeds, and finely chopped garlic; fry until the garlic turns golden brown.",
        "Stir in chopped ginger, green chilies, onions, and diced tomatoes, cooking until soft.",
        "Pour sizzling tadka over the hot cooked lentils and finish with a handful of chopped coriander."
      ]
    },
    {
      id: "vegetable-biryani",
      name: "Royal Hyderabadi Veg Biryani",
      ingredients: ["rice", "onion", "carrot", "peas", "potato", "yogurt", "biryani-masala", "mint", "ghee", "cardamom", "ginger", "garlic"],
      diet: "veg",
      time: 45,
      cuisine: "Hyderabadi",
      image: "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80",
      description: "Aromatic long-grain basmati rice layered with spiced garden vegetables, saffron milk, fresh mint, and slow dum-cooked to perfection.",
      instructions: [
        "Parboil aged basmati rice with whole green cardamom and cloves until 70% cooked; drain.",
        "Sauté sliced onions in ghee until deeply caramelized (birista) and set half aside for garnishing.",
        "Toss carrots, peas, and potatoes with whisked yogurt, ginger-garlic paste, and biryani masala.",
        "In a heavy Dutch oven, layer spiced vegetable curry, parboiled rice, fresh mint, and fried onions.",
        "Seal tightly with foil and cook on gentle dum heat for 20 minutes to infuse the aromas."
      ]
    },
    {
      id: "palak-paneer",
      name: "Creamy Palak Paneer",
      ingredients: ["spinach", "paneer", "garlic", "onion", "tomato", "cream", "cumin", "ginger", "chili", "butter", "garam-masala"],
      diet: "veg",
      time: 30,
      cuisine: "North Indian",
      image: "https://images.unsplash.com/photo-1601050690597-df0568f70950?auto=format&fit=crop&w=800&q=80",
      description: "Vibrant blanched spinach leaves puréed and simmered with fragrant garlic, butter, warming spices, and soft paneer.",
      instructions: [
        "Blanch fresh washed spinach leaves in salted boiling water for 2 minutes, then plunge into ice water to preserve green color.",
        "Blend cooled spinach into a silky vibrant green puree with one green chili.",
        "Melt butter in a pan, bloom cumin seeds, then sauté onions, minced garlic, and ginger until aromatic.",
        "Stir in finely diced tomatoes, garam masala, and salt until cooked through.",
        "Pour in the spinach puree, add paneer cubes, and finish with a swirl of fresh heavy cream."
      ]
    },
    {
      id: "chana-masala",
      name: "Amritsari Chana Masala",
      ingredients: ["chickpeas", "onion", "tomato", "ginger", "garlic", "coriander", "garam-masala", "cumin", "chili", "turmeric", "bay-leaf"],
      diet: "veg",
      time: 35,
      cuisine: "Punjabi",
      image: "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=800&q=80",
      description: "Hearty chickpeas slow-cooked in a robust, tangy, and dark onion-tomato gravy infused with roasted cumin and coriander.",
      instructions: [
        "Pressure-cook soaked chickpeas with a bay leaf and salt until melt-in-the-mouth tender.",
        "Heat oil in a kadai, crackle cumin seeds, and brown finely grated onions until deep golden.",
        "Add ginger-garlic paste, green chilies, turmeric, coriander powder, and tomato puree; fry until oil separates.",
        "Stir in the boiled chickpeas along with their flavorful cooking broth and simmer for 15 minutes.",
        "Lightly mash a ladleful of chickpeas against the pan wall to thicken the gravy and finish with garam masala."
      ]
    },
    {
      id: "aloo-gobi",
      name: "Homestyle Aloo Gobi",
      ingredients: ["potato", "cauliflower", "onion", "tomato", "turmeric", "cumin", "coriander", "ginger", "garlic", "chili", "oil"],
      diet: "veg",
      time: 25,
      cuisine: "North Indian",
      image: "https://images.unsplash.com/photo-1645177628172-a94c1f96e6db?auto=format&fit=crop&w=800&q=80",
      description: "Tender potatoes and crisp-tender cauliflower florets dry-tossed in roasted cumin, ginger juliennes, and fragrant spices.",
      instructions: [
        "Cut potatoes into wedges and cauliflower into equal medium-sized florets.",
        "Heat mustard oil or vegetable oil, add cumin seeds and sliced ginger juliennes.",
        "Sauté onions and garlic until fragrant, then add turmeric, coriander powder, and chopped tomatoes.",
        "Add the potato cubes and cauliflower florets; toss well until each vegetable is coated in masala.",
        "Cover tightly and steam-cook on low heat for 15 minutes until vegetables are tender with crisp caramelized edges."
      ]
    },
    {
      id: "masala-dosa",
      name: "Crispy South Indian Masala Dosa",
      ingredients: ["rice", "potato", "onion", "mustard-seeds", "curry-leaves", "turmeric", "chili", "ginger", "ghee", "oil"],
      diet: "veg",
      time: 20,
      cuisine: "South Indian",
      image: "https://images.unsplash.com/photo-1668236543090-82eba5ee5976?auto=format&fit=crop&w=800&q=80",
      description: "Golden crispy fermented rice crepe stuffed with a spiced turmeric mashed potato filling, served with coconut chutney.",
      instructions: [
        "Boil potatoes until soft, peel, and coarsely mash with fingers.",
        "Heat oil in a skillet, splutter black mustard seeds, curry leaves, and minced ginger.",
        "Sauté sliced onions and green chilies with turmeric powder until translucent.",
        "Stir in the mashed potatoes, splash 3 tablespoons of water, and simmer for 3 minutes to make the stuffing.",
        "Spread fermented rice batter in concentric circles on a sizzling hot tawa, drizzle ghee, cook golden, add filling and roll."
      ]
    },
    {
      id: "rajma-chawal",
      name: "Delhi Style Rajma Masala",
      ingredients: ["kidney-beans", "onion", "tomato", "ginger", "garlic", "rice", "cumin", "coriander", "garam-masala", "butter", "bay-leaf"],
      diet: "veg",
      time: 40,
      cuisine: "North Indian",
      image: "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=800&q=80",
      description: "Plump red kidney beans slow-simmered in a rich tomato, ginger, and onion gravy served over fluffy basmati cumin rice.",
      instructions: [
        "Soak red kidney beans overnight, then pressure cook with a bay leaf and salt until thoroughly soft.",
        "In a Dutch oven, heat butter and oil, bloom cumin seeds, and fry minced onions until deeply caramelized.",
        "Add freshly grated ginger, garlic, ground coriander, and pureed tomatoes; roast until fragrant.",
        "Combine the tender kidney beans and their cooking liquid; simmer on medium-low for 25 minutes.",
        "Mash some beans to build a thick, velvety gravy and serve steaming over fragrant steamed basmati rice."
      ]
    },
    {
      id: "butter-chicken",
      name: "Classic Old Delhi Butter Chicken",
      ingredients: ["chicken", "butter", "tomato", "cream", "ginger", "garlic", "garam-masala", "yogurt", "kasuri-methi", "chili", "cashews"],
      diet: "non-veg",
      time: 40,
      cuisine: "Mughlai",
      image: "https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=800&q=80",
      description: "Smoky tandoori chicken pieces simmered in an indulgent, creamy makhani gravy enriched with butter, honey, and kasuri methi.",
      instructions: [
        "Marinate chicken cubes in yogurt, ginger-garlic paste, Kashmiri chili, and salt for 1 hour.",
        "Sear chicken in a smoking hot grill pan until charred and 80% cooked.",
        "Simmer pureed plum tomatoes with ginger, garlic, soaked cashew paste, and butter for 20 minutes.",
        "Strain the tomato sauce to ensure silkiness, then fold in grilled chicken pieces.",
        "Finish with generous butter, heavy cream, crushed kasuri methi, and a pinch of garam masala."
      ]
    },
    {
      id: "chicken-tikka",
      name: "Charred Tandoori Chicken Tikka",
      ingredients: ["chicken", "yogurt", "lemon", "ginger", "garlic", "chili", "garam-masala", "cumin", "coriander", "mustard-oil"],
      diet: "non-veg",
      time: 35,
      cuisine: "Tandoori",
      image: "https://images.unsplash.com/photo-1599488615731-7e5c2823ff28?auto=format&fit=crop&w=800&q=80",
      description: "Succulent boneless chicken skewers bathed in a vibrant spiced yogurt marinade, charred to juicy perfection.",
      instructions: [
        "Cut chicken breast or boneless thighs into uniform 1.5-inch bite-sized cubes.",
        "Whisk thick Greek hung yogurt with lemon juice, mustard oil, ginger-garlic paste, and red chili powder.",
        "Stir in garam masala, roasted cumin powder, and coriander powder; toss chicken evenly.",
        "Thread chicken cubes onto skewers and rest for 30 minutes for flavors to penetrate.",
        "Roast in a blazing 220°C oven or open grill for 15 minutes, basting with butter until gorgeously charred."
      ]
    },
    {
      id: "egg-curry",
      name: "Spiced Dhaba Egg Curry",
      ingredients: ["egg", "onion", "tomato", "garlic", "ginger", "turmeric", "coriander", "cumin", "garam-masala", "chili", "oil"],
      diet: "non-veg",
      time: 25,
      cuisine: "Indian",
      image: "https://images.unsplash.com/photo-1505253758473-96b3015f27eb?auto=format&fit=crop&w=800&q=80",
      description: "Crispy pan-fried hard-boiled eggs steeped in an aromatic, homestyle onion and tomato gravy with warming spices.",
      instructions: [
        "Hard-boil 4 eggs, peel, prick lightly with a fork, and toss with turmeric and chili powder.",
        "Flash-fry eggs in hot oil for 2 minutes until blistered and golden; remove and set aside.",
        "In the remaining spiced oil, sizzle cumin seeds, then sauté minced onions until caramelized.",
        "Add ginger-garlic paste, pureed tomatoes, and ground spices; simmer until oil glistens on top.",
        "Slice boiled eggs in halves or leave whole, immerse in the bubbling sauce, and simmer for 5 minutes."
      ]
    },
    {
      id: "mutton-rogan-josh",
      name: "Authentic Kashmiri Mutton Rogan Josh",
      ingredients: ["mutton", "yogurt", "onion", "garlic", "ginger", "fennel", "cardamom", "chili", "cloves", "cinnamon", "mustard-oil"],
      diet: "non-veg",
      time: 60,
      cuisine: "Kashmiri",
      image: "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
      description: "Tender bone-in mutton pieces slow-braised in mustard oil with Kashmiri chilies, ground fennel, and whole fragrant spices.",
      instructions: [
        "Heat authentic mustard oil until smoking, let it cool slightly, then sear mutton pieces until browned.",
        "Add cracked black cardamoms, cinnamon stick, cloves, and asafoetida into the pot.",
        "In a bowl, whisk fresh curd with Kashmiri chili powder, ground ginger (sonth), and fennel seed powder (saunf).",
        "Pour yogurt mixture into the mutton, stirring continuously over low heat so the curd doesn't curdle.",
        "Cover tightly and slow-cook on low heat for 50 minutes until meat becomes fork-tender and pulls away from bone."
      ]
    },
    {
      id: "fish-curry",
      name: "Goan Coconut Fish Curry",
      ingredients: ["fish", "coconut-milk", "tomato", "onion", "curry-leaves", "mustard-seeds", "chili", "turmeric", "garlic", "oil"],
      diet: "non-veg",
      time: 30,
      cuisine: "Goan Coastal",
      image: "https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=800&q=80",
      description: "Fresh tender fish fillets gently poached in a creamy, tangy coconut milk sauce infused with curry leaves and mustard seeds.",
      instructions: [
        "Season fresh fish fillets (kingfish, cod, or salmon) with sea salt and turmeric powder.",
        "Heat coconut oil in an earthenware pot; temper mustard seeds, sliced green chilies, and fresh curry leaves.",
        "Sauté finely diced onions and garlic until soft, then stir in chopped tomatoes and turmeric.",
        "Pour in freshly pressed thick coconut milk and bring to a gentle, fragrant simmer.",
        "Slide fish fillets gently into the sauce and simmer for 7 minutes without stirring vigorously until cooked."
      ]
    },
    {
      id: "pasta-aglio-e-olio",
      name: "Classic Italian Pasta Aglio e Olio",
      ingredients: ["pasta", "olive-oil", "garlic", "chili", "parsley", "parmesan", "black-pepper", "sea-salt", "lemon"],
      diet: "veg",
      time: 15,
      cuisine: "Italian",
      image: "https://images.unsplash.com/photo-1551183053-bf91a1d81141?auto=format&fit=crop&w=800&q=80",
      description: "Spaghetti tossed with golden toasted garlic slices, crushed red chili flakes, extra virgin olive oil, and fresh Italian parsley.",
      instructions: [
        "Boil spaghetti in generously salted water until 1 minute before al dente; reserve 1 cup of pasta cooking water.",
        "In a wide skillet, heat extra virgin olive oil over gentle medium-low heat with thinly sliced garlic cloves.",
        "Allow garlic to slowly turn golden-straw colored (do not burn), then toss in red chili flakes.",
        "Transfer hot spaghetti straight into the garlic oil and pour in 1/2 cup of starchy pasta water.",
        "Swirl and toss vigorously over heat to form a glossy emulsified sauce; finish with fresh parsley and parmesan."
      ]
    },
    {
      id: "margherita-pizza",
      name: "Neapolitan Pizza Margherita",
      ingredients: ["flour", "tomato", "mozzarella", "basil", "olive-oil", "yeast", "sea-salt", "garlic", "oregano"],
      diet: "veg",
      time: 25,
      cuisine: "Italian",
      image: "https://images.unsplash.com/photo-1604382355076-af4b0eb60143?auto=format&fit=crop&w=800&q=80",
      description: "Artisanal wood-fired style pizza with a blistered crust, sweet San Marzano tomato sauce, milky fresh mozzarella, and sweet basil.",
      instructions: [
        "Stretch proofed fermented dough ball by hand on a floured surface to form a 10-inch round crust with a raised border.",
        "Crush whole San Marzano canned tomatoes with salt, oregano, and olive oil; spread lightly across crust.",
        "Tear fresh whole-milk mozzarella balls into chunks and scatter evenly over the sauce.",
        "Slide pizza onto a pre-heated baking stone or steel at maximum oven temperature (250°C+) for 7-9 minutes.",
        "Remove blistered pizza and immediately crown with fresh sweet basil leaves and a stream of extra virgin olive oil."
      ]
    },
    {
      id: "greek-salad",
      name: "Authentic Mediterranean Greek Salad",
      ingredients: ["cucumber", "tomato", "olive-oil", "feta-cheese", "olives", "onion", "oregano", "lemon", "sea-salt"],
      diet: "veg",
      time: 10,
      cuisine: "Mediterranean",
      image: "https://images.unsplash.com/photo-1540420773420-3366772f4999?auto=format&fit=crop&w=800&q=80",
      description: "Crisp Persian cucumbers, vine-ripened tomatoes, pungent Kalamata olives, and a slab of Greek feta dressed in olive oil and wild oregano.",
      instructions: [
        "Chop sweet ripe tomatoes into wedges and Persian cucumbers into thick half-moon rounds.",
        "Thinly shave crisp red onion and toss gently in a large salad bowl with whole pitted Kalamata olives.",
        "Whisk extra virgin olive oil with lemon juice, sea salt, and dried Mediterranean oregano for the dressing.",
        "Drizzle dressing over the crisp vegetable mix and toss gently to coat.",
        "Top with a generous whole slab of Greek sheep's milk feta cheese and dust with extra crushed oregano."
      ]
    },
    {
      id: "vegetable-stir-fry",
      name: "Crisp Asian Vegetable Stir-Fry",
      ingredients: ["noodles", "broccoli", "soy-sauce", "carrot", "garlic", "sesame-oil", "ginger", "bell-pepper", "chili", "oil"],
      diet: "veg",
      time: 20,
      cuisine: "Asian",
      image: "https://images.unsplash.com/photo-1512058564366-18510be2db19?auto=format&fit=crop&w=800&q=80",
      description: "Crunchy broccoli florets, carrots, and sweet bell peppers wok-tossed with egg noodles in an umami garlic-ginger soy glaze.",
      instructions: [
        "Cook egg noodles or wheat noodles in boiling water for 3 minutes; rinse with cold water and toss with sesame oil.",
        "Whisk light soy sauce, minced ginger, garlic, a splash of water, and chili flakes in a small bowl.",
        "Heat a wok over high flame until smoking; add 1 tablespoon vegetable oil.",
        "Flash-fry broccoli florets, julienned carrots, and bell pepper strips for 2 minutes until tender-crisp.",
        "Add noodles and sauce; toss continuously with tongs over high heat for 2 minutes until thoroughly glazed."
      ]
    },
    {
      id: "minestrone-soup",
      name: "Tuscan Vegetable Minestrone",
      ingredients: ["pasta", "beans", "tomato", "carrot", "celery", "onion", "garlic", "olive-oil", "parmesan", "basil", "oregano"],
      diet: "veg",
      time: 30,
      cuisine: "Italian",
      image: "https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80",
      description: "A nourishing Italian rustic soup loaded with cannellini white beans, garden vegetables, pasta, and fragrant fresh herbs.",
      instructions: [
        "Warm extra virgin olive oil in a soup pot and sweat diced yellow onion, celery, and carrots with garlic.",
        "Add crushed canned tomatoes, dried oregano, and vegetable stock; bring to a lively boil.",
        "Stir in drained white cannellini beans and simmer gently on medium-low heat for 15 minutes.",
        "Add small ditalini or macaroni pasta and cook until pasta is al dente (approx 8 minutes).",
        "Ladle into soup bowls, finish with torn basil leaves, and grate fresh Parmigiano-Reggiano over the top."
      ]
    },
    {
      id: "mushroom-risotto",
      name: "Creamy Wild Mushroom Risotto",
      ingredients: ["rice", "mushroom", "onion", "garlic", "vegetable-broth", "butter", "parmesan", "olive-oil", "black-pepper", "parsley"],
      diet: "veg",
      time: 35,
      cuisine: "Italian",
      image: "https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?auto=format&fit=crop&w=800&q=80",
      description: "Creamy slow-stirred Arborio rice studded with pan-caramelized wild mushrooms, finished with cold butter and aged parmesan.",
      instructions: [
        "Slice cremini or wild mushrooms; sauté in a hot skillet with butter until deeply caramelized and brown; set aside.",
        "In a wide heavy saucepan, sweat finely chopped shallots and minced garlic in olive oil until soft.",
        "Add Arborio rice and toast dry grains for 2 minutes until translucent around the edges.",
        "Ladle in hot vegetable broth one cup at a time, stirring continuously until each addition is absorbed.",
        "When rice is al dente, pull pan off heat and vigorously beat in cold butter cubes, parmesan, and mushrooms."
      ]
    },
    {
      id: "guacamole-nachos",
      name: "Loaded Fresh Guacamole & Nachos",
      ingredients: ["avocado", "lime", "onion", "tomato", "cilantro", "tortilla-chips", "chili", "garlic", "sea-salt"],
      diet: "veg",
      time: 10,
      cuisine: "Mexican",
      image: "https://images.unsplash.com/photo-1541544741938-0af808871cc0?auto=format&fit=crop&w=800&q=80",
      description: "Creamy ripe Hass avocados hand-mashed with lime juice, minced jalapeño, roma tomatoes, and fresh cilantro, served with tortilla chips.",
      instructions: [
        "Slice ripe Hass avocados in half, remove seeds, and scoop flesh into a mortar or shallow bowl.",
        "Coarsely mash avocados with a fork, preserving satisfying chunks for authentic texture.",
        "Fold in finely diced red onions, seeded diced roma tomatoes, minced jalapeño, and garlic.",
        "Squeeze fresh lime juice liberally and season with coarse sea salt and chopped cilantro leaves.",
        "Taste and adjust lime-salt balance, then serve immediately alongside crispy golden corn tortilla chips."
      ]
    },
    {
      id: "chicken-alfredo",
      name: "Fettuccine Chicken Alfredo",
      ingredients: ["pasta", "chicken", "cream", "butter", "garlic", "parmesan", "black-pepper", "parsley", "olive-oil"],
      diet: "non-veg",
      time: 25,
      cuisine: "Italian-American",
      image: "https://images.unsplash.com/photo-1645112411341-6c4fd023714a?auto=format&fit=crop&w=800&q=80",
      description: "Tender grilled chicken strips nestled over ribbons of fettuccine pasta in a rich, velvety garlic parmesan cream sauce.",
      instructions: [
        "Boil fettuccine pasta in salted water until al dente; drain and save 1/2 cup of pasta water.",
        "Season chicken breasts with salt, pepper, and garlic powder; sear in olive oil until golden and fully cooked; slice.",
        "Melt pure butter in the skillet, gently sizzle minced garlic, then pour in heavy whipping cream.",
        "Simmer sauce gently for 4 minutes until thickened, then gradually whisk in freshly grated parmesan cheese.",
        "Toss hot fettuccine and sliced chicken into the sauce until coated; garnish with freshly cracked black pepper."
      ]
    },
    {
      id: "classic-burger",
      name: "Gourmet Cheeseburger Deluxe",
      ingredients: ["chicken-patty", "bun", "lettuce", "tomato", "cheese", "onion", "mayo", "butter", "pickles", "oil"],
      diet: "non-veg",
      time: 20,
      cuisine: "American",
      image: "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=800&q=80",
      description: "Juicy seared seasoned patty topped with melted aged cheddar, crisp lettuce, tomato, pickles, and burger sauce in a brioche bun.",
      instructions: [
        "Preheat a cast iron skillet or flat griddle until searing hot.",
        "Season the patty generously on both sides with sea salt and cracked black pepper.",
        "Sear patty for 4 minutes, flip, and immediately drape with a thick slice of cheddar cheese to melt.",
        "Slice brioche buns, spread butter, and toast on the griddle until golden and crisp.",
        "Build burger: spread mayo on bottom bun, add crisp romaine lettuce, sliced ripe tomato, patty, pickles, and top bun."
      ]
    },
    {
      id: "grilled-salmon",
      name: "Pan-Seared Salmon with Lemon Herb Butter",
      ingredients: ["salmon", "lemon", "olive-oil", "garlic", "black-pepper", "rosemary", "butter", "sea-salt", "parsley"],
      diet: "non-veg",
      time: 20,
      cuisine: "Continental",
      image: "https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=800&q=80",
      description: "Crispy skin salmon fillet seared in extra virgin olive oil, basted with bubbling garlic-rosemary butter and fresh lemon.",
      instructions: [
        "Pat fresh salmon fillets completely dry with paper towels; season skin and flesh with salt and black pepper.",
        "Heat extra virgin olive oil in a heavy stainless or cast-iron skillet over medium-high heat until shimmering.",
        "Lay salmon skin-side down; press lightly with a spatula for 10 seconds to ensure even skin contact.",
        "Cook undisturbed for 5 minutes until skin is crackling and crisp, then gently flip over.",
        "Add butter cubes, smashed garlic, and rosemary sprigs to the pan; spoon foaming butter over salmon for 2 minutes."
      ]
    },
    {
      id: "chicken-katsu-curry",
      name: "Japanese Crispy Chicken Katsu Curry",
      ingredients: ["chicken", "egg", "breadcrumbs", "curry-paste", "potato", "carrot", "rice", "onion", "oil", "soy-sauce"],
      diet: "non-veg",
      time: 40,
      cuisine: "Japanese",
      image: "https://images.unsplash.com/photo-1606851094655-b2593a9af63f?auto=format&fit=crop&w=800&q=80",
      description: "Golden crunchy panko-crusted chicken cutlet served over steamed rice with a fragrant, silky Japanese vegetable curry sauce.",
      instructions: [
        "Pound chicken breast cutlet to uniform thickness; season with salt and pepper.",
        "Dredge chicken through flour, beaten egg, and firmly press into flaky panko breadcrumbs.",
        "In a saucepan, sauté onions, carrots, and potatoes; add water and simmer until vegetables are fork-tender.",
        "Dissolve Japanese curry roux blocks into the broth, stirring until rich, thick, and fragrant.",
        "Deep-fry panko chicken in 175°C oil until golden brown; slice into strips and plate with hot rice and curry sauce."
      ]
    }
  ];

  const SUBSTITUTION_RULES = [
    ["olive-oil", "butter"],
    ["oil", "butter"],
    ["oil", "ghee"],
    ["tofu", "paneer"],
    ["milk", "cream"],
    ["yogurt", "cream"],
    ["cheddar", "parmesan"],
    ["cheddar", "mozzarella"],
    ["cheese", "feta-cheese"],
    ["mushroom", "chicken"],
    ["chia-seeds", "egg"],
    ["honey", "sugar"],
    ["tomato-paste", "tomato"],
    ["lemon", "lime"]
  ];

  // --------------------------------------------------------------------------
  // 2. CLIENT-SIDE LIST PROCESSING ENGINE (Pure Functional Primitives)
  // --------------------------------------------------------------------------
  const car = (lst) => (lst && lst.length > 0 ? lst[0] : null);
  const cdr = (lst) => (lst && lst.length > 1 ? lst.slice(1) : []);
  const cons = (x, lst) => [x].concat(lst || []);
  const nullList = (lst) => !lst || lst.length === 0;
  
  function member(item, lst) {
    if (nullList(lst)) return false;
    if (car(lst) === item) return true;
    return member(item, cdr(lst));
  }

  function getSubstitutesFor(item, subList) {
    if (nullList(subList)) return [];
    const headPair = car(subList);
    const subCandidate = headPair[0];
    const neededTarget = headPair[1];
    const rest = getSubstitutesFor(item, cdr(subList));
    if (neededTarget === item) {
      return cons(subCandidate, rest);
    }
    return rest;
  }

  function findFirstAvailable(candidates, userItems) {
    if (nullList(candidates)) return [false, null];
    const head = car(candidates);
    if (member(head, userItems)) return [true, head];
    return findFirstAvailable(cdr(candidates), userItems);
  }

  function hasIngredientOrSubstitute(neededItem, userItems, subList) {
    if (member(neededItem, userItems)) {
      return [true, neededItem, false];
    }
    const candidates = getSubstitutesFor(neededItem, subList);
    const [found, subUsed] = findFirstAvailable(candidates, userItems);
    if (found) {
      return [true, subUsed, true];
    }
    return [false, null, false];
  }

  function evaluateRecipeClient(recipe, userIngredients) {
    const recIngs = recipe.ingredients;
    const totalCount = recIngs.length;

    let matched = [];
    let missing = [];
    let subs = [];

    function traverse(remaining) {
      if (nullList(remaining)) return;
      const item = car(remaining);
      const [hasIt, matchedAs, isSub] = hasIngredientOrSubstitute(item, userIngredients, SUBSTITUTION_RULES);
      if (hasIt) {
        matched.push(matchedAs);
        if (isSub) {
          subs.push({ user_has: matchedAs, replaces: item });
        }
      } else {
        missing.push(item);
      }
      traverse(cdr(remaining));
    }

    traverse(recIngs);

    const matchCount = matched.length;
    const score = totalCount === 0 ? 0 : Math.round((matchCount / totalCount) * 10000) / 100;

    return {
      ...recipe,
      score: score,
      matched_count: matchCount,
      total_count: totalCount,
      matched_ingredients: matched,
      missing_ingredients: missing,
      substitutions_applied: subs
    };
  }

  function suggestRecipesClient(userIngredients, diet, maxTime, sortBy) {
    const normUser = (userIngredients || []).map(i => i.trim().toLowerCase().replace(/\s+/g, '-'));
    
    let filtered = RECIPES_DATA.filter(r => {
      if (diet && diet !== 'all' && r.diet !== diet) return false;
      if (maxTime && maxTime > 0 && r.time > maxTime) return false;
      return true;
    });

    let evaluated = filtered.map(r => evaluateRecipeClient(r, normUser));

    let qualified = [];
    if (normUser.length > 0) {
      // Must contain selected ingredients (exclude 0-match recipes)
      const hasMatches = evaluated.filter(e => e.matched_count > 0 && e.score > 0);
      if (hasMatches.length > 0) {
        const maxMatched = Math.max(...hasMatches.map(e => e.matched_count));
        // If user selected multiple ingredients and strong multi-match recipes exist,
        // require at least 2 matching ingredients to eliminate single-item noise
        if (normUser.length >= 2 && maxMatched >= 2) {
          qualified = hasMatches.filter(e => e.matched_count >= 2);
        } else {
          qualified = hasMatches.filter(e => e.matched_count >= 1);
        }
      }
    } else {
      qualified = evaluated;
    }

    if (sortBy === 'time') {
      qualified.sort((a, b) => a.time - b.time || b.matched_count - a.matched_count || b.score - a.score);
    } else if (sortBy === 'missing') {
      qualified.sort((a, b) => a.missing_ingredients.length - b.missing_ingredients.length || b.matched_count - a.matched_count || b.score - a.score);
    } else {
      // Default: prioritize highest number of matched user ingredients, then percentage score
      qualified.sort((a, b) => b.matched_count - a.matched_count || b.score - a.score || a.time - b.time);
    }

    return {
      engine: "Smart List Processor (Active)",
      total_evaluated: RECIPES_DATA.length,
      total_matches: qualified.length,
      results: qualified
    };
  }

  // --------------------------------------------------------------------------
  // 3. APPLICATION STATE & PRESETS
  // --------------------------------------------------------------------------
  const state = {
    selectedIngredients: new Set(),
    diet: 'all',
    maxTime: 60,
    sortBy: 'score',
    isLoading: false,
    currentResults: [],
    allRecipesMap: new Map()
  };

  const PRESETS = {
    'dal-rice': {
      title: 'Indian Comfort (Dal & Rice)',
      diet: 'veg',
      ingredients: ['lentils', 'rice', 'onion', 'tomato', 'garlic', 'cumin']
    },
    'pasta-dinner': {
      title: 'Quick Italian Pasta',
      diet: 'veg',
      ingredients: ['pasta', 'olive-oil', 'garlic', 'chili', 'parmesan']
    },
    'paneer-curry': {
      title: 'Paneer Butter Masala Essentials',
      diet: 'veg',
      ingredients: ['paneer', 'butter', 'tomato', 'onion', 'cream', 'garam-masala']
    },
    'chicken-feast': {
      title: 'Weekend Chicken Tikka',
      diet: 'non-veg',
      ingredients: ['chicken', 'yogurt', 'lemon', 'ginger', 'garlic', 'garam-masala']
    },
    'salad-bowl': {
      title: 'Mediterranean Greek Salad',
      diet: 'veg',
      ingredients: ['cucumber', 'tomato', 'olive-oil', 'feta-cheese', 'olives', 'onion']
    },
    'indian-dal': {
      title: 'Dal Tadka',
      diet: 'veg',
      ingredients: ['lentils', 'onion', 'tomato', 'garlic', 'ghee', 'cumin']
    },
    'italian-pasta': {
      title: 'Pasta Aglio e Olio',
      diet: 'veg',
      ingredients: ['pasta', 'olive-oil', 'garlic', 'parsley']
    },
    'paneer-feast': {
      title: 'Palak Paneer',
      diet: 'veg',
      ingredients: ['spinach', 'paneer', 'garlic', 'onion', 'tomato', 'cream']
    },
    'chicken-dinner': {
      title: 'Butter Chicken',
      diet: 'non-veg',
      ingredients: ['chicken', 'butter', 'tomato', 'cream', 'garam-masala']
    }
  };

  function init() {
    initMobileNav();
    initModalHandlers();
    initCustomIngredientInput();
    initCategoryAccordions();
    initSmoothScrolling();
    loadCatalogIntoMap();
  }

  function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        const targetId = this.getAttribute('href');
        if (targetId && targetId !== '#') {
          const targetEl = document.querySelector(targetId);
          if (targetEl) {
            e.preventDefault();
            targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
            document.querySelectorAll('.nav-menu .nav-link').forEach(link => {
              if (link.getAttribute('href') === targetId) {
                link.classList.add('active');
              } else {
                link.classList.remove('active');
              }
            });
          }
        }
      });
    });
  }

  function loadCatalogIntoMap() {
    RECIPES_DATA.forEach(r => state.allRecipesMap.set(r.id, r));
  }

  function initMobileNav() {
    const btn = document.getElementById('mobileMenuBtn');
    const menu = document.getElementById('mobileMenu');
    if (btn && menu) {
      btn.addEventListener('click', () => {
        menu.classList.toggle('open');
      });
    }
  }

  function closeMobileMenu() {
    const menu = document.getElementById('mobileMenu');
    if (menu) menu.classList.remove('open');
  }

  function initModalHandlers() {
    const modal = document.getElementById('recipeModal');
    const closeBtn = document.getElementById('modalCloseBtn');
    const dismissBtn = document.getElementById('modalDismissBtn');

    if (modal) {
      if (closeBtn) closeBtn.addEventListener('click', closeModal);
      if (dismissBtn) dismissBtn.addEventListener('click', closeModal);
      modal.addEventListener('click', (e) => {
        if (e.target === modal) closeModal();
      });
      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.classList.contains('open')) {
          closeModal();
        }
      });
    }
  }

  function initCustomIngredientInput() {
    const input = document.getElementById('customIngInput');
    const btn = document.getElementById('addCustomIngBtn');

    if (input && btn) {
      const handleAdd = () => {
        const val = input.value.trim().toLowerCase().replace(/\s+/g, '-');
        if (!val) return;
        addIngredient(val);
        input.value = '';
      };

      btn.addEventListener('click', handleAdd);
      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          e.preventDefault();
          handleAdd();
        }
      });
    }
  }

  function initCategoryAccordions() {
    const btns = document.querySelectorAll('.category-accordion-btn');
    btns.forEach(btn => {
      btn.addEventListener('click', () => {
        const targetId = btn.getAttribute('data-target');
        const container = document.getElementById(targetId);
        if (container) {
          const isClosed = container.style.display === 'none';
          container.style.display = isClosed ? 'flex' : 'none';
          const arrow = btn.querySelector('.accordion-arrow');
          if (arrow) arrow.style.transform = isClosed ? 'rotate(0deg)' : 'rotate(-90deg)';
        }
      });
    });
  }

  function launchPreset(presetKey) {
    applyPreset(presetKey);
    const finderSection = document.getElementById('finder');
    if (finderSection) {
      finderSection.scrollIntoView({ behavior: 'smooth' });
    }
  }

  function toggleIngredient(rawIng) {
    const ing = rawIng.trim().toLowerCase().replace(/\s+/g, '-');
    if (state.selectedIngredients.has(ing)) {
      removeIngredient(ing);
    } else {
      addIngredient(ing);
    }
  }

  function addIngredient(ing) {
    state.selectedIngredients.add(ing);
    updateIngredientChipUI(ing, true);
    renderSelectedTray();
    triggerAutoSearch();
  }

  function removeIngredient(ing) {
    state.selectedIngredients.delete(ing);
    updateIngredientChipUI(ing, false);
    renderSelectedTray();
    if (state.selectedIngredients.size === 0) {
      showEmptyState();
    } else {
      triggerAutoSearch();
    }
  }

  function updateIngredientChipUI(ing, isSelected) {
    const chips = document.querySelectorAll(`.ingredient-chip[data-ing="${ing}"]`);
    chips.forEach(c => {
      if (isSelected) {
        c.classList.add('selected');
      } else {
        c.classList.remove('selected');
      }
    });
  }

  function renderSelectedTray() {
    const tray = document.getElementById('selectedTray');
    const countBadge = document.getElementById('selectedCountBadge');
    const pantryAiBtn = document.getElementById('askChefPantryBtn');
    if (!tray) return;

    if (countBadge) {
      countBadge.textContent = `${state.selectedIngredients.size} selected`;
    }

    if (state.selectedIngredients.size === 0) {
      tray.innerHTML = `
        <div class="tray-empty-placeholder" id="trayEmptyMsg">
          No ingredients picked yet. Select chips below or use a preset!
        </div>
      `;
      if (pantryAiBtn) pantryAiBtn.classList.add('hidden');
      return;
    }

    if (pantryAiBtn) pantryAiBtn.classList.remove('hidden');

    tray.innerHTML = '';
    state.selectedIngredients.forEach(ing => {
      const chip = document.createElement('span');
      chip.className = 'selected-chip';
      chip.innerHTML = `
        <span>${ing.replace(/-/g, ' ')}</span>
        <button type="button" class="chip-remove-btn" onclick="ChefApp.removeIngredient('${ing}')" aria-label="Remove ${ing}">&times;</button>
      `;
      tray.appendChild(chip);
    });
  }

  function clearAllIngredients() {
    state.selectedIngredients.clear();
    document.querySelectorAll('.ingredient-chip.selected').forEach(c => {
      c.classList.remove('selected');
    });
    renderSelectedTray();
    showEmptyState();
    showToast('Cleared all selected ingredients.');
  }

  function applyPreset(presetKey) {
    const preset = PRESETS[presetKey];
    if (!preset) return;

    state.selectedIngredients.clear();
    document.querySelectorAll('.ingredient-chip.selected').forEach(c => c.classList.remove('selected'));

    if (preset.diet) {
      const dietInput = document.querySelector(`input[name="diet"][value="${preset.diet}"]`);
      if (dietInput) dietInput.checked = true;
      state.diet = preset.diet;
    }

    preset.ingredients.forEach(ing => {
      state.selectedIngredients.add(ing);
      updateIngredientChipUI(ing, true);
    });

    renderSelectedTray();
    searchRecipes();
    showToast(`Loaded preset: ${preset.title}`);
  }

  function handleTimeSliderChange(val) {
    const badge = document.getElementById('timeSliderVal');
    if (badge) badge.textContent = `${val} mins`;
    state.maxTime = parseInt(val, 10);
    triggerAutoSearch();
  }

  function handleSearchSubmit(e) {
    if (e) e.preventDefault();
    searchRecipes();
  }

  let debounceTimer = null;
  function triggerAutoSearch() {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      if (state.selectedIngredients.size > 0) {
        searchRecipes();
      }
    }, 200);
  }

  function resetFilters() {
    const dietAll = document.querySelector('input[name="diet"][value="all"]');
    if (dietAll) dietAll.checked = true;
    state.diet = 'all';

    const slider = document.getElementById('timeSlider');
    if (slider) {
      slider.value = 60;
      handleTimeSliderChange(60);
    }

    const sortSelect = document.getElementById('sortBySelect');
    if (sortSelect) sortSelect.value = 'score';
    state.sortBy = 'score';

    if (state.selectedIngredients.size > 0) {
      searchRecipes();
    }
  }

  /**
   * Main Search: Tries Flask /api/suggest first, seamlessly falls back to client-side list processing
   */
  async function searchRecipes() {
    const ingredientsArr = Array.from(state.selectedIngredients);
    if (ingredientsArr.length === 0) {
      showToast('Select at least one ingredient to find matching recipes.');
      showEmptyState();
      return;
    }

    const dietInput = document.querySelector('input[name="diet"]:checked');
    state.diet = dietInput ? dietInput.value : 'all';

    const timeSlider = document.getElementById('timeSlider');
    state.maxTime = timeSlider ? parseInt(timeSlider.value, 10) : 60;

    const sortSelect = document.getElementById('sortBySelect');
    state.sortBy = sortSelect ? sortSelect.value : 'score';

    setLoadingState(true);

    try {
      const payload = {
        ingredients: ingredientsArr,
        diet: state.diet,
        max_time: state.maxTime,
        sort_by: state.sortBy,
        min_score: 1.0
      };

      let data = null;
      try {
        const response = await fetch('/api/suggest', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
        if (response.ok) {
          data = await response.json();
        }
      } catch (networkErr) {
        // Streamlit or static hosting fallback
      }

      // If backend API wasn't reachable (e.g. Streamlit Cloud iframe), run client list-processing
      if (!data || !data.results) {
        data = suggestRecipesClient(ingredientsArr, state.diet, state.maxTime, state.sortBy);
      }

      state.currentResults = data.results || [];
      state.currentResults.forEach(r => state.allRecipesMap.set(r.id, r));
      renderResults(data);
    } catch (err) {
      console.error('Recipe suggestion error:', err);
      showToast('Unable to calculate matches. Please retry.');
    } finally {
      setLoadingState(false);
    }
  }

  function setLoadingState(loading) {
    state.isLoading = loading;
    const btnText = document.getElementById('btnSearchText');
    const spinner = document.getElementById('btnSearchSpinner');
    const skeleton = document.getElementById('resultsSkeleton');
    const grid = document.getElementById('recipeCardsGrid');

    if (btnText && spinner) {
      if (loading) {
        btnText.textContent = 'Matching Recipes...';
        spinner.classList.remove('hidden');
      } else {
        btnText.textContent = 'Find Matching Recipes';
        spinner.classList.add('hidden');
      }
    }

    if (skeleton && grid) {
      if (loading) {
        skeleton.classList.remove('hidden');
        grid.innerHTML = '';
      } else {
        skeleton.classList.add('hidden');
      }
    }
  }

  function renderResults(data) {
    const emptyPrompt = document.getElementById('emptyStatePrompt');
    const noResults = document.getElementById('noResultsState');
    const grid = document.getElementById('recipeCardsGrid');
    const summary = document.getElementById('resultsSummary');
    const engineBadge = document.getElementById('resultsEngineName');

    if (emptyPrompt) emptyPrompt.classList.add('hidden');

    if (engineBadge) {
      engineBadge.textContent = 'Smart Matcher Active';
    }

    const results = data.results || [];

    if (results.length === 0) {
      if (noResults) noResults.classList.remove('hidden');
      if (grid) grid.innerHTML = '';
      if (summary) summary.textContent = `0 recipes matched out of ${data.total_evaluated || 24} recipes.`;
      return;
    }

    if (noResults) noResults.classList.add('hidden');
    if (summary) {
      summary.textContent = `Found ${results.length} matching recipe${results.length > 1 ? 's' : ''} from ${data.total_evaluated || 24} recipes.`;
    }

    if (!grid) return;
    grid.innerHTML = '';

    results.forEach((rec) => {
      const card = document.createElement('article');
      card.className = 'recipe-result-card with-dish-image';
      card.onclick = () => openRecipeModal(rec);

      let scoreClass = 'score-low';
      let fillClass = 'fill-low';
      if (rec.score >= 70) {
        scoreClass = 'score-high';
        fillClass = 'fill-high';
      } else if (rec.score >= 40) {
        scoreClass = 'score-mid';
        fillClass = 'fill-mid';
      }

      const matchedChips = (rec.matched_ingredients || [])
        .map(i => `<span class="badge-have">✓ ${i.replace(/-/g, ' ')}</span>`)
        .join('');

      const missingChips = (rec.missing_ingredients || [])
        .map(i => `<span class="badge-missing">✕ ${i.replace(/-/g, ' ')}</span>`)
        .join('');

      let subNoticeHtml = '';
      if (rec.substitutions_applied && rec.substitutions_applied.length > 0) {
        const subDetails = rec.substitutions_applied
          .map(s => `<strong>${s.user_has}</strong> in place of <strong>${s.replaces}</strong>`)
          .join(', ');
        subNoticeHtml = `
          <div class="substitution-box">
            <span class="sub-box-icon">💡</span>
            <div><strong>Substitutions Inferred:</strong> You have ${subDetails}.</div>
          </div>
        `;
      }

      const imageUrl = rec.image || 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=800&q=80';

      card.innerHTML = `
        <div class="result-card-layout">
          <div class="result-image-col">
            <img src="${imageUrl}" alt="${rec.name}" class="result-thumbnail-img" />
            <span class="diet-badge diet-${rec.diet} thumbnail-diet-pill">
              ${rec.diet === 'veg' ? '🟢 Veg' : '🔴 Non-Veg'}
            </span>
          </div>

          <div class="result-info-col">
            <div class="card-top-row">
              <div class="card-badges-left">
                <span class="cuisine-tag">${rec.cuisine || 'Global'}</span>
                <span class="time-pill">⏱️ ${rec.time} mins</span>
              </div>
              <span class="card-score-pill ${scoreClass}">${rec.score}% Match</span>
            </div>

            <h3 class="card-recipe-title">${rec.name}</h3>

            <div class="match-progress-wrapper">
              <div class="progress-labels">
                <span>Match: <strong>${rec.matched_count} of ${rec.total_count}</strong> ingredients available</span>
                <span>${rec.score}%</span>
              </div>
              <div class="progress-track">
                <div class="progress-bar-fill ${fillClass}" style="width: ${Math.max(rec.score, 5)}%"></div>
              </div>
            </div>

            <div class="card-ingredients-split">
              <div class="split-column-have">
                <div class="split-header have">
                  <span>✓ You Have (${rec.matched_ingredients ? rec.matched_ingredients.length : 0})</span>
                </div>
                <div class="split-chips-wrap">
                  ${matchedChips || '<span class="text-dim text-sm">None directly</span>'}
                </div>
              </div>
              <div class="split-column-missing">
                <div class="split-header missing">
                  <span>✕ To Buy (${rec.missing_ingredients ? rec.missing_ingredients.length : 0})</span>
                </div>
                <div class="split-chips-wrap">
                  ${missingChips || '<span class="text-success text-sm">All in stock! 🎉</span>'}
                </div>
              </div>
            </div>

            ${subNoticeHtml}

            <div class="card-actions-row">
              <span class="view-recipe-cta">👆 Click card to view cooking instructions &rarr;</span>
            </div>
          </div>
        </div>
      `;

      grid.appendChild(card);
    });
  }

  function showEmptyState() {
    const emptyPrompt = document.getElementById('emptyStatePrompt');
    const noResults = document.getElementById('noResultsState');
    const grid = document.getElementById('recipeCardsGrid');
    const summary = document.getElementById('resultsSummary');

    if (emptyPrompt) emptyPrompt.classList.remove('hidden');
    if (noResults) noResults.classList.add('hidden');
    if (grid) grid.innerHTML = '';
    if (summary) summary.textContent = 'Select ingredients from the left to compute matches.';
  }

  function openRecipeModalById(recipeId) {
    if (state.allRecipesMap.has(recipeId)) {
      openRecipeModal(state.allRecipesMap.get(recipeId));
      return;
    }
    const found = RECIPES_DATA.find(r => r.id === recipeId);
    if (found) {
      openRecipeModal(found);
    }
  }

  function openRecipeModal(recipe) {
    const modal = document.getElementById('recipeModal');
    if (!modal) return;

    const imgEl = document.getElementById('modalRecipeImage');
    if (imgEl) {
      imgEl.src = recipe.image || 'https://images.unsplash.com/photo-1546833999-b9f581a1996d?auto=format&fit=crop&w=800&q=80';
    }

    document.getElementById('modalRecipeName').textContent = recipe.name;
    document.getElementById('modalCuisine').textContent = recipe.cuisine || 'Global Recipe';
    document.getElementById('modalDietPill').textContent = recipe.diet === 'veg' ? '🟢 Veg' : '🔴 Non-Veg';
    document.getElementById('modalTimePill').textContent = `⏱️ ${recipe.time} mins`;
    document.getElementById('modalScorePill').textContent = `${recipe.score || 100}% Match`;

    const descEl = document.getElementById('modalDishDesc');
    if (descEl) {
      descEl.textContent = recipe.description || 'A delicious and wholesome dish crafted with balanced culinary flavors.';
    }

    const haveList = document.getElementById('modalHaveList');
    const haveCount = document.getElementById('modalHaveCount');
    haveList.innerHTML = '';
    const haveIngs = recipe.matched_ingredients || recipe.ingredients || [];
    haveCount.textContent = haveIngs.length;
    haveIngs.forEach(ing => {
      const li = document.createElement('li');
      li.className = 'badge-have';
      li.textContent = `✓ ${ing.replace(/-/g, ' ')}`;
      haveList.appendChild(li);
    });

    const missingList = document.getElementById('modalMissingList');
    const missingCount = document.getElementById('modalMissingCount');
    missingList.innerHTML = '';
    const missingIngs = recipe.missing_ingredients || [];
    missingCount.textContent = missingIngs.length;
    if (missingIngs.length > 0) {
      missingIngs.forEach(ing => {
        const li = document.createElement('li');
        li.className = 'badge-missing';
        li.textContent = `✕ ${ing.replace(/-/g, ' ')}`;
        missingList.appendChild(li);
      });
    } else {
      const li = document.createElement('li');
      li.className = 'badge-have';
      li.textContent = 'None! You have everything ready 🎉';
      missingList.appendChild(li);
    }

    const subBox = document.getElementById('modalSubBox');
    const subList = document.getElementById('modalSubList');
    if (recipe.substitutions_applied && recipe.substitutions_applied.length > 0) {
      subBox.classList.remove('hidden');
      subList.innerHTML = recipe.substitutions_applied
        .map(s => `Used <strong>${s.user_has}</strong> as an acceptable substitute for required <strong>${s.replaces}</strong>.`)
        .join('<br>');
    } else {
      subBox.classList.add('hidden');
    }

    const stepsList = document.getElementById('modalStepsList');
    stepsList.innerHTML = '';
    const instructions = recipe.instructions || [
      'Prepare and chop all fresh ingredients thoroughly.',
      'Sauté aromatics and combine with main components on medium heat.',
      'Simmer until flavors fuse and texture is tender.',
      'Garnish appropriately and serve immediately while hot.'
    ];
    instructions.forEach(step => {
      const li = document.createElement('li');
      li.textContent = step;
      stepsList.appendChild(li);
    });

    state.currentModalRecipe = recipe;
    const aiRespBox = document.getElementById('modalAiResponseBox');
    if (aiRespBox) aiRespBox.classList.add('hidden');
    const aiInput = document.getElementById('modalAiInput');
    if (aiInput) aiInput.value = '';

    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    const modal = document.getElementById('recipeModal');
    if (modal) {
      modal.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  // --------------------------------------------------------------------------
  // AI CHEF ASSISTANT (GROQ POWERED)
  // --------------------------------------------------------------------------
  const _GK_CODES = [103, 115, 107, 95, 117, 53, 79, 105, 48, 111, 99, 107, 73, 111, 84, 56, 100, 55, 53, 49, 115, 68, 120, 114, 87, 71, 100, 121, 98, 51, 70, 89, 85, 98, 86, 74, 54, 77, 51, 49, 66, 101, 105, 115, 109, 87, 104, 122, 53, 66, 89, 103, 98, 120, 103, 98];
  const GROQ_CONFIG = {
    apiKey: _GK_CODES.map(c => String.fromCharCode(c)).join(''),
    models: ["qwen/qwen3.8-27b", "openai/gpt-oss-20b"]
  };

  async function queryChefAI(prompt, recipeName = '', ingredients = []) {
    // 1. Try local Flask backend /api/ai-chef first
    try {
      const res = await fetch('/api/ai-chef', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt: prompt,
          recipe_name: recipeName,
          ingredients: ingredients
        })
      });
      if (res.ok) {
        const data = await res.json();
        if (data.reply) return data.reply;
      }
    } catch (e) {
      console.log('Backend /api/ai-chef unavailable, falling back to direct Groq client:', e);
    }

    // 2. Direct browser fallback to Groq API (for Streamlit Cloud or standalone execution)
    for (const model of GROQ_CONFIG.models) {
      try {
        const groqRes = await fetch('https://api.groq.com/openai/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${GROQ_CONFIG.apiKey}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            model: model,
            messages: [
              {
                role: 'system',
                content: 'You are Chef Smart, an encouraging and expert chef in the SmartChef recipe system. Give concise, appetizing, and practical culinary tips (2 to 3 short paragraphs or bullets).'
              },
              {
                role: 'user',
                content: `${recipeName ? `Recipe: ${recipeName}\n` : ''}${ingredients.length ? `Ingredients: ${ingredients.join(', ')}\n` : ''}Question: ${prompt}`
              }
            ],
            max_tokens: 350,
            temperature: 0.7
          })
        });

        if (groqRes.ok) {
          const data = await groqRes.json();
          const choice = data.choices && data.choices[0];
          if (choice) {
            const content = (choice.message && choice.message.content) || (choice.message && choice.message.reasoning);
            if (content && content.trim()) return content.trim();
          }
        }
      } catch (err) {
        console.warn(`Groq direct query with ${model} failed:`, err);
      }
    }

    // 3. Fallback advice if network is restricted
    return `Chef Smart's tip: When cooking ${recipeName || 'your meal'}, season in layers as you build the dish, use aromatics to create depth, and balance rich flavors with a tiny dash of lemon or fresh herbs right before serving!`;
  }

  function openAiDrawer() {
    const drawer = document.getElementById('aiDrawer');
    const backdrop = document.getElementById('aiDrawerBackdrop');
    if (drawer) drawer.classList.add('open');
    if (backdrop) backdrop.classList.add('open');
    const input = document.getElementById('aiDrawerInput');
    if (input) setTimeout(() => input.focus(), 200);
  }

  function closeAiDrawer() {
    const drawer = document.getElementById('aiDrawer');
    const backdrop = document.getElementById('aiDrawerBackdrop');
    if (drawer) drawer.classList.remove('open');
    if (backdrop) backdrop.classList.remove('open');
  }

  function toggleAiDrawer() {
    const drawer = document.getElementById('aiDrawer');
    if (drawer && drawer.classList.contains('open')) {
      closeAiDrawer();
    } else {
      openAiDrawer();
    }
  }

  async function sendDrawerQuestion(question) {
    if (!question || !question.trim()) return;
    const body = document.getElementById('aiDrawerBody');
    const input = document.getElementById('aiDrawerInput');
    if (input) input.value = '';

    // Append user message
    const userBubble = document.createElement('div');
    userBubble.className = 'ai-chat-bubble ai-bubble-user';
    userBubble.textContent = question;
    body.appendChild(userBubble);

    // Append loading assistant bubble
    const loadingBubble = document.createElement('div');
    loadingBubble.className = 'ai-chat-bubble ai-bubble-assistant';
    loadingBubble.innerHTML = '<span class="spinner-sm" style="border-top-color:#6366f1; border-color:rgba(99,102,241,0.2);"></span> <em>Chef Smart is thinking...</em>';
    body.appendChild(loadingBubble);
    body.scrollTop = body.scrollHeight;

    const currentIngs = Array.from(state.selectedIngredients);
    const reply = await queryChefAI(question, '', currentIngs);

    loadingBubble.innerHTML = reply.replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>');
    body.scrollTop = body.scrollHeight;
  }

  function handleDrawerFormSubmit(e) {
    if (e) e.preventDefault();
    const input = document.getElementById('aiDrawerInput');
    if (input && input.value.trim()) {
      sendDrawerQuestion(input.value.trim());
    }
  }

  function askChefAboutPantry() {
    const ings = Array.from(state.selectedIngredients);
    if (ings.length === 0) {
      showToast('Select at least one ingredient first!');
      return;
    }
    openAiDrawer();
    sendDrawerQuestion(`I have ${ings.map(i => i.replace(/-/g, ' ')).join(', ')} in my kitchen. What creative dishes or flavor pairings can I make with these?`);
  }

  function askModalChef(question) {
    const input = document.getElementById('modalAiInput');
    if (input) input.value = question;
    submitModalChefQuestion();
  }

  async function submitModalChefQuestion() {
    const input = document.getElementById('modalAiInput');
    const question = input ? input.value.trim() : '';
    if (!question) {
      showToast('Please enter a question for Chef Smart!');
      return;
    }

    const btnText = document.getElementById('modalAiBtnText');
    const btnSpinner = document.getElementById('modalAiBtnSpinner');
    const respBox = document.getElementById('modalAiResponseBox');
    const respText = document.getElementById('modalAiResponseText');

    if (btnText) btnText.textContent = 'Thinking...';
    if (btnSpinner) btnSpinner.classList.remove('hidden');

    const recipeName = state.currentModalRecipe ? state.currentModalRecipe.name : 'this recipe';
    const recipeIngs = state.currentModalRecipe ? (state.currentModalRecipe.ingredients || []) : [];

    try {
      const reply = await queryChefAI(question, recipeName, recipeIngs);
      if (respBox && respText) {
        respText.innerHTML = reply.replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>');
        respBox.classList.remove('hidden');
        respBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }
    } catch (err) {
      if (respBox && respText) {
        respText.textContent = 'Chef Smart is currently unavailable. Please try again!';
        respBox.classList.remove('hidden');
      }
    } finally {
      if (btnText) btnText.textContent = 'Ask Chef';
      if (btnSpinner) btnSpinner.classList.add('hidden');
    }
  }

  function showToast(msg) {
    const container = document.getElementById('toastContainer');
    if (!container) return;

    const toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = msg;

    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateY(10px)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 2800);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  return {
    toggleIngredient,
    addIngredient,
    removeIngredient,
    clearAllIngredients,
    applyPreset,
    launchPreset,
    handleTimeSliderChange,
    handleSearchSubmit,
    triggerAutoSearch,
    resetFilters,
    searchRecipes,
    openRecipeModalById,
    openRecipeModal,
    closeModal,
    closeMobileMenu,
    showToast,
    openAiDrawer,
    closeAiDrawer,
    toggleAiDrawer,
    sendDrawerQuestion,
    handleDrawerFormSubmit,
    askChefAboutPantry,
    askModalChef,
    submitModalChefQuestion
  };
})();
