import math
ts=1 #seconds
tm=60*ts #minuts
th=60*tm #hours
td=th*24 #days
tw=td*7 #weaks
ty=tw*365 #years
alpha=1000000 #steps per second

def n2(y):
    n
    while c<=y:
        n+=1
        c=2**n
    return n-1
print(n2(y))    


#print("-----------------------------")
#print("time|seconds|steps|log2N|sqrt(N)|N|N^2|2^N|N!|")
#print("-----------------------------")
#print("1 second", ts, alpha, "|", math.log2(alpha),"|", math.sqrt(alpha),"|", alpha,"|", alpha**2,"|", 2**alpha,"|", 2**alpha,"|", math.factorial(alpha),"|")
#print("1 weak", tm, tm*alpha, "|", math.log2(tm*alpha),"|", math.sqrt(tm*alpha),"|", tm*alpha,"|", (tm*alpha)**2,"|", 2**(tm*alpha),"|", math.factorial(tm*alpha),"|")
#print("1 hour", th, th*alpha, "|", math.log2(th*alpha),"|", math.sqrt(th*alpha),"|", th*alpha,"|", (th*alpha)**2,"|", 2**(th*alpha),"|", math.factorial(th*alpha),"|")
#print("1 days", td, td*alpha, "|", math.log2(td*alpha),"|", math.sqrt(td*alpha),"|", td*alpha,"|", (td*alpha)**2,"|", 2**(td*alpha),"|", math.factorial(td*alpha),"|")
#print("1 weak", tw, tw*alpha, "|", math.log2(tw*alpha),"|", math.sqrt(tw*alpha),"|", tw*alpha,"|", (tw*alpha)**2,"|", 2**(tw*alpha),"|", math.factorial(tw*alpha),"|")
#print("1 year", ty, ty*alpha, "|", math.log2(ty*alpha),"|", math.sqrt(ty*alpha),"|", ty*alpha,"|", (ty*alpha)**2,"|", 2**(ty*alpha),"|", math.factorial(ty*alpha),"|")
