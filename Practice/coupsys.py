t=int(input())
while t>0:
    n=int(input())
    d1=0
    c1=0
    d2=0
    c2=0
    d3=0
    c3=0
    for i in range(n):
        a=[int(x) for x in input().split()]
        if a[1]==1:
            if d1<a[2]:
                d1=a[2]
                c1=a[0]
            elif d1==a[2]:
                if c1>a[0]:
                    c1=a[0]
        if a[1]==2:
            if d2<a[2]:
                d2=a[2]
                c2=a[0]
            elif d2==a[2]:
                if c2>a[0]:
                    c2=a[0]
        if a[1]==3:
            if d3<a[2]:
                d3=a[2]
                c3=a[0]
            elif d3==a[2]:
                if c3>a[0]:
                    c3=a[0]
    print(d1,c1)
    print(d2,c2)
    print(d3,c3)
    t=t-1
