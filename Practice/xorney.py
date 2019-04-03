for _ in range(int(input())):
    l,r=input().split(' ')
    l=int(l)
    r=int(r)
    d=r-l+1
    if d%4==0:
        print('Even')
    elif d%4==1:
        if r%2==0:
            print('Even')
        else:
            print('Odd')
    elif d%2==0:
        print('Odd')
    else:
        if r%2==0:
            print('Odd')
        else:
            print('Even')
