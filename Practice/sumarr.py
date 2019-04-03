for _ in range(int(input())):
    N,M,K=[int(x) for x in input().split()]
    A=[int(y) for y in input().split()]
    B=A*M
    print(B)
    cnt=0
    for i in range(N*M):
        for j in range(1,N*M):
            t=B[i:j+i]
            print(t)
            if sum(t)<=K:
                cnt=cnt+1
            elif sum(t)>K:
                i=i+1
        continue
    print(cnt)
