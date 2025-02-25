import re

def match_pattern(a):
    p = r"^[a-z]+_[a-z]+$"  
    if re.match(p, a):
        return "Yes"
    else:
        return "No"

test = ["abb", "abbb", "a", "ab", "abbbb", "ba", "abbc"]
for s in test:
    print(f"'{s}': {match_pattern(s)}")
