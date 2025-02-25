import re

def sequ(text):
    p = r'[A-Z][a-z]+'  
    m = re.findall(p, text)
    return m

text = ["Hello world"]
s = sequ(text)
print (s)