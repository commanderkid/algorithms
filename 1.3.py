a = input()
a = list(a)
c = []
print(a)
n = len(a)
for i in range(n - 1):
    for u in range(n - 1):
        c.append(a[i]+a[u+1])
        f=a[u+1]+a[i]
        if f in c:
            c.pop(i)
        if a[i]==a[u+1]:
            c.pop()
print(c)

