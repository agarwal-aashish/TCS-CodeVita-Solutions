n=int(input())
r1,r2=map(int,input().split())
target=int(input())
di={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
i=0
while i<=n:
    gen=0
    non=n-i
    for m in di.keys():
        for d in range(1,di[m]+1):
            pat=((6-m)**2)+abs(d-15)
            x=min(pat,n)
            if x>non:
                gen+=non*r2
                y=x-non
                gen+=y*r1
            else:
                gen+=x*r2
    if gen>=target:
        break
    i+=1
print(i,end='')
        
