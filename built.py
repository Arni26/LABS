from functools import reduce
import time
import math

def listt(numbers):
    return reduce(lambda x, y: x * y, numbers)


def count(s):
    upper_case = sum(1 for char in s if char.isupper())
    lower_case = sum(1 for char in s if char.islower())
    return upper_case, lower_case


def palindrome(s):
    return s == s[::-1]


def delay(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)


def all_true(t):
    return all(t)

print(listt([1, 2, 3, 4])) 
print(count("Hello World"))  
print(palindrome("madam")) 
print(delay(25100, 2123))
print(all_true((True, True, False))) 
