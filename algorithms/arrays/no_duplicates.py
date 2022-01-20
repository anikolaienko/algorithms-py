def no_duplicates(input: str) -> bool:
    chars = set()
    for ch in input:
        if ch in chars:
            return False
        chars.add(ch)
    return True
