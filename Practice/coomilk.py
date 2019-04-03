for _ in range(int(input())):
    n=int(input())
    l=[str(x) for x in input().split(' ')]
    c=0
    for i in range(n-1):
        if l[i]=='cookie' and l[i+1]=='milk':
            c+=1
    if l.count('cookie')==c:
        print('YES')
    elif l.count('milk')==len(l):
        print('YES')
    else:
        print('NO')
