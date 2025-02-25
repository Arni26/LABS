import re


def camel(a):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', a).lower()


s = "helloWorldExample"

print(camel(s))
