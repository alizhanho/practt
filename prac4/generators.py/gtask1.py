def squares(n):
    for i in range(1, n + 1):
        yield i * i

N = int(input())
for square in squares(N):
    print(square)