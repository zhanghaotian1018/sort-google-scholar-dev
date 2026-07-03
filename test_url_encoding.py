#!/usr/bin/env python3
"""
Test script to verify URL encoding fix for complex queries
"""

import urllib.parse

def test_url_encoding():
    """Test URL encoding for complex Google Scholar queries"""

    test_queries = [
        # Simple query
        "machine learning",

        # Query with quotes
        '"cultural heritage"',

        # Complex query with AND/OR
        '"cultural heritage" AND "CT imaging" AND "semantic segmentation" OR "reconstruction" OR "super-resolution"',

        # Query with special characters
        'deep learning OR "neural networks"',

        # Query with parentheses
        '(machine learning OR AI) AND "computer vision"',
    ]

    print("Testing URL encoding for Google Scholar queries:")
    print("=" * 80)

    for query in test_queries:
        # Old method (broken)
        old_encoded = query.replace(" ", "+")

        # New method (fixed)
        new_encoded = urllib.parse.quote(query)

        print(f"Original: {query}")
        print(f"Old (broken): {old_encoded}")
        print(f"New (fixed):  {new_encoded}")
        print("-" * 80)

        # Test URL construction
        base_url = "https://scholar.google.com/scholar?start={}&q={}&hl=en&as_sdt=0,5"
        old_url = base_url.format("0", old_encoded)
        new_url = base_url.format("0", new_encoded)

        print(f"Old URL: {old_url}")
        print(f"New URL: {new_url}")
        print("=" * 80)

if __name__ == "__main__":
    test_url_encoding()