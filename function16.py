def revers(sentence):
    word = sentence.split()
    r = " ".join(reversed(word))
    return r

a = input()
print(revers(a))