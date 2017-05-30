i=1
y=int(input())
import math
def fact(y):
    for i in range(y):
        if math.factorial(i)<=y:
            i+=1
        else:
            print(i)
print(fact(y))
