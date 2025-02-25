import re

def match_pattern(s):
    return re.sub(r'[ ,.]', ':', s)

test = ["Hello, world. Welcome to Python", "This is a test, with spaces, commas, and dots.", "NoSpecialCharacters"]
for s in test:
    print(f"'{s}': {match_pattern(s)}")
