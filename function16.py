def revers(sentence):
    word = sentence.split()
    r = " ".join(reversed(words))
    return r

a = input()
print(revers(a))