def findpath(i,j,prev,char):
    global mat,n,m,di,dj
    res=[[0]*m for x in range(n)]
    for a in range(n):
        for b in range(m):
            if mat[a][b]=='s':
                res[a][b]='-'
            else:
                res[a][b]=mat[a][b]
    res[i][j]=chr(char)
    x=prev[di][dj][0]
    y=prev[di][dj][1]
    while prev[x][y]!=0:
        res[x][y]=chr(char)
        x,y=prev[x][y][0],prev[x][y][1]
    for a in res:
        for b in a:
            print(b,end=' ')
        print()

def fun(i,j):
    global mat,n,m
    rc=[0,0,-1,1,-1,1,-1,1]
    cc=[-1,1,0,0,-1,-1,1,1]
    adj=[]
    for k in range(8):
        x=i+rc[k]
        y=j+cc[k]
        if x<0 or y<0 or x>=n or y>=m or mat[x][y]=='w':
            continue
        adj.append([x,y])
    return adj

def bfs(i,j,char):
    global mat,n,m
    queue=[[i,j]]
    visited=[[0]*m for x in range(n)]
    visited[i][j]=1
    prev=[[0]*m for x in range(n)]
    while len(queue)>0:
        cur=queue.pop(0)
        adj=fun(cur[0],cur[1])
        for k in adj:
            x,y=k[0],k[1]
            if visited[x][y]==0:
                queue.append([x,y])
                visited[x][y]=1
                prev[x][y]=cur.copy()
    findpath(i,j,prev,char)

 
n,m=map(int,input().split())
mat=[]
for i in range(n):
    l=list(input().split())
    mat.append(l.copy())
input()
for i in range(n):
    for j in range(m):
        if mat[i][j]=='d':
            di,dj=i,j
            break
char=97
for i in range(n):
    for j in range(m):
        if mat[i][j]=='s':
            bfs(i,j,char)
            char+=1
