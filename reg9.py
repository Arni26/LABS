import re

def insert(a):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', a)

s = "HelloWorldExample"

print(f"Insert Spaces: {insert(s)}")

