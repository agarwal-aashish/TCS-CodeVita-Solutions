n=int(input())
t=int(input())
mat=[]
for i in range(n):
    l=list(map(int,input().split()))
    for i in range(1,t):
        l[i]+=l[i-1]
    mat.append(l.copy())
ct=(t-1)//2
res=[[0]*ct for i in range(n)]
for i in range(n):
    for j in range(ct):
        res[i][j]=mat[i][(j*2)+1]*mat[i][-1]
winner=[0]*n
for i in range(ct):
    m=0
    for j in range(n):
        if res[j][i]>m:
            m=res[j][i]
            best=j
    winner[best]+=1
x=max(winner)
print(winner.index(x)+1,end='')
