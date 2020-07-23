minl=int(input())
maxl=int(input())
minw=int(input())
maxw=int(input())
out=0
memo=[[0]*(maxw+1) for i in range(maxl+1)]
for i in range(maxl+1):
    memo[i][0]=0
for i in range(maxw+1):
    memo[0][i]=0
for i in range(1,maxl+1):
    for j in range(1,maxw+1):
        a,b=i,j
        if a>b:
            a-=b
        else:
            b-=a
        memo[i][j]=memo[a][b]+1
for i in range(minl,maxl+1):
    for j in range(minw,maxw+1):
        out+=memo[i][j]
print(out)
