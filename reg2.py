import re

def match_pattern(a):
    p = r'^ab{2,3}$'  
    if re.match(p, a):
        return "Yes"
    else:
        return "No"

test = ["abb", "abbb", "a", "ab", "abbbb", "ba", "abbc"]
for s in test:
    print(f"'{s}': {match_pattern(s)}")
