#!/usr/bin/env python3
"""Scrape product images from brand websites for the HTML pages."""

import json
import os
import re
import time
import urllib.request
from pathlib import Path

BASE = "/Users/atiqarahman/clawd/gtf-brand-pages/images"

BRANDS = {
    "alex-eagle-studio": {
        "shopify_url": "https://alexeagle.com/collections/clothing/products.json?limit=8",
        "fallback_urls": [
            "https://alexeagle.com/collections/dresses/products.json?limit=5",
            "https://alexeagle.com/collections/tops/products.json?limit=5",
        ],
    },
    "aria-cove": {
        "shopify_url": "https://www.ariacove.com/collections/all/products.json?limit=8",
        "fallback_urls": [
            "https://www.ariacove.com/collections/dresses/products.json?limit=5",
        ],
    },
    "galvan-london": {
        "shopify_url": "https://www.galvanlondon.com/collections/all/products.json?limit=8",
        "fallback_urls": [
            "https://www.galvanlondon.com/collections/eveningwear/products.json?limit=5",
        ],
    },
    "rohe": {
        "shopify_url": "https://roheframes.com/collections/all/products.json?limit=8",
        "fallback_urls": [],
    },
    "laganini": {
        "shopify_url": "https://laganini.com/collections/all/products.json?limit=8",
        "fallback_urls": [
            "https://www.laganini.com/collections/all/products.json?limit=8",
        ],
    },
    "into-gaia": {
        "shopify_url": "https://intogaia.com/collections/all/products.json?limit=8",
        "fallback_urls": [
            "https://www.intogaia.com/collections/all/products.json?limit=8",
        ],
    },
    "venderbys": {
        "shopify_url": "https://venderbys.com/collections/all/products.json?limit=8",
        "fallback_urls": [
            "https://www.venderbys.com/collections/all/products.json?limit=8",
        ],
    },
    "desigual": {
        "shopify_url": "https://www.desigual.com/collections/all/products.json?limit=8",
        "fallback_urls": [],
    },
    "ashes-moscow": {
        "shopify_url": "https://ashes-moscow.com/collections/all/products.json?limit=8",
        "fallback_urls": [
            "https://www.ashes-moscow.com/collections/all/products.json?limit=8",
        ],
    },
    "korobeynikov": {
        "shopify_url": "https://korobeynikov.com/collections/all/products.json?limit=8",
        "fallback_urls": [
            "https://www.korobeynikov.com/collections/all/products.json?limit=8",
        ],
    },
}

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except Exception as e:
        return None

def download_image(url, path):
    try:
        # Get highest quality version
        url = re.sub(r'_\d+x\d+', '', url)
        url = re.sub(r'\?v=\d+', '', url)
        if '?' not in url:
            url += '?width=800'
        else:
            url += '&width=800'
            
        req = urllib.request.Request(url, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
        })
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
            if len(data) > 1000:  # Not an error page
                with open(path, 'wb') as f:
                    f.write(data)
                return True
    except Exception as e:
        pass
    return False

def scrape_brand(slug, config):
    out_dir = os.path.join(BASE, slug)
    os.makedirs(out_dir, exist_ok=True)
    
    # Try main URL first, then fallbacks
    urls = [config["shopify_url"]] + config.get("fallback_urls", [])
    products = []
    
    for url in urls:
        data = fetch_json(url)
        if data and "products" in data:
            products = data["products"]
            break
        time.sleep(0.5)
    
    if not products:
        print(f"  ❌ No products found for {slug}")
        return []
    
    print(f"  Found {len(products)} products")
    
    downloaded = []
    for i, product in enumerate(products[:6]):
        title = product.get("title", f"Product {i+1}")
        images = product.get("images", [])
        if not images:
            continue
        
        img_url = images[0].get("src", "")
        if not img_url:
            continue
        
        # Ensure https
        if img_url.startswith("//"):
            img_url = "https:" + img_url
        
        filename = f"product-{i+1}.jpg"
        filepath = os.path.join(out_dir, filename)
        
        if os.path.exists(filepath) and os.path.getsize(filepath) > 5000:
            print(f"    ⏭️  {title[:40]} (already downloaded)")
            downloaded.append({"title": title, "file": filename, "price": ""})
            continue
        
        ok = download_image(img_url, filepath)
        if ok:
            price = ""
            variants = product.get("variants", [])
            if variants:
                price = variants[0].get("price", "")
            
            print(f"    ✅ {title[:40]} → {filename}")
            downloaded.append({"title": title, "file": filename, "price": price})
        else:
            print(f"    ❌ Failed: {title[:40]}")
        
        time.sleep(0.3)
    
    return downloaded

def main():
    print("=" * 60)
    print("  SCRAPING BRAND PRODUCT IMAGES")
    print("=" * 60)
    
    results = {}
    for slug, config in BRANDS.items():
        print(f"\n📦 {slug}")
        downloaded = scrape_brand(slug, config)
        results[slug] = downloaded
    
    # Save results
    with open(os.path.join(BASE, "scrape_results.json"), "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"\n{'='*60}")
    total = sum(len(v) for v in results.values())
    print(f"  DONE. {total} images across {len(results)} brands")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
