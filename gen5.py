def squares(a):
    for i in range(a, -1, -1):
        yield i
        
a = int(input())

for square in squares(a):
    print(square)