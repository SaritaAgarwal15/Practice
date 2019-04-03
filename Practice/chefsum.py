for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split()]
    sump=0
    sums=0
    sum=[]
    for i in range(n):
        for j in range(0,i+1):
            sump=sump+l[j]
        for k in range(i,n):
            sums=sums+l[k]
        s=sump+sums
        sum.append(s)
        sump=0
        sums=0
    print(sum.index(min(sum))+1)
