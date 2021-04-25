x = int(input())
m = 0

while (x):
    if (x % 10 > m):
        m = x % 10
    x //= 10

print(m)