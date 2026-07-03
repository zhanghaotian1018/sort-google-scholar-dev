#!/usr/bin/env python3
"""
Detailed debug script to analyze Google Scholar HTML structure
"""

import requests
from bs4 import BeautifulSoup
import json

# Use web.archive.org for testing to avoid robot check
url = "https://web.archive.org/web/20210314203256/https://scholar.google.com/scholar?start=0&q=machine%20learning&hl=en&as_sdt=0,5"

print(f"Fetching: {url}\n")

try:
    session = requests.Session()
    page = session.get(url, timeout=10)
    page.encoding = 'utf-8'
    c = page.content

    soup = BeautifulSoup(c, "html.parser")
    mydivs = soup.findAll("div", {"class": "gs_or"})

    print(f"Found {len(mydivs)} results\n")
    print("=" * 100)

    for i, div in enumerate(mydivs[:2]):  # Check first 2 results
        print(f"\n📄 Result #{i+1}:")
        print("-" * 100)
        
        # Get the metadata div
        try:
            meta_div = div.find("div", {"class": "gs_a"})
            if meta_div:
                meta_text = meta_div.text
                meta_html = meta_div.get_text(separator='|', strip=True)
                
                print(f"Raw metadata text:\n  {meta_text}\n")
                print(f"Metadata with separators:\n  {meta_html}\n")
                
                # Try to analyze the structure
                print("Metadata structure analysis:")
                # Split by common delimiters
                parts_by_dash = meta_text.split("-")
                parts_by_comma = meta_text.split(",")
                
                print(f"  Parts split by '-' ({len(parts_by_dash)}):")
                for j, part in enumerate(parts_by_dash):
                    clean_part = part.strip()
                    print(f"    [{j}]: '{clean_part}'")
                
                print(f"\n  Format Analysis:")
                print(f"    Author: '{parts_by_dash[0].strip()}'")
                if len(parts_by_dash) >= 3:
                    year = parts_by_dash[1].strip()
                    publisher = "-".join(parts_by_dash[2:]).strip()
                    print(f"    Year: '{year}'")
                    print(f"    Publisher: '{publisher}'")
        except Exception as e:
            print(f"Error analyzing metadata: {e}")
        
        # Get content/abstract
        try:
            content_div = div.find("div", {"class": "gs_rs"})
            if content_div:
                content_text = content_div.text.strip()
                print(f"\nContent information:")
                print(f"  Text length: {len(content_text)} chars")
                print(f"  Full text: {content_text}")
                print(f"  Has ellipsis: {'…' in content_text}")
                
                # Check all children
                print(f"\n  HTML structure of content div:")
                print(f"  {content_div.prettify()[:500]}...")
        except Exception as e:
            print(f"Error getting content: {e}")
        
        print("-" * 100)

except Exception as e:
    print(f"Error: {e}")
    print("Note: If robot check, try using web.archive.org URL")

print("\n✓ Analysis complete!")
