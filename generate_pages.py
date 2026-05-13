#!/usr/bin/env python3
"""Generate 10 brand HTML pages from the alchemy-london.html template."""

import re

# Read template
with open("/Users/atiqarahman/clawd/gtf-brand-pages/alchemy-london.html") as f:
    template = f.read()

brands = [
    {
        "filename": "alexeaglestudio.html",
        "name": "Alex Eagle Studio",
        "name_upper": "ALEX EAGLE STUDIO",
        "slug": "alex-eagle-studio",
        "desc": "Luxury lifestyle brand based in Soho, London. Ready-to-wear wardrobe essentials crafted with British craftsmanship and fine fabrics. A 360° take on modern retail.",
        "vibes": ["Old Money", "Elevated Basics", "Elevated City"],
        "products": [
            ("Wool Tailored Blazer", "£485", "~AED 2,280"),
            ("Silk Slip Dress", "£395", "~AED 1,857"),
            ("Cashmere Crew Neck", "£320", "~AED 1,504"),
            ("Linen Wide-Leg Trousers", "£285", "~AED 1,340"),
        ],
        "dashboard_revenue": "$18.6k",
        "dashboard_orders": "38",
        "dashboard_avg": "$489",
        "dashboard_vibe": "Old Money",
        "dashboard_pct": "72% of traffic",
        "search_query": "understated luxury wardrobe essentials British tailoring",
        "cta_city": "London",
    },
    {
        "filename": "aria-cove.html",
        "name": "Aria Cove",
        "name_upper": "ARIA COVE",
        "slug": "aria-cove",
        "desc": "Fashion for confident women who know who they are. Statement dresses, bodysuits, and co-ords designed to turn heads. UK-based with a loyal following.",
        "vibes": ["Sexy Elegant", "IT Girl", "Glam"],
        "products": [
            ("Satin Cowl Neck Midi Dress", "£85", "~AED 400"),
            ("Cut-Out Bodysuit", "£48", "~AED 226"),
            ("Ruched Mini Dress", "£72", "~AED 338"),
            ("Sequin Co-ord Set", "£120", "~AED 564"),
        ],
        "dashboard_revenue": "$22.1k",
        "dashboard_orders": "156",
        "dashboard_avg": "$142",
        "dashboard_vibe": "Sexy Elegant",
        "dashboard_pct": "68% of traffic",
        "search_query": "going out dress satin bodycon date night",
        "cta_city": "London",
    },
    {
        "filename": "galvan-london.html",
        "name": "Galvan London",
        "name_upper": "GALVAN LONDON",
        "slug": "galvan-london",
        "desc": "Luxury evening wear cut from bias-cut satin and sculpting jersey. Modern and timeless gowns in rich tones and soft pastels. Stocked at Farfetch and Saks Fifth Avenue.",
        "vibes": ["Glam", "Sexy Elegant", "Wedding Guest"],
        "products": [
            ("Bias-Cut Satin Gown", "£1,250", "~AED 5,875"),
            ("Sequin Column Dress", "£890", "~AED 4,183"),
            ("Halterneck Midi", "£650", "~AED 3,055"),
            ("Jersey Draped Top", "£420", "~AED 1,974"),
        ],
        "dashboard_revenue": "$31.4k",
        "dashboard_orders": "24",
        "dashboard_avg": "$1,308",
        "dashboard_vibe": "Glam",
        "dashboard_pct": "58% of traffic",
        "search_query": "luxury evening gown satin bias-cut elegant",
        "cta_city": "London",
    },
    {
        "filename": "rohe.html",
        "name": "Róhe",
        "name_upper": "RÓHE",
        "slug": "rohe",
        "desc": "Amsterdam-based design studio and atelier. Contemporary shapes through distinct design elements and precise craftsmanship. Elevated minimalism loved by European influencers. Forbes-featured.",
        "vibes": ["Old Money", "Elevated Basics", "Cool Girl"],
        "products": [
            ("Structured Wool Coat", "€680", "~AED 2,720"),
            ("Draped Silk Blouse", "€380", "~AED 1,520"),
            ("Tailored Wide Trousers", "€420", "~AED 1,680"),
            ("Minimal Knit Top", "€240", "~AED 960"),
        ],
        "dashboard_revenue": "$16.8k",
        "dashboard_orders": "31",
        "dashboard_avg": "$542",
        "dashboard_vibe": "Elevated Basics",
        "dashboard_pct": "76% of traffic",
        "search_query": "elevated minimalist Amsterdam contemporary tailoring",
        "cta_city": "London",
    },
    {
        "filename": "laganini.html",
        "name": "Laganini",
        "name_upper": "LAGANINI",
        "slug": "laganini",
        "desc": "Mediterranean resort wear from Spain. Relaxed elegance that captures the sun-kissed ease of coastal living. Effortless pieces for the modern traveler.",
        "vibes": ["Beach & Resort", "Cool Girl", "Elevated Basics"],
        "products": [
            ("Linen Wrap Dress", "€220", "~AED 880"),
            ("Cotton Oversized Shirt", "€145", "~AED 580"),
            ("Crochet Midi Skirt", "€185", "~AED 740"),
            ("Silk Resort Co-ord", "€340", "~AED 1,360"),
        ],
        "dashboard_revenue": "$11.2k",
        "dashboard_orders": "42",
        "dashboard_avg": "$267",
        "dashboard_vibe": "Beach & Resort",
        "dashboard_pct": "71% of traffic",
        "search_query": "Mediterranean resort wear linen vacation dress",
        "cta_city": "London",
    },
    {
        "filename": "intogaia.html",
        "name": "Into Gaia",
        "name_upper": "INTO GAIA",
        "slug": "into-gaia",
        "desc": "Sustainable fashion bridging London's contemporary edge with Bali's artisanal craft. Conscious design that doesn't compromise on style. Where modern silhouettes meet handmade heritage.",
        "vibes": ["Unique Finds", "Cool Girl", "Elevated Basics"],
        "products": [
            ("Hand-Dyed Silk Dress", "£280", "~AED 1,316"),
            ("Artisan Woven Jacket", "£195", "~AED 917"),
            ("Organic Cotton Co-ord", "£165", "~AED 776"),
            ("Batik Print Midi Skirt", "£140", "~AED 658"),
        ],
        "dashboard_revenue": "$9.4k",
        "dashboard_orders": "35",
        "dashboard_avg": "$269",
        "dashboard_vibe": "Unique Finds",
        "dashboard_pct": "64% of traffic",
        "search_query": "sustainable artisan handmade conscious fashion",
        "cta_city": "London",
    },
    {
        "filename": "venderbys.html",
        "name": "Venderby's",
        "name_upper": "VENDERBY'S",
        "slug": "venderbys",
        "desc": "Scandinavian minimalism meets modern femininity. Clean lines, muted palettes, and thoughtful construction from Copenhagen. The Danish approach to effortless dressing.",
        "vibes": ["Elevated Basics", "Old Money", "Elevated City"],
        "products": [
            ("Structured Blazer", "€380", "~AED 1,520"),
            ("Merino Knit Dress", "€295", "~AED 1,180"),
            ("Tailored Wool Trousers", "€260", "~AED 1,040"),
            ("Silk Cami Top", "€155", "~AED 620"),
        ],
        "dashboard_revenue": "$13.6k",
        "dashboard_orders": "36",
        "dashboard_avg": "$378",
        "dashboard_vibe": "Elevated Basics",
        "dashboard_pct": "74% of traffic",
        "search_query": "Scandinavian minimalist clean elegant Copenhagen",
        "cta_city": "London",
    },
    {
        "filename": "desigual.html",
        "name": "Desigual",
        "name_upper": "DESIGUAL",
        "slug": "desigual",
        "desc": "Bold, colorful, unapologetically artistic. Born in Barcelona, known worldwide for vibrant prints, artistic collaborations, and fashion that celebrates individuality. La Vida es Chula.",
        "vibes": ["IT Girl", "Unique Finds", "Cool Girl"],
        "products": [
            ("Artistic Print Midi Dress", "€149", "~AED 596"),
            ("Patchwork Denim Jacket", "€189", "~AED 756"),
            ("Embroidered Boho Blouse", "€89", "~AED 356"),
            ("Color-Block Knit Sweater", "€119", "~AED 476"),
        ],
        "dashboard_revenue": "$28.7k",
        "dashboard_orders": "189",
        "dashboard_avg": "$152",
        "dashboard_vibe": "IT Girl",
        "dashboard_pct": "55% of traffic",
        "search_query": "bold colorful artistic print statement fashion",
        "cta_city": "London",
    },
    {
        "filename": "ashes-moscow.html",
        "name": "Ashes Moscow",
        "name_upper": "ASHES MOSCOW",
        "slug": "ashes-moscow",
        "desc": "Contemporary fashion with architectural edge from Moscow. Structured silhouettes, unexpected details, and a darkly elegant aesthetic. Where Russian avant-garde meets wearable design.",
        "vibes": ["Cool Girl", "Elevated City", "Unique Finds"],
        "products": [
            ("Deconstructed Blazer", "€420", "~AED 1,680"),
            ("Asymmetric Wool Dress", "€350", "~AED 1,400"),
            ("Structured Leather Top", "€280", "~AED 1,120"),
            ("Architectural Trench", "€520", "~AED 2,080"),
        ],
        "dashboard_revenue": "$12.3k",
        "dashboard_orders": "28",
        "dashboard_avg": "$439",
        "dashboard_vibe": "Cool Girl",
        "dashboard_pct": "61% of traffic",
        "search_query": "architectural contemporary structured dark elegant",
        "cta_city": "London",
    },
    {
        "filename": "korobeynikov.html",
        "name": "KOROBEYNIKOV",
        "name_upper": "KOROBEYNIKOV",
        "slug": "korobeynikov",
        "desc": "Designer eveningwear with structured elegance from Russia. Bold silhouettes, luxurious fabrics, and meticulous construction. For women who command the room.",
        "vibes": ["Glam", "Sexy Elegant", "Dubai Glam"],
        "products": [
            ("Crystal Embellished Gown", "€1,200", "~AED 4,800"),
            ("Sculpted Blazer Dress", "€680", "~AED 2,720"),
            ("Draped Satin Midi", "€520", "~AED 2,080"),
            ("Feather-Trim Cocktail Dress", "€890", "~AED 3,560"),
        ],
        "dashboard_revenue": "$19.8k",
        "dashboard_orders": "16",
        "dashboard_avg": "$1,238",
        "dashboard_vibe": "Glam",
        "dashboard_pct": "66% of traffic",
        "search_query": "designer evening gown crystal embellished luxury",
        "cta_city": "London",
    },
]

