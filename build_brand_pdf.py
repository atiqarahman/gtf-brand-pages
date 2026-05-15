#!/usr/bin/env python3
"""
Build GTF Partnership Proposal PDFs — same format as Zen Oficial proposal.
Generates an HTML version that can be exported to PDF.
"""

import os

OUTPUT_DIR = "/Users/atiqarahman/clawd/gtf-brand-pages/proposals"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Brand data for London brands
BRANDS = [
    {
        "name": "Galvan London",
        "slug": "galvan-london",
        "tagline": "FROM SCULPTURE TO CART. FRICTIONLESS.",
        "hook": "the platform where bias-cut precision meets AI-powered discovery",
        "discovery_gap_scenario": "A woman in Dubai is getting ready for New Year's Eve at Nobu DIFC. She screenshots a Galvan satin gown from Instagram — the way it drapes, the confident silhouette. She searches. She finds fast fashion knockoffs. She can't find you. That sale — and probably a $1,200 order — is lost.",
        "brand_validation": "Galvan London has built something rare: luxury evening wear that feels modern, not costumey. Stocked at Farfetch and Saks, worn by women who want to command a room without trying too hard. Your bias-cut satins and sculptural jerseys sit in a price point ($400-$2,000) that proves investment-quality design.",
        "search_queries": [
            ('"Something satin for New Year\'s Eve in Dubai"', 'GTF AI: occasion = evening/NYE, material = satin, vibe = Glam → surfaces Galvan Aphrodite Midi Dress'),
            ('"Elegant column dress for a wedding reception"', 'GTF AI: occasion = wedding-guest, silhouette = column, vibe = Wedding Guest → surfaces Galvan Amorphous Silk Dress'),
            ('"Like what Meghan Markle would wear to a gala"', 'GTF AI: style reference = polished, modern royal, occasion = formal → surfaces Galvan structured evening pieces'),
            ('"Sculptural but wearable — not costume-y"', 'GTF AI: silhouette = structured/sculptural, vibe = Sexy Elegant, keywords = elevated → surfaces Galvan jersey pieces'),
            ('"Something that moves beautifully when I walk"', 'GTF AI: material = flowing/satin, silhouette = bias-cut, keyword = movement → surfaces Galvan drape dresses'),
        ],
        "vibes": ["Glam", "Sexy Elegant", "Wedding Guest", "Dubai Glam"],
        "dna_table": [
            ("Bias-cut satin construction", "AI indexes silhouette + material as core attributes", '"Something that drapes" queries → Galvan'),
            ("Evening → ready-to-wear evolution", "Occasion-aware discovery", "Day-to-night queries find your transition pieces"),
            ("£400-£2,000 range", '"Investment piece" positioning', "Above Zara, below couture = GTF sweet spot"),
            ("Farfetch/Saks credibility", "Trust + premium positioning", "Pre-validated luxury = higher conversion confidence"),
            ("Sculptural jersey + satin", "Material-specific search matching", '"Satin dress" and "jersey evening" queries surface Galvan'),
            ("British design heritage", "Global emerging brand curation", "UK luxury brand accessible to MENA = exclusivity"),
        ],
        "poc_email": "",
        "country": "UK",
        "currency": "£",
        "html_preview": "https://atiqarahman.github.io/gtf-brand-pages/galvan-london.html",
    },
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Get The Fit × {name} — Partnership Proposal</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap');
  
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  
  body {{
    font-family: 'Inter', -apple-system, sans-serif;
    background: #0a0a0a;
    color: #e0e0e0;
    max-width: 900px;
    margin: 0 auto;
    padding: 0;
  }}

  .page {{
    min-height: 100vh;
    padding: 60px 48px;
    page-break-after: always;
    position: relative;
  }}

  .page:last-child {{ page-break-after: avoid; }}

  h1 {{
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: 400;
    color: #fff;
    margin-bottom: 16px;
  }}

  h2 {{
    font-family: 'Playfair Display', serif;
    font-size: 28px;
    font-weight: 400;
    color: #fff;
    margin-bottom: 12px;
  }}

  h3 {{
    font-size: 16px;
    font-weight: 600;
    color: #7C6AEF;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 16px;
  }}

  p {{
    font-size: 14px;
    line-height: 1.75;
    color: #bbb;
    margin-bottom: 16px;
  }}

  .accent {{ color: #7C6AEF; }}
  .bold {{ font-weight: 700; color: #fff; }}
  
  /* Cover */
  .cover {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 100vh;
    text-align: center;
  }}

  .cover .brand-x {{
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    color: #7C6AEF;
    margin-bottom: 24px;
  }}

  .cover h1 {{
    font-size: 52px;
    margin-bottom: 20px;
  }}

  .cover .tagline {{
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    font-style: italic;
    color: #888;
    margin-bottom: 40px;
  }}

  .cover .hook {{
    font-size: 15px;
    color: #999;
    max-width: 500px;
    margin: 0 auto 40px;
  }}

  .cover .footer {{
    font-size: 11px;
    color: #555;
    letter-spacing: 1px;
  }}

  /* Stats banner */
  .stats-row {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin: 24px 0;
  }}

  .stat-box {{
    background: #151515;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
  }}

  .stat-box .num {{
    font-size: 28px;
    font-weight: 700;
    color: #7C6AEF;
  }}

  .stat-box .label {{
    font-size: 10px;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-top: 4px;
  }}

  /* Query cards */
  .query-card {{
    background: #151515;
    border-left: 4px solid #7C6AEF;
    padding: 16px 20px;
    border-radius: 0 10px 10px 0;
    margin-bottom: 12px;
  }}

  .query-card .query {{
    font-size: 15px;
    font-weight: 600;
    color: #fff;
    margin-bottom: 6px;
  }}

  .query-card .result {{
    font-size: 12px;
    color: #888;
  }}

  /* Screenshot */
  .screenshot {{
    width: 100%;
    border-radius: 12px;
    margin: 16px 0;
    box-shadow: 0 4px 20px rgba(124, 106, 239, 0.1);
  }}

  .caption {{
    font-size: 11px;
    color: #666;
    text-align: center;
    margin-bottom: 20px;
    font-style: italic;
  }}

  /* DNA table */
  table {{
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 13px;
  }}

  th {{
    background: #7C6AEF;
    color: #fff;
    font-weight: 600;
    text-align: left;
    padding: 12px 16px;
  }}

  td {{
    padding: 12px 16px;
    border-bottom: 1px solid #222;
    color: #ccc;
  }}

  tr:nth-child(even) td {{ background: #111; }}

  /* Toolkit cards */
  .toolkit-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin: 16px 0;
  }}

  .tool-card {{
    background: #151515;
    border-left: 4px solid #7C6AEF;
    border-radius: 0 10px 10px 0;
    padding: 16px 20px;
  }}

  .tool-card h4 {{
    font-size: 14px;
    font-weight: 600;
    color: #fff;
    margin-bottom: 4px;
  }}

  .tool-card p {{
    font-size: 12px;
    color: #888;
    margin: 0;
  }}

  /* Commission */
  .commission-box {{
    background: linear-gradient(135deg, #1a1040, #2a1a60);
    border-radius: 16px;
    padding: 32px;
    text-align: center;
    margin: 24px 0;
  }}

  .commission-box .rate {{
    font-size: 64px;
    font-weight: 700;
    color: #7C6AEF;
  }}

  .commission-box .sub {{
    font-size: 14px;
    color: #888;
  }}

  /* CTA */
  .cta-box {{
    text-align: center;
    padding: 40px;
    background: linear-gradient(135deg, #0a0a0a, #1a1040);
    border-radius: 16px;
    margin: 24px 0;
  }}

  .cta-box a {{
    display: inline-block;
    padding: 16px 48px;
    background: #7C6AEF;
    color: #fff;
    text-decoration: none;
    font-weight: 700;
    border-radius: 8px;
    font-size: 14px;
    margin: 12px 0;
  }}

  @media print {{
    body {{ background: #0a0a0a; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    .page {{ page-break-after: always; }}
  }}
</style>
</head>
<body>

<!-- PAGE 1: COVER -->
<div class="page cover">
  <div class="brand-x">GET THE FIT × {name_upper}</div>
  <h1>Partnership Proposal</h1>
  <div class="tagline">{tagline}</div>
  <div class="hook">{hook}</div>
  <div class="footer">PREPARED EXCLUSIVELY FOR {name_upper}<br>By Atiqa Rahman, CEO — Get The Fit · May 2026</div>
</div>

<!-- PAGE 2: THE DISCOVERY GAP -->
<div class="page">
  <h3>The Problem</h3>
  <h2>The Discovery Gap Your Customers Face</h2>
  <p style="color:#fff;font-size:15px;line-height:1.8;margin-bottom:24px;">{discovery_gap}</p>
  <p>{brand_validation}</p>
  <p style="color:#fff;font-weight:600;">Instagram shows, it doesn't sell. And traditional marketplaces bury emerging brands under fast fashion noise.</p>
  
  <h3 style="margin-top:32px;">What Your Customer Actually Searches For</h3>
  {query_cards}
  <p style="margin-top:16px;">No traditional marketplace can process these queries. They rely on category filters. GTF's AI understands intent, vibe, occasion, and style — and matches them to your product attributes.</p>
</div>

<!-- PAGE 3: THE PLATFORM -->
<div class="page">
  <h3>The Platform</h3>
  <h2>The GTF Platform — Built for Discovery</h2>
  
  <div class="stats-row">
    <div class="stat-box"><div class="num">$60K</div><div class="label">GMV in 3 months</div></div>
    <div class="stat-box"><div class="num">15+</div><div class="label">Brands onboarding</div></div>
    <div class="stat-box"><div class="num">$200K</div><div class="label">Antler-backed</div></div>
    <div class="stat-box"><div class="num">$16K</div><div class="label">Top brand at UAE pop-up</div></div>
  </div>
  
  <p>Get The Fit brings the entire shopping journey into one place — from natural language discovery to virtual try-on to checkout. Every feature converts browsers into buyers for brands like {name}.</p>
  
  <p><span class="bold">Try it live:</span> <a href="https://gtf.minterminds.in/shop/product/contour-knit-dress" style="color:#7C6AEF;">Product Page</a> · <a href="https://gtf.minterminds.in/outfit-creator" style="color:#7C6AEF;">Outfit Creator</a> · <a href="https://gtf.minterminds.in/designers" style="color:#7C6AEF;">Our Designers</a></p>

  <h3 style="margin-top:24px;">Our Designers — Discover by Vibe</h3>
  <img src="platform-screenshots/our-designers.jpg" class="screenshot" alt="Our Designers">
  <div class="caption">Every brand has a dedicated page with their aesthetic, vibes, and collection — filterable by vibe and region</div>
  
  <img src="platform-screenshots/brand-vibes-dropdown.jpg" class="screenshot" alt="Brand Vibes">
  <div class="caption">Customers discover brands through vibes — {name} would surface under {vibes_str}</div>
</div>

<!-- PAGE 4: SHOP THE LOOK + OUTFIT CREATOR -->
<div class="page">
  <h3>Features</h3>
  <h2>Outfit Creator + Cross-Brand Styling</h2>
  <p>This is where the magic happens. Customers build complete outfits mixing pieces from different designers. Your products get discovered by customers who came for another brand — and leave with yours too.</p>
  
  <img src="platform-screenshots/outfit-creator.jpg" class="screenshot" alt="Outfit Creator">
  <div class="caption">Outfit Creator — customers mix and match across brands, "Try On Me" brings it together</div>
  
  <h3 style="margin-top:32px;">Community Spotlight — Shoppable UGC</h3>
  <p>Real looks from real customers. Every video and photo is shoppable. Social proof that converts.</p>
  
  <img src="platform-screenshots/spotlight-ugc.jpg" class="screenshot" alt="Spotlight">
  <div class="caption">Spotlight — shoppable UGC with engagement metrics. Real customers, real outfits, real purchases.</div>
</div>

<!-- PAGE 5: WHY THIS BRAND -->
<div class="page">
  <h3>The Fit</h3>
  <h2>Why {name} Is a Perfect Partner</h2>
  
  <table>
    <tr><th>{name} DNA</th><th>GTF Positioning</th><th>Why It Converts</th></tr>
    {dna_rows}
  </table>
</div>

<!-- PAGE 6: TOOLKIT -->
<div class="page">
  <h3>What You Get</h3>
  <h2>The Complete GTF Toolkit for {name}</h2>
  
  <div class="toolkit-grid">
    <div class="tool-card"><h4>🔍 AI Discovery Engine</h4><p>14-attribute product indexing. Natural language + image search. Vibe, occasion, style reference matching.</p></div>
    <div class="tool-card"><h4>🧪 Virtual Try-On</h4><p>On every PDP. Customer sees themselves in your clothes. 3-5x conversion uplift.</p></div>
    <div class="tool-card"><h4>✨ Outfit Builder</h4><p>Cross-brand outfit creation with your pieces as anchors. Increases AOV.</p></div>
    <div class="tool-card"><h4>🎬 Shoppable UGC</h4><p>Real customer videos. Engagement metrics. Social proof that converts.</p></div>
    <div class="tool-card"><h4>👗 Shop the Look</h4><p>Editorial-to-commerce. Full outfit toggles. One-click add-to-bag.</p></div>
    <div class="tool-card"><h4>📊 Brand Dashboard</h4><p>Real-time: views, clicks, conversions, top queries, vibe indexing.</p></div>
    <div class="tool-card"><h4>🌍 Global Logistics</h4><p>DHL + Zonos. Customs pre-calculated. You ship, we handle international.</p></div>
    <div class="tool-card"><h4>🏷 Brand Page</h4><p>Your story, aesthetic tags, trending products, UGC gallery. Premium experience.</p></div>
  </div>
</div>

<!-- PAGE 7: COMMISSION + CTA -->
<div class="page">
  <h3>Terms</h3>
  <h2>Commission & Payout</h2>
  
  <div class="commission-box">
    <div class="rate">35%</div>
    <div class="sub">Performance-based. You pay zero if we don't sell.</div>
  </div>
  
  <table>
    <tr><th>Channel</th><th>Effective Cost</th><th>What You Get</th></tr>
    <tr><td>Instagram/Meta Ads</td><td>25-35% of revenue</td><td>Impressions, maybe clicks. You pay even if nobody buys.</td></tr>
    <tr><td>Influencer Marketing</td><td>15-40% per campaign</td><td>One-time exposure. Content expires.</td></tr>
    <tr><td>Traditional Marketplace</td><td>30-45% + listing fees</td><td>Buried in 10,000 brands. Discount-driven.</td></tr>
    <tr><td style="color:#7C6AEF;font-weight:600;">GTF (35%)</td><td style="color:#7C6AEF;font-weight:600;">35% — only on sales</td><td style="color:#7C6AEF;">AI discovery + try-on + outfit builder + UGC + global logistics + analytics. Zero upfront.</td></tr>
  </table>
  
  <div class="cta-box" style="margin-top:40px;">
    <h2>Let's Meet in London</h2>
    <p style="color:#888;">I'll be in London next month. 30 minutes — I'll show you the full platform live and discuss how {name} fits into GTF.</p>
    <a href="https://calendly.com/atiqa-getthefit/30min">BOOK A 30-MIN MEETING →</a>
    <p style="font-size:11px;color:#555;margin-top:12px;">Atiqa Rahman, Founder · Get The Fit · Antler-backed · UAE-based</p>
  </div>
</div>

</body>
</html>"""

def generate_proposal(brand):
    query_cards = ""
    for query, result in brand["search_queries"]:
        query_cards += f'<div class="query-card"><div class="query">{query}</div><div class="result">→ {result}</div></div>\n'
    
    dna_rows = ""
    for dna, positioning, converts in brand["dna_table"]:
        dna_rows += f"<tr><td>{dna}</td><td>{positioning}</td><td>{converts}</td></tr>\n"
    
    html = HTML_TEMPLATE.format(
        name=brand["name"],
        name_upper=brand["name"].upper(),
        tagline=brand["tagline"],
        hook=brand["hook"],
        discovery_gap=brand["discovery_gap_scenario"],
        brand_validation=brand["brand_validation"],
        query_cards=query_cards,
        dna_rows=dna_rows,
        vibes_str=", ".join(brand["vibes"]),
    )
    
    out_path = os.path.join(OUTPUT_DIR, f"GTF-x-{brand['slug']}-Proposal.html")
    with open(out_path, "w") as f:
        f.write(html)
    print(f"✅ {out_path}")
    return out_path

# Generate Galvan as the first one for Atiqa to approve
for brand in BRANDS:
    generate_proposal(brand)

print("\nDone! Open the HTML in browser, then print to PDF.")
