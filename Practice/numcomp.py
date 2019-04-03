for _ in range(int(input())):
    a,b,n=[int(x) for x in input().split()]
    p=a**n
    q=b**n
    if (n%2)==0:
        if abs(a)==abs(b):
            print(0)
        elif abs(a)<abs(b):
            print(2)
        else:
            print(1)
    else:
        if p>q:
            print(1)
        elif p<q:
            print(2)
        elif p==q:
            print(0)
