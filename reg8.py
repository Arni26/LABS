import re

def split(s):
    return re.findall('[A-Z][^A-Z]*', s)

s = "HelloWorldExample"

print(split(s))
