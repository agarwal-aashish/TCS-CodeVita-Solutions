from math import log
t=int(input())
for _ in range(t):
    n=int(input())
    out=int(log(n,2))
    print(out+1)
