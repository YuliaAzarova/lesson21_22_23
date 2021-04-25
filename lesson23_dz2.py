n = int(input())
a = b = []
x = str(n)
count = 0
In = int()
e = 1
for i in range(len(x)):
    a.append(x[i])
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        b.append(a[i])
        b.sort()
        In = b[+0]
        print(In)
        e += 1
        count += 1

if (e>0):
    print(In)
if (count ==0 ):
    print('NO')