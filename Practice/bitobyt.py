for _ in range(int(input())):
    N=int(input())
    p=N // 26
    N=N%26
    if N==0 and p!=0:
        b=0
        ni=0
        bt=2**(p-1)
    elif p==0 and N==0:
        b=1
        ni=0
        bt=0
    elif 0<N<=2:
        b=2 ** p
        ni=0
        bt=0
    elif 2<N<=10:
        b=0
        ni=2 ** p
        bt=0
    elif 10<N<=26:
        b=0
        ni=0
        bt=2 ** p
    print(b, ni, bt)
