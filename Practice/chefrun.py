for _ in range(int(input())):
    c,k,b,vc,vk=[int(x) for x in input().split()]
    tc=abs(b-c)/vc
    tk=abs(b-k)/vk
    if tc>tk:
        print('Kefa')
    elif tk>tc:
        print('Chef')
    elif tk==tc:
        print('Draw')
