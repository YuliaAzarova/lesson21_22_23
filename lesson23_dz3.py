n = int(input())
x = str(n)
a = b = []
for i in range(len(x)):
    a.append(int(x[i]))
    if a[i] % 2 == 0 or a[0] % 2 == 0:
        b.append(a[i])
        b.sort()
print(sum(b))