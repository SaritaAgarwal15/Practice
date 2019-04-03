m=[]
mn=[]
mx=[]
n=int(input())
for _ in range(n):
    a=[int(x) for x in input().split()]
    m.append(a)
    mn.append(min(a))
for j in range(n):
    c=0
    for i in range(n):
        if c<m[i][j]:
            c=m[i][j]
    mx.append(c)
print(mn)
print(mx)
