import math
ts = 1 #seconds
tm = 60*ts #minuts
th = 60*tm #hours
td = th*24 #days
tw = td*7 #weaks
ty = tw*365 #years
alpha = 1000000 #steps per second

def nn(y):
    c, n = 1, 1
    while c<=y:
        n += 1
        c = n**2
    return n-1

def n2(y):
    c, n = 1, 1
    while c <= y:
        n += 1
        c = 2**n
    return n-1  

def log(y):
    c, n = 1, 1
    while c <= y:
        n += 1
        c = 2**n
    return n-1  

def fact(y):
    c, n = 1, 1
    while c <= y:
        n += 1
        c = c*n
    return n-1

def sqrut(y):
    c, n = 1, 1
    while c <= y:
        c = math.sqrt(n)
        n += 1
    return n-1
        
print("-----------------------------")
print("time|seconds|steps|log2N|sqrt(N)|N|N^2|2^N|N!|")
print("-----------------------------")
print("1 second", ts, alpha, "|", math.log2(3),"|", sqrut(ts),"|", nn(ts*alpha),"|", alpha,"|", n2(ts*alpha),"|", fact(alpha),"|")
print("1 minut", tm, tm*alpha, "|", math.log2(3),"|", sqrut(tm),"|", nn(tm*alpha),"|", tm*alpha,"|", n2(tm*alpha),"|", fact(tm*alpha),"|")
#print("1 hour", th, th*alpha, "|", math.log2(3),"|", sqrut(th),"|", nn(th*alpha),"|", th*alpha,"|", n2(th*alpha),"|", fact(th*alpha),"|")
#print("1 days", td, td*alpha, "|", math.log2(3),"|", sqrut(td),"|", nn(td*alpha),"|", td*alpha,"|", n2(td*alpha),"|", fact(td*alpha),"|")
#print("1 weak", tw, tw*alpha, "|", math.log2(3),"|", sqrut(tw),"|", nn(tw*alpha),"|", tw*alpha,"|", n2(tw*alpha),"|", fact(tw*alpha),"|")
#print("1 year", ty, ty*alpha, "|", math.log2(3),"|", sqrut(ty),"|", nn(ty*alpha),"|", ty*alpha,"|", n2(ty*alpha),"|", fact(ty*alpha),"|")
