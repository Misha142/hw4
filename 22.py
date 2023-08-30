n = int(input())
m = int(input())
x=[]
y=[]
for _ in range(n):
    x.append(int(input()))
for _ in range(m):
    y.append(int(input()))
x=set(x)
y=set(y)
z = x.intersection(y)
z=list(z)
z.sort()
print(*z)