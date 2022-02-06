"""
Implement an algorithm to determine if a string has all unique characters.

Cracking the coding interview 1.1
"""

def all_unique_characters(input: str) -> bool:
    return len(input) != len(set(input))
