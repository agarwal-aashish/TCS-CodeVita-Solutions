n=int(input())
s=input()
freq=[0]*26
process=[0]*n
for i in range(n):
    process[i]=freq[ord(s[i])-97]
    freq[ord(s[i])-97]+=1
q=int(input())
for _ in range(q-1):
    x=int(input())    
    print(process[x-1])
x=int(input())
print(process[x-1],end='')
