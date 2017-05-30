#N^2-N
a, i, j = 0, 0, 0
n, g = 1000, 1000
for i in range(n-1):
    j=i+1
    for j in range(g):
        a = a + 1
print(a)
