for _ in range(int(input())):
    N=int(input())
    C=[int(x) for x in input().split()]
    L=[int(y) for y in input().split()]
    cost=0
    f=0
    for i in range(f,N):
        s=L[i]
        for j in range(i+1,N):
            if C[i]<=C[j]:
                s=s+L[j]
                f=i+j
            elif C[i]>C[j]:
                p=L[j]*C[j]
                f=i+1
        cost=cost+p
    print(cost)
