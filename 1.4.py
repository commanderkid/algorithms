n = int(input())
c = []
for i in range(n+1):
    
    a = i**2 / n**2
    c.append(a)
b = sum(c)    
print(n, n/b)
