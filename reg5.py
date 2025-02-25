
import re

def match_pattern(s):
    p = r'^a.*b$'  
    if re.match(p, s):
        return "Yes"
    else:
        return "No"

test = ["a", "ab", "abb", "b", "ba", "abc", "aabb"]
for s in test:
    print(f"'{s}': {match_pattern(s)}")
