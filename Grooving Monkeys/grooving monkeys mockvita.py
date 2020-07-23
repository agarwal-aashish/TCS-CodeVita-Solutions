t=int(input())
for _ in range(t):
    n=int(input())
    pos=list(map(int,input().split()))
    initial=[i for i in range(n)]
    cur=[0]*n
    c=1
    for i in range(n):
        cur[pos[i]-1]=initial[i]
    while initial!=cur:
        x=[0]*n
        for i in range(n):
            x[pos[i]-1]=cur[i]
        cur=x.copy()
        c+=1
    print(c)
