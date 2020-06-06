def f(num,base):
    n=len(num)
    i=n-1
    p=0
    val=0
    while i>=0:
        t=ord(num[i])
        if t>=48 and t<=57:
            val+=(t-48)*(base**p)
        else:
            val+=(t-65+10)*(base**p)
        i-=1
        p+=1
    return val

l=list(input().split())
base=[]
val=[]
for i in l:
    temp=max(i)
    t=ord(temp)
    if t>=48 and t<=57:
        base.append(t-48+1)
    else:
        base.append(t-65+11)
i=0
n=len(l)
while i<n:
    val.append(f(l[i],base[i]))
    i+=1
print(min(val),end='')
