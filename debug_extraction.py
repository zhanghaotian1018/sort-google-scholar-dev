#!/usr/bin/env python3
"""
Debug script to check Google Scholar HTML structure and data extraction
"""

import requests
from bs4 import BeautifulSoup
import re

def get_citations(content: str) -> int:
    """Extract number of citations from content using regex."""
    match = re.search(r"Cited by (\d+)", content)
    return int(match.group(1)) if match else 0

def get_year(content: str) -> int:
    """Extract publication year from content using regex."""
    match = re.search(r"\b(19|20)\d{2}\b", content)
    return int(match.group(0)) if match else 0

def clean_text(text: str) -> str:
    """Clean and normalize extracted text."""
    if not text:
        return ""
    text = text.replace("\xa0", " ").replace("\u200b", "").replace("\r", " ").replace("\n", " ")
    text = " ".join(text.split())
    return text.strip()

# Fetch a test page
url = "https://scholar.google.com/scholar?start=0&q=machine%20learning&hl=en&as_sdt=0,5"
print(f"Fetching: {url}\n")

session = requests.Session()
page = session.get(url)
page.encoding = 'utf-8'
c = page.content

soup = BeautifulSoup(c, "html.parser")
mydivs = soup.findAll("div", {"class": "gs_or"})

print(f"Found {len(mydivs)} results\n")
print("=" * 80)

for i, div in enumerate(mydivs[:3]):  # Check only first 3 results
    print(f"\n📄 Result #{i+1}:")
    print("-" * 80)
    
    # Title
    try:
        title = clean_text(div.find("h3").find("a").text)
        print(f"✓ Title: {title[:80]}..." if len(title) > 80 else f"✓ Title: {title}")
    except Exception as e:
        print(f"✗ Title extraction failed: {e}")
    
    # Author and other metadata
    try:
        meta_div = div.find("div", {"class": "gs_a"})
        meta_text = meta_div.text if meta_div else "Not found"
        print(f"✓ Raw metadata: {meta_text}")
        
        # Parse metadata parts
        parts = meta_text.split("-")
        print(f"  Parts count: {len(parts)}")
        for j, part in enumerate(parts):
            print(f"    Part {j}: {clean_text(part)[:60]}...")
            
    except Exception as e:
        print(f"✗ Metadata extraction failed: {e}")
    
    # Content/Abstract
    try:
        content_div = div.find("div", {"class": "gs_rs"})
        if content_div:
            content_text = clean_text(content_div.text)
            print(f"✓ Content length: {len(content_text)} characters")
            print(f"  Content: {content_text[:100]}..." if len(content_text) > 100 else f"  Content: {content_text}")
        else:
            print("✗ Content div not found")
    except Exception as e:
        print(f"✗ Content extraction failed: {e}")
    
    print("-" * 80)

print("\n✓ Debug extraction complete!")
