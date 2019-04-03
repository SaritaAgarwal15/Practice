for _ in range(int(input())):
    a=str(input())
    n=int(a)
    count=0
    for i in range(len(a)):
        if a[i]=='4':
            count=count+1
    print(count)
