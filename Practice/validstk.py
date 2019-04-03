for _ in range(int(input())):
    n=int(input())
    l=[int(x) for x in input().split(' ')]
    sum=0
    for i in l:
        if i==1:
            sum+=1
        else:
            sum-=1
        if sum<0:
            print('Invalid')
            break
    if sum>=0:
        print('Valid')
