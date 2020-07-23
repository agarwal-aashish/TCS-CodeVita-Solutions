n=int(input())
l=list(map(int,input().split()))
bitscore=[]
for i in range(n):
    num=l[i]
    ma=0
    mi=9
    while num>0:
        x=num%10
        ma=max(ma,x)
        mi=min(mi,x)
        num//=10
    ma*=11
    mi*=7
    s=ma+mi
    s=str(s)
    if len(s)>2:
        s=s[1:]
    bitscore.append(s)
pairs=0
used=[0]*10
for i in range(0,n,2):
    x=int(bitscore[i][0])
    if used[x]>=2:
        continue
    for j in range(i+2,n,2):
        if bitscore[i][0]==bitscore[j][0]:
            used[x]+=1
            pairs+=1
for i in range(1,n,2):
    x=int(bitscore[i][0])
    if used[x]>=2:
        continue
    for j in range(i+1,n,2):
        if bitscore[i][0]==bitscore[j][0]:
            used[x]+=1
            pairs+=1
print(pairs,end='')
