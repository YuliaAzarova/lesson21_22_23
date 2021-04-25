n = int(input())
a = []
x = str(n)
for i in range(len(x)):
    a.append(x[i])
a.sort()
ln = a[-1]
In = a[+0]
print(In, ln)