s = int(input())
ans = 0
while s != 0:
    if s % 2 == 0:
        ans += 1
    s = int(input())
print(ans)