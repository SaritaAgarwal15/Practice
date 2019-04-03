for _ in range(int(input())):
    s=str(input())
    ca=0
    cb=0
    Al=[]
    Bl=[]
    dt=0
    for i in s:
        if i=='.':
            dt+=1
    if dt==len(s):
        ca=0
        cb=0
    else:
        z=s.find('A')
        y=s.find('B')
        if (z<y and z!=-1) or y==-1:
            s=s[z:]
        elif (z>y and y!=-1) or z==-1:
            s=s[y:]
        s=s[::-1]
        z1=s.find('A')
        y1=s.find('B')
        if z1<y1 and z1!=-1 or y1==-1:
            s=s[z1:]
        elif z1>y1 and y1!=-1 or z1==-1:
            s=s[y1:]
        for i in range(len(s)):
            if s[i]=='A':
                ca+=1
            elif s[i]=='B':
                cb+=1
        p=s.split('A')
        for j in range(len(p)):
            if 'B' in p[j]:
                Al.append(p[j])
        for i in Al:
            p.remove(i)
        for k in p:
            for m in k:
                if m=='.':
                    ca+=1
        n=s.split('B')
        for j in range(len(n)):
            if 'A' in n[j]:
                Bl.append(n[j])
        for i in Bl:
            n.remove(i)
        for k in n:
            for m in k:
                if m=='.':
                    cb+=1
    print(ca,cb)
