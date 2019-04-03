a=int(input())
A=[int(x) for x in input().split()]
c=int(input())
C=[int(y) for y in input().split()]
B=[]
for e in range(max(C)-max(A)+1):
    for i in A:
        for j in C:
            if e+i==j:
                if e not in B:
                    B.append(e)
for t in B:
    for k in A:
        if t+k not in C:
            B.remove(t)
B.sort()
print(*B, sep=' ')
