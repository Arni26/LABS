import re

def snake(a):
    c = a.split('_')
    return c[0] + ''.join(x.title() for x in c[1:])


s = "hello_world_example"

print(snake(s))

