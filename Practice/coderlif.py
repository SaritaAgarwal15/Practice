for _ in range(int(input())):
    s=str(input())
    s=s.split('0')
    d=0
    for i in s:
        i=i.strip(' ')
        if len(i)>9:
            d=1
    if d==1:
        print('#coderlifematters')
    else:
        print('#allcodersarefun')
