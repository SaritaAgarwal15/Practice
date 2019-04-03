for _ in range(int(input())):
    M,x,y=[int(x) for x in input().split()]
    cop=[int(y) for y in input().split()]
    l=[]
    for i in range(1,101):
        l.append(i)
    p=x*y
    for j in range(0,M):
        for k in range(cop[j]-p,cop[j]+p+1):
            if k in l:
                l.remove(k)
    print(len(l))