def generate_page(brand, template):
    page = template
    
    # Title
    page = page.replace("Alchemy London × Get The Fit", f"{brand['name']} × Get The Fit")
    
    # Intro banner
    page = page.replace("Exclusive Preview for Alchemy London", f"Exclusive Preview for {brand['name']}")
    page = page.replace("Imagine <em>Alchemy London</em> on Get The Fit", f"Imagine <em>{brand['name']}</em> on Get The Fit")
    page = page.replace("Here's how your customers would discover, try on, and buy your pieces on GTF.", f"Here's how your customers would discover, try on, and buy your pieces on GTF.")
    
    # Search query
    page = page.replace('value="contemporary London fashion jewellery bold"', f'value="{brand["search_query"]}"')
    
    # Vibes/Pills
    old_pills = '<span class="pill">Cool Girl</span>\n      <span class="pill">IT Girl</span>\n      <span class="pill">Elegant</span>'
    new_pills = "\n      ".join(f'<span class="pill">{v}</span>' for v in brand["vibes"])
    page = page.replace(old_pills, new_pills)
    
    # Brand name replacements
    page = page.replace("ALCHEMY LONDON", brand["name_upper"])
    page = page.replace("Alchemy London", brand["name"])
    page = page.replace("Alchemy", brand["name"])
    
    # Products - replace product names and prices
    old_products = [
        ("Green Sleeveless Vest", "£320", "~AED 1,504"),
        ("Black Keyhole Top", "£280", "~AED 1,316"),
        ("Mauve Cutout Top", "£295", "~AED 1,386"),
        ("Pearl Chain Set", "£180", "~AED 846"),
    ]
    
    for i, (old_name, old_price, old_conv) in enumerate(old_products):
        if i < len(brand["products"]):
            new_name, new_price, new_conv = brand["products"][i]
            page = page.replace(old_name, new_name)
            page = page.replace(old_price, new_price)
            page = page.replace(old_conv, new_conv)
    
    # Extra products referenced (5, 6)
    page = page.replace("Gold Statement Bracelet", brand["products"][0][0] if brand["products"] else "Statement Piece")
    
    # Dashboard
    page = page.replace("$14.2k", brand["dashboard_revenue"])
    page = page.replace(">47<", f">{brand['dashboard_orders']}<")
    page = page.replace("$302", brand["dashboard_avg"])
    page = page.replace(">Cool Girl<", f">{brand['dashboard_vibe']}<")
    page = page.replace("64% of traffic", brand["dashboard_pct"])
    page = page.replace(f"{brand['name']} — Brand Dashboard", f"{brand['name']} — Brand Dashboard")
    
    # Brand description
    page = page.replace("Contemporary jewellery-inspired fashion. Bold accessories meet clean silhouettes.", brand["desc"])
    
    # CTA
    page = page.replace("Let's meet in London", f"Let's meet in {brand['cta_city']}")
    page = page.replace(f"how {brand['name']} fits into GTF's curated collection", f"how {brand['name']} fits into GTF's curated collection")
    
    # Image paths - use brand slug
    page = page.replace("images/alchemy-london/", f"images/{brand['slug']}/")
    
    return page

# Generate all pages
for brand in brands:
    page = generate_page(brand, template)
    output_path = f"/Users/atiqarahman/clawd/gtf-brand-pages/{brand['filename']}"
    with open(output_path, "w") as f:
        f.write(page)
    print(f"✅ {brand['filename']} — {brand['name']}")

print(f"\nDone! {len(brands)} pages created.")
