from itertools import combinations

x=int(input())
s=int(input())
y=int(input())
m=int(input())
z=int(input())
c=int(input())
a,b=input().split()
one=input()
total=x+y+z
select=s+m+c
i=65
simple=[]
medium=[]
hard=[]
while i<65+x:
    simple.append(chr(i))
    i+=1
while i<65+x+y:
    medium.append(chr(i))
    i+=1
while i<65+x+y+z:
    hard.append(chr(i))
    i+=1
out=[]
l1=combinations(simple,s)
for i in l1:
    sq=list(i)
    l2=combinations(medium,m)
    for j in l2:
        mq=list(j)
        l3=combinations(hard,c)
        for k in l3:
            hq=list(k)
            out.append(sq+mq+hq)
best=[]
print(out)
print(len(out))
for i in out:
    if a in i:
        if b in i:
            continue
        else:
            best.append(i)
    else:
        best.append(i)
print(best)
del(out)
c=0
flag=1
for i in best:
    if one in i:
        if flag:
            c+=1
            flag=0
    else:
        c+=1
print(c,end='')
