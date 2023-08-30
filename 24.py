n=int(input())
ch=[]
for _ in range(n):
    ch.append(int(input()))
maxx=ch[0]+ch[-1]+ch[-2]
for i in range(n-1):
    if ch[i-1]+ch[i]+ch[i+1]>maxx:
        maxx=ch[i-1]+ch[i]+ch[i+1]
print(maxx)