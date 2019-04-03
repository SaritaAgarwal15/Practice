for _ in range(int(input())):
    n=int(input())
    m=[int(x) for x in input().split()]
    s=[]
    for i in range(n):
        for j in range(i+1,n):
            sum=m[i]+m[j]
            s.append(sum)
    mx=max(s)
    c=s.count(mx)
    p=c/len(s)
    print(format(p, '.8f'))
