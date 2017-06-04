a = input()
a = list(a)
c = []
print(a)
n = len(a)
for i in range(n - 2):
    for u in range(n - 2):
    c.append(a[i]+a[i+1])
print(c)
