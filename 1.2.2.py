
y=int(input())  
def n2(y):
    n=1
    c=1
    while c<=y:
        n+=1
        c=2**n
    return n
print(n2(y))    
