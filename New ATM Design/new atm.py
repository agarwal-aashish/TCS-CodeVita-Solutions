n=int(input())
amt=int(input())
h=int(input())
t=int(input())
f=int(input())
th=int(input())
out=0
flag=1
if n>=1:
    for i in range(th+1):
        s=i*1000
        if i>n or s>amt:
            break
        elif s<amt:
            for j in range(f+1):
                s1=s+j*500
                if i+j>n or s1>amt:
                    break
                elif s1<amt:
                    for k in range(t+1):
                        s2=s1+k*200
                        if i+j+k>n or s2>amt:
                            break
                        elif s2<amt:
                            for l in range(h+1):
                                s3=s2+l*100
                                if i+j+k+l>n or s3>amt:
                                    break
                                if s3==amt:
                                    out=i+j+k+l
                                    flag=0
                                    break
                        elif s2==amt:
                            out=i+j+k
                            flag=0
                            break
                        if not flag:
                            break
                elif s1==amt:
                    out=i+j
                    flag=0
                    break
                if not flag:
                    break
        elif s==amt:
            out=i
            break
        if not flag:
            break                   
print(out,end='')
                            
                        
        
        
        
