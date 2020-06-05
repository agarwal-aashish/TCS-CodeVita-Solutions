t=int(input())
for _ in range(t):
    p=input()
    s=input()
    out=''
    freq=[0]*26
    for i in range(len(s)):
        freq[ord(s[i])-97]+=1
    for i in p:
        if freq[ord(i)-97]==0:
            continue
        out+=i*freq[ord(i)-97]
    if _==t-1:
        print(out,end='')
    else:
        print(out)
