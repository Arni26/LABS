def even(n):
    for i in range(0, n+1, 1):
        if (i%3==0 or i%4==0):
            yield i
        

n = int(input())

even_numbers = even(n)

print(", ".join(map(str, even_numbers)))
