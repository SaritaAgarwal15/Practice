for _ in range(int(input())):
    n=int(input())
    sum=0
    l=[int(x) for x in input().split()]
    for i in l:
        sum=sum+i
    if sum%2==1:
        print('YES')
    else:
        print('NO')
