def even(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())

even_numbers = even(n)

print(", ".join(map(str, even_numbers)))
