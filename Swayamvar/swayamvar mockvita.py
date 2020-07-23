n=int(input())
brides=input()
grooms=input()
gf={'r':0,'m':0}
for i in grooms:
    gf[i]+=1
count=0
for i in brides:
    if gf[i]==0:
        break
    gf[i]-=1
    count+=1
print(n-count)
