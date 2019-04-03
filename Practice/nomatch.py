for _ in range(int(input())):
    n=int(input())
    d=n//2
    p=[int(x) for x in input().split()]
    p.sort()
    sum=0
    for i in range(d):
        s=abs(p[i]-p[i+d])
        sum=s+sum
    print(sum)
