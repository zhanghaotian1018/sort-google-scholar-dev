#!/usr/bin/env python3
"""
Test the improved venue and publisher extraction
"""

from sortgs.sortgs import clean_text, get_venue_and_publisher, extract_venue_from_publisher

# Test cases based on actual Google Scholar format: Author - Year - Publisher
test_cases = [
    ("CM Bishop - 2006 - Springer", "Pattern recognition and machine learning"),
    ("E Alpaydin - 2021 - books.google.com", "Introduction to machine learning"),
    ("KP Murphy - 2012 - books.google.com", "Machine learning: a probabilistic perspective"),
    ("DE King - 2009 - The Journal of Machine Learning Research", "Dlib-ml: A machine learning toolkit"),
    ("KT Butler - 2018 - Nature", "Machine learning for molecular and materials science"),
    ("JJ Grefenstette - 1993 - ACM", "Genetic algorithms and machine learning"),
]

print("=" * 100)
print("Testing Venue and Publisher Extraction (Author - Year - Publisher format)")
print("=" * 100)

for i, (metadata, title) in enumerate(test_cases, 1):
    print(f"\nTest Case {i}: {title}")
    print(f"Input: {metadata}")
    venue, publisher = get_venue_and_publisher(metadata)
    print(f"  Publisher: {publisher if publisher else '(empty)'}")
    print(f"  Venue: {venue if venue else '(empty)'}")
    print("-" * 100)

# Test extract_venue_from_publisher
print("\n" + "=" * 100)
print("Testing Venue Extraction from Publisher")
print("=" * 100)

publisher_tests = [
    "Springer",
    "books.google.com",
    "The Journal of Machine Learning Research",
    "Nature",
    "ACM Transactions on Computer Systems",
    "IEEE Transactions on Pattern Analysis",
    "Proceedings of the 2023 Conference",
]

for publisher in publisher_tests:
    venue = extract_venue_from_publisher(publisher)
    print(f"Publisher: '{publisher}'")
    print(f"  Extracted Venue: '{venue if venue else '(no venue detected)'}'")
    print()

print("All tests completed!")
