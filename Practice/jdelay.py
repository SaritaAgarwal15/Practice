for _ in range(int(input())):
    n=int(input())
    c=0
    for i in range(n):
        a,b=[int(x) for x in input().split()]
        if b-a>5:
            c+=1
    print(c)
