#!/usr/bin/env python3
import argparse
import sys

def test_argparse():
    parser = argparse.ArgumentParser(description="Test argument parsing")
    parser.add_argument(
        "kw",
        nargs='*',  # Allow multiple positional arguments
        help="Keyword to be searched",
        default=["machine learning"],
    )

    args, _ = parser.parse_known_args()

    # Join all keyword parts back together with spaces
    keyword = " ".join(args.kw) if args.kw else "machine learning"

    print(f"Parsed keyword: '{keyword}'")
    print(f"Raw sys.argv: {sys.argv}")

if __name__ == "__main__":
    test_argparse()