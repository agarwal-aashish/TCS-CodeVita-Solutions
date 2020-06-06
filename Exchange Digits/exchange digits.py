def combi(l,lo,hi):
    global x
    if lo==hi:
        s=''
        for i in l:
            s+=i
        x.append(int(s))
    else:
        for i in range(lo,hi+1):
            if lo !=i:
                l[lo],l[i]=l[i],l[lo]
            combi(l,lo+1,hi)
            if lo != i:
                l[lo],l[i]=l[i],l[lo]

a,b=input().split()
b=int(b)
a=list(a)
x=[]
combi(a,0,len(a)-1)
x=set(x)
x=list(x)
best=10**9
flag=0
for i in x:
    if i>b and i<best:
        best=i
        flag=1
if flag:
    print(best)
else:
    print(-1)
        
