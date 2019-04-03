for _ in range(int(input())):
    p=[]
    for i in range(3):
        s=str(input())
        p.append(s)
    ans=0
    for i in range(2):
        if (p[i][0]=='l'):
            if (p[i+1][0]=='l'):
                if (p[i+1][1]=='l'):
                    ans=1
        elif (p[i][1]=='l'):
            if (p[i+1][1]=='l'):
                if (p[i+1][2]=='l'):
                    ans=1
        else:
            ans=0
    if ans==1:
        print('yes')
    elif ans==0:
        print('no')
